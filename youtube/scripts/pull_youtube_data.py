#!/usr/bin/env python3
"""Pull @balajichippada YouTube channel data via terminal (no Cursor MCP)."""

from __future__ import annotations

import json
import os
import sys
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

CONFIG = Path.home() / ".youtube-mcp"
OUTPUT_ROOT = Path(__file__).resolve().parents[1] / "data"


def setup_env() -> None:
    os.environ.setdefault("YOUTUBE_MCP_CONFIG_DIR", str(CONFIG))
    os.environ.setdefault("YOUTUBE_MCP_CLIENT_SECRET", str(CONFIG / "client_secret.json"))


def save(out_dir: Path, name: str, data: object) -> Path:
    path = out_dir / f"{name}.json"
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False, default=str))
    return path


def run_analytics(analytics, metrics: str, *, dimensions: str = "", days: int = 30, **kwargs):
    end = date.today()
    start = end - timedelta(days=days)
    params = {
        "ids": "channel==MINE",
        "startDate": start.isoformat(),
        "endDate": end.isoformat(),
        "metrics": metrics,
    }
    if dimensions:
        params["dimensions"] = dimensions
    params.update(kwargs)
    resp = analytics.reports().query(**params).execute()
    cols = [h["name"] for h in resp.get("columnHeaders", [])]
    rows = [dict(zip(cols, row)) for row in resp.get("rows", [])]
    return {
        "start_date": params["startDate"],
        "end_date": params["endDate"],
        "columns": cols,
        "results": rows,
        "total_rows": len(rows),
    }


def get_channel(youtube):
    ch = youtube.channels().list(part="snippet,statistics,contentDetails", mine=True).execute()["items"][0]
    snippet, stats = ch["snippet"], ch["statistics"]
    return {
        "id": ch["id"],
        "title": snippet.get("title"),
        "handle": snippet.get("customUrl"),
        "published_at": snippet.get("publishedAt"),
        "subscribers": int(stats.get("subscriberCount", 0)),
        "total_views": int(stats.get("viewCount", 0)),
        "video_count": int(stats.get("videoCount", 0)),
        "uploads_playlist_id": ch["contentDetails"]["relatedPlaylists"]["uploads"],
    }


def list_all_video_ids(youtube, uploads_playlist_id: str) -> list[str]:
    ids: list[str] = []
    token = None
    while True:
        resp = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=uploads_playlist_id,
            maxResults=50,
            pageToken=token,
        ).execute()
        ids.extend(item["contentDetails"]["videoId"] for item in resp.get("items", []))
        token = resp.get("nextPageToken")
        if not token:
            break
    return ids


def get_videos(youtube, video_ids: list[str]) -> list[dict]:
    videos: list[dict] = []
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i : i + 50]
        resp = youtube.videos().list(
            part="snippet,statistics,contentDetails",
            id=",".join(batch),
        ).execute()
        for v in resp.get("items", []):
            s, st, c = v["snippet"], v["statistics"], v["contentDetails"]
            dur = c.get("duration", "")
            videos.append(
                {
                    "id": v["id"],
                    "title": s.get("title"),
                    "published_at": s.get("publishedAt"),
                    "duration": dur,
                    "views": int(st.get("viewCount", 0)),
                    "likes": int(st.get("likeCount", 0)),
                    "comments": int(st.get("commentCount", 0)),
                    "url": f"https://www.youtube.com/watch?v={v['id']}",
                }
            )
    videos.sort(key=lambda x: x["published_at"] or "", reverse=True)
    return videos


def list_playlists(youtube, channel_id: str) -> list[dict]:
    playlists: list[dict] = []
    token = None
    while True:
        resp = youtube.playlists().list(
            part="snippet,contentDetails",
            channelId=channel_id,
            maxResults=50,
            pageToken=token,
        ).execute()
        for p in resp.get("items", []):
            playlists.append(
                {
                    "id": p["id"],
                    "title": p["snippet"]["title"],
                    "video_count": int(p["contentDetails"]["itemCount"]),
                    "published_at": p["snippet"].get("publishedAt"),
                }
            )
        token = resp.get("nextPageToken")
        if not token:
            break
    return playlists


