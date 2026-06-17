"""Async chatbot — Streamlit UI. Run with:

    streamlit run async_agent.py --server.port 8502
"""
from __future__ import annotations

import asyncio

import streamlit as st

from agent_core import run_async_agent

st.set_page_config(page_title="Async Agent", page_icon="⚡", layout="wide")

DEMO_PROMPT = (
    "Plan a 5-day trip across Hyderabad, Bangalore, Chennai, Mysore, and Pondicherry. "
    "I want weather and top attractions for each city."
)

st.markdown("# ⚡ Async Agent")
st.caption("Tools run **in parallel** with `asyncio.gather`. One change. Big speed-up.")

with st.sidebar:
    st.markdown("**Headline demo prompt** (paste into both apps):")
    st.code(DEMO_PROMPT, language=None)
    if st.button("Use demo prompt"):
        st.session_state.pending_prompt = DEMO_PROMPT

if "history" not in st.session_state:
    st.session_state.history = []

for role, content in st.session_state.history:
    with st.chat_message(role):
        st.markdown(content)

prompt = st.chat_input("Ask me to plan a trip across some cities…")
if st.session_state.get("pending_prompt"):
    prompt = st.session_state.pop("pending_prompt")

if prompt:
    st.session_state.history.append(("user", prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        status_placeholder = st.empty()
        log_placeholder = st.empty()

        def on_tools_start(labels: list[str]) -> None:
            lines = [f"⏳ {l}  (running…)" for l in labels]
            log_placeholder.markdown(
                "**All " + str(len(labels)) + " tools fired in parallel:**\n\n" + "\n".join(lines)
            )

        def on_tools_done(labels: list[str], parallel_elapsed: float) -> None:
            lines = [f"✅ {l}" for l in labels]
            log_placeholder.markdown(
                f"**All {len(labels)} tools finished in {parallel_elapsed:.2f}s "
                f"(parallel):**\n\n" + "\n".join(lines)
            )

        with status_placeholder.status("Working in parallel…", expanded=True):
            result = asyncio.run(
                run_async_agent(prompt, on_tools_start=on_tools_start, on_tools_done=on_tools_done)
            )

        status_placeholder.empty()
        st.markdown(result["answer"])
        st.session_state.history.append(("assistant", result["answer"]))

        n = result.get("tool_count", 0)
        tools_s = result.get("tools_elapsed", 0.0)
        llm_s = max(0.0, result["total_time"] - tools_s)
        st.markdown(
            f"**{n} tool calls** · tool phase **{tools_s:.2f}s** (parallel) · LLM ~**{llm_s:.2f}s**"
        )
        st.markdown(
            f"<div style='font-size:42px;font-weight:800;color:#16A34A;"
            f"padding:8px 0;'>⏱ Total: {result['total_time']:.2f}s</div>",
            unsafe_allow_html=True,
        )
        if n < 8:
            st.warning(
                "Few tool calls this run — async speedup looks small. Use the sidebar "
                "**5-city demo prompt** so the model fires ~10 tools (weather + attractions × 5 cities)."
            )