def pull_comments(youtube, video_ids: list[str], max_per_video: int = 50) -> list[dict]:
    all_comments: list[dict] = []
    for vid in video_ids:
        try:
            resp = youtube.commentThreads().list(
                part="snippet",
                videoId=vid,
                maxResults=min(max_per_video, 100),
                order="time",
                textFormat="plainText",
            ).execute()
        except Exception as exc:
            all_comments.append({"video_id": vid, "error": str(exc), "comments": []})
            continue
        comments = []
        for item in resp.get("items", []):
            top = item["snippet"]["topLevelComment"]["snippet"]
            comments.append(
                {
                    "comment_id": item["snippet"]["topLevelComment"]["id"],
                    "author": top.get("authorDisplayName"),
                    "text": top.get("textDisplay"),
                    "likes": top.get("likeCount", 0),
                    "published_at": top.get("publishedAt"),
                    "reply_count": item["snippet"].get("totalReplyCount", 0),
                }
            )
        all_comments.append({"video_id": vid, "comments": comments, "total": len(comments)})
    return all_comments


def day_of_week_aggregate(daily_rows: list[dict]) -> list[dict]:
    names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    totals: dict[str, dict] = defaultdict(lambda: {"views": 0, "minutes": 0, "days": 0})
    for row in daily_rows:
        d = date.fromisoformat(row["day"])
        key = names[d.weekday()]
        totals[key]["views"] += row.get("views", 0)
        totals[key]["minutes"] += row.get("estimatedMinutesWatched", 0)
        totals[key]["days"] += 1
    out = []
    for name in names:
        t = totals[name]
        n = t["days"] or 1
        out.append(
            {
                "day": name,
                "avg_views": round(t["views"] / n, 1),
                "avg_minutes": round(t["minutes"] / n, 1),
                "sample_days": t["days"],
            }
        )
    return out


def build_summary(channel, videos, overview_30, top_videos, traffic, comments) -> str:
    lines = [
        f"# YouTube Data Pull — {channel['title']} ({channel['handle']})",
        f"",
        f"Pulled: {date.today().isoformat()}",
        f"",
        f"## Channel snapshot",
        f"- Subscribers: **{channel['subscribers']:,}**",
        f"- Total views: **{channel['total_views']:,}**",
        f"- Videos on channel: **{channel['video_count']}**",
        f"",
    ]
    if overview_30["results"]:
        o = overview_30["results"][0]
        lines += [
            f"## Last 30 days",
            f"- Views: **{int(o.get('views', 0)):,}**",
            f"- Watch time (minutes): **{int(o.get('estimatedMinutesWatched', 0)):,}**",
            f"- Subs gained: **{int(o.get('subscribersGained', 0)):,}** (lost: {int(o.get('subscribersLost', 0)):,})",
            f"- Likes: **{int(o.get('likes', 0)):,}** | Comments: **{int(o.get('comments', 0)):,}**",
            f"",
        ]
    lines.append("## Top videos (30d analytics)")
    for i, row in enumerate(top_videos.get("results", [])[:10], 1):
        vid = row.get("video", "?")
        title = next((v["title"] for v in videos if v["id"] == vid), vid)
        lines.append(f"{i}. {title[:70]} — {int(row.get('views', 0)):,} views (30d)")
    lines.append("")
    lines.append("## Traffic sources (30d)")
    for row in traffic.get("results", [])[:8]:
        lines.append(f"- {row.get('insightTrafficSourceType')}: {int(row.get('views', 0)):,} views")
    lines.append("")
    lines.append("## Recent uploads (lifetime views)")
    for v in videos[:10]:
        lines.append(f"- {v['title'][:70]} — {v['views']:,} views")
    lines.append("")
    recent_comment_count = sum(len(c.get("comments", [])) for c in comments)
    lines.append(f"## Comments pulled: {recent_comment_count} across {len(comments)} recent videos")
    return "\n".join(lines) + "\n"


def main() -> int:
    setup_env()
    from youtube_mcp.auth import YouTubeAuth

    out_dir = OUTPUT_ROOT / f"export-{date.today().isoformat()}"
    out_dir.mkdir(parents=True, exist_ok=True)

    auth = YouTubeAuth(config_dir=CONFIG, client_secret_path=CONFIG / "client_secret.json")
    youtube = auth.build_youtube_service()
    analytics = auth.build_youtube_analytics_service()

    print(f"Output: {out_dir}")
    print("Pulling channel...")
    channel = get_channel(youtube)
    save(out_dir, "channel", channel)

    print(f"Pulling {channel['video_count']} videos (paginated)...")
    video_ids = list_all_video_ids(youtube, channel["uploads_playlist_id"])
    videos = get_videos(youtube, video_ids)
    save(out_dir, "videos", {"total": len(videos), "videos": videos})

    print("Pulling analytics (30d + 90d)...")
    overview_30 = run_analytics(
        analytics,
        "views,estimatedMinutesWatched,averageViewDuration,subscribersGained,subscribersLost,likes,comments,shares",
        days=30,
    )
    save(out_dir, "analytics-overview-30d", overview_30)

    overview_90 = run_analytics(
        analytics,
        "views,estimatedMinutesWatched,averageViewDuration,subscribersGained,subscribersLost,likes,comments,shares",
        days=90,
    )
    save(out_dir, "analytics-overview-90d", overview_90)

    daily_90 = run_analytics(
        analytics,
        "views,estimatedMinutesWatched,averageViewDuration,subscribersGained,likes,shares",
        dimensions="day",
        days=90,
        sort="day",
    )
    save(out_dir, "analytics-daily-90d", daily_90)
    save(
        out_dir,
        "analytics-day-of-week-90d",
        {"results": day_of_week_aggregate(daily_90["results"]), **{k: daily_90[k] for k in ("start_date", "end_date")}},
    )

    top_videos = run_analytics(
        analytics,
        "views,estimatedMinutesWatched,averageViewDuration,likes,comments,shares",
        dimensions="video",
        days=30,
        filters="creatorContentType==video_on_demand",
        sort="-views",
        maxResults=50,
    )
    save(out_dir, "analytics-top-videos-30d", top_videos)

    top_shorts = run_analytics(
        analytics,
        "views,estimatedMinutesWatched,averageViewDuration,likes,comments,shares",
        dimensions="video",
        days=30,
        filters="creatorContentType==shorts",
        sort="-views",
        maxResults=50,
    )
    save(out_dir, "analytics-top-shorts-30d", top_shorts)

    traffic = run_analytics(
        analytics,
        "views,estimatedMinutesWatched",
        dimensions="insightTrafficSourceType",
        days=30,
        sort="-views",
    )
    save(out_dir, "analytics-traffic-sources-30d", traffic)

    demographics = run_analytics(
        analytics, "viewerPercentage", dimensions="ageGroup,gender", days=90, sort="-viewerPercentage"
    )
    save(out_dir, "analytics-demographics-90d", demographics)

    geography = run_analytics(
        analytics,
        "views,estimatedMinutesWatched",
        dimensions="country",
        days=90,
        sort="-views",
        maxResults=25,
    )
    save(out_dir, "analytics-geography-90d", geography)

    print("Pulling playlists...")
    playlists = list_playlists(youtube, channel["id"])
    save(out_dir, "playlists", {"total": len(playlists), "playlists": playlists})

    print("Pulling comments from 15 most recent videos...")
    recent_ids = [v["id"] for v in videos[:15]]
    comments = pull_comments(youtube, recent_ids, max_per_video=50)
    save(out_dir, "comments-recent-15-videos", {"videos": comments})

    try:
        revenue = run_analytics(
            analytics,
            "estimatedRevenue,estimatedAdRevenue,grossRevenue,estimatedRedPartnerRevenue",
            days=30,
        )
    except Exception as exc:
        revenue = {"error": str(exc)}
    save(out_dir, "analytics-revenue-30d", revenue)

    summary = build_summary(channel, videos, overview_30, top_videos, traffic, comments)
    (out_dir / "SUMMARY.md").write_text(summary)

    print("\n" + "=" * 60)
    print(summary)
    print("=" * 60)
    print(f"\nDone. {len(list(out_dir.glob('*.json')))} JSON files + SUMMARY.md")
    print(f"Folder: {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
