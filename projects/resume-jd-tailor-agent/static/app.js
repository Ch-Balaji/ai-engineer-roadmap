/**
 * Resume JD Tailor Agent — Frontend Logic
 *
 * Handles the SSE connection to the FastAPI backend,
 * updates the pipeline progress, and renders results.
 */

// ── State ───────────────────────────────────────────────────
let allResults = {};

// ── Helpers ─────────────────────────────────────────────────

function scoreColor(score, max) {
  const pct = score / max;
  if (pct >= 0.8) return 'c-green';
  if (pct >= 0.5) return 'c-orange';
  return 'c-red';
}

function barColor(score, max) {
  const pct = score / max;
  if (pct >= 0.8) return '#16a34a';
  if (pct >= 0.5) return '#ea580c';
  return '#dc2626';
}

function tags(items, cls) {
  return items.map(i => `<span class="tag ${cls}">${esc(i)}</span>`).join(' ');
}

function esc(s) {
  const d = document.createElement('div');
  d.textContent = s;
  return d.innerHTML;
}

function show(id) { document.getElementById(id).style.display = ''; }
function hide(id) { document.getElementById(id).style.display = 'none'; }

// Map step numbers to the result card that will appear next
const STEP_TO_LOADER_TARGET = {
  0: 'jdCard',
  1: 'matchCard',
  2: 'bulletsCard',
  3: 'coverCard',
  4: 'criticCard',
  5: 'criticCard',   // revision updates critic
  6: 'interviewCard',
};

const STEP_LABELS = [
  'Analyzing Job Description',
  'Matching Resume to JD',
  'Rewriting Resume Bullets',
  'Drafting Cover Letter',
  'Running Critic Review',
  'Revising based on feedback',
  'Generating Interview Questions',
];

/** Insert a loading indicator just before the target card */
function showSectionLoader(step, label) {
  // Remove any existing section loader
  removeSectionLoader();

  const targetId = STEP_TO_LOADER_TARGET[step];
  if (!targetId) return;

  const loader = document.createElement('div');
  loader.id = 'currentSectionLoader';
  loader.className = 'section-loader fade-in';
  loader.innerHTML = `
    <div class="loader-dots">
      <div class="dot"></div><div class="dot"></div><div class="dot"></div>
    </div>
    <span class="loader-text">${esc(label)}</span>
  `;

  // Insert after the last visible result card, or at the start of results
  const resultsSection = document.getElementById('resultsSection');
  const targetCard = document.getElementById(targetId);
  if (targetCard) {
    targetCard.parentNode.insertBefore(loader, targetCard);
  } else {
    resultsSection.appendChild(loader);
  }
}

function removeSectionLoader() {
  const existing = document.getElementById('currentSectionLoader');
  if (existing) existing.remove();
}

// ── Pipeline Progress ───────────────────────────────────────

function updatePipelineStep(step, label) {
  const items = document.querySelectorAll('.step-item');
  items.forEach((el, i) => {
    el.classList.remove('active', 'done');
    if (i < step) el.classList.add('done');
    else if (i === step) el.classList.add('active');
  });

  // Progress bar with travelling dot
  const bar = document.getElementById('pipelineBar');
  const pct = Math.min(((step + 0.5) / 7) * 100, 97);
  bar.style.width = pct + '%';
  bar.classList.add('running');
  bar.classList.remove('done');

  document.getElementById('stepStatus').innerHTML =
    `<span class="spinner"></span> ${esc(label)}`;

  // Show section loader below results
  show('resultsSection');
  showSectionLoader(step, label);
}

function markAllDone() {
  document.querySelectorAll('.step-item').forEach(el => {
    el.classList.remove('active');
    el.classList.add('done');
  });
  const bar = document.getElementById('pipelineBar');
  bar.style.width = '100%';
  bar.classList.remove('running');
  bar.classList.add('done');

  document.getElementById('stepStatus').innerHTML = '✅ Pipeline complete!';
  document.getElementById('stepStatus').style.color = '#16a34a';

  removeSectionLoader();
}

// ── Run Agent ───────────────────────────────────────────────

async function runAgent() {
  const resume = document.getElementById('resume').value.trim();
  const jd = document.getElementById('jd').value.trim();
  const role = document.getElementById('role').value.trim();
  const errEl = document.getElementById('errorMsg');

  // Validate
  if (!resume) { errEl.textContent = '⚠️ Please paste your resume text.'; show('errorMsg'); return; }
  if (!jd) { errEl.textContent = '⚠️ Please paste the job description.'; show('errorMsg'); return; }
  hide('errorMsg');

  // Reset UI
  allResults = {};
  const btn = document.getElementById('runBtn');
  btn.disabled = true;
  btn.innerHTML = '<span class="spinner"></span> Running Pipeline...';
  show('pipelineSection');
  hide('resultsSection');
  document.getElementById('metricsRow').innerHTML = '';
  document.getElementById('stepStatus').style.color = '#6366f1';

  // Reset step items
  document.querySelectorAll('.step-item').forEach(el => el.classList.remove('active', 'done'));
  document.getElementById('pipelineBar').style.width = '0%';
  document.getElementById('pipelineBar').classList.remove('running', 'done');

  // Hide all result cards
  ['jdCard','matchCard','bulletsCard','coverCard','criticCard','interviewCard','downloadRow'].forEach(hide);
  removeSectionLoader();

  try {
    const resp = await fetch('/api/run', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ resume, jd, role }),
    });

    const reader = resp.body.getReader();
    const decoder = new TextDecoder();
    let buffer = '';

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      buffer += decoder.decode(value, { stream: true });
      const lines = buffer.split('\n');
      buffer = lines.pop(); // keep incomplete line

      for (const line of lines) {
        if (!line.startsWith('data: ')) continue;
        const msg = JSON.parse(line.slice(6));
        handleSSE(msg);
      }
    }
  } catch (e) {
    document.getElementById('stepStatus').innerHTML = `❌ Error: ${esc(e.message)}`;
    document.getElementById('stepStatus').style.color = '#dc2626';
  }

  btn.disabled = false;
  btn.innerHTML = '<span class="btn-icon">🚀</span> Run Agent Pipeline';
}

// ── SSE Handler ─────────────────────────────────────────────

function handleSSE(msg) {
  if (msg.type === 'step') {
    updatePipelineStep(msg.step, msg.label);
  }
  else if (msg.type === 'result') {
    // Store results
    if (msg.key === 'revision') {
      allResults.bullets = msg.data.bullets;
      allResults.cover_letter = msg.data.cover_letter;
      allResults.critic = msg.data.critic;
      allResults.revision_count = msg.data.revision_count;
    } else {
      allResults[msg.key] = msg.data;
    }
    // Render incrementally
    renderResult(msg.key, msg.data);
  }
  else if (msg.type === 'done') {
    markAllDone();
    renderMetrics();
    show('downloadRow');
  }
  else if (msg.type === 'error') {
    document.getElementById('stepStatus').innerHTML = `❌ ${esc(msg.message)}`;
    document.getElementById('stepStatus').style.color = '#dc2626';
  }
}

// ── Render Functions ────────────────────────────────────────

function renderResult(key, data) {
  show('resultsSection');
  removeSectionLoader();

  if (key === 'jd_analysis') renderJD(data);
  else if (key === 'match_analysis') renderMatch(data);
  else if (key === 'bullets') renderBullets(data);
  else if (key === 'cover_letter') renderCover(data);
  else if (key === 'critic') renderCritic(data);
  else if (key === 'revision') {
    renderBullets(data.bullets);
    renderCover(data.cover_letter);
    renderCritic(data.critic, data.revision_count);
  }
  else if (key === 'interview_questions') renderInterview(data);
}

function renderJD(d) {
  const card = document.getElementById('jdCard');
  card.style.display = '';
  card.classList.add('fade-in');

  document.getElementById('jdContent').innerHTML = `
    <div class="card-grid">
      <div>
        <div class="tags-row">
          <div class="tags-label">Seniority Level</div>
          <span class="tag tag-purple">${esc(d.seniority_level || 'N/A')}</span>
        </div>
        <div class="tags-row">
          <div class="tags-label">Top Keywords</div>
          ${tags(d.top_keywords || [], 'tag-blue')}
        </div>
        <div class="tags-row">
          <div class="tags-label">Tools & Technologies</div>
          ${tags(d.tools_technologies || [], 'tag-purple')}
        </div>
      </div>
      <div>
        <div class="tags-row">
          <div class="tags-label">Must-Have Skills</div>
          ${tags(d.must_have_skills || [], 'tag-green')}
        </div>
        <div class="tags-row">
          <div class="tags-label">Nice-to-Have Skills</div>
          ${tags(d.nice_to_have_skills || [], 'tag-yellow')}
        </div>
      </div>
    </div>
    ${(d.responsibilities && d.responsibilities.length) ? `
      <div style="margin-top:1rem;">
        <div class="tags-label">Key Responsibilities</div>
        <ul style="margin:0.4rem 0 0 1.2rem; font-size:0.88rem; color:#475569;">
          ${d.responsibilities.map(r => `<li>${esc(r)}</li>`).join('')}
        </ul>
      </div>
    ` : ''}
  `;
}

function renderMatch(d) {
  const card = document.getElementById('matchCard');
  card.style.display = '';
  card.classList.add('fade-in');

  const score = d.match_score || 0;
  const color = barColor(score, 100);

  document.getElementById('matchContent').innerHTML = `
    <div style="text-align:center; margin-bottom:1rem;">
      <span class="${scoreColor(score, 100)}" style="font-size:2.5rem; font-weight:800;">${score}</span>
      <span style="font-size:1.2rem; color:#94a3b8;">/100</span>
    </div>
    <div class="score-bar-bg">
      <div class="score-bar" style="width:${score}%; background:${color};"></div>
    </div>
    <p class="score-explanation">${esc(d.score_explanation || '')}</p>
    <div class="card-grid-3" style="margin-top:1.2rem;">
      <div>
        <div class="tags-label">✅ Matched Skills</div>
        ${tags(d.matched_skills || [], 'tag-green')}
      </div>
      <div>
        <div class="tags-label">⚠️ Weak Skills</div>
        ${tags(d.weak_skills || [], 'tag-yellow')}
      </div>
      <div>
        <div class="tags-label">❌ Missing Skills</div>
        ${tags(d.missing_skills || [], 'tag-red')}
        ${(d.missing_skills && d.missing_skills.length) ?
          '<p style="font-size:0.78rem; color:#94a3b8; margin-top:0.4rem;">Not added to rewritten bullets — learn these to strengthen your profile.</p>' : ''}
      </div>
    </div>
    ${(d.sections_to_improve && d.sections_to_improve.length) ? `
      <div style="margin-top:1rem;">
        <div class="tags-label">Sections to Improve</div>
        ${tags(d.sections_to_improve, 'tag-yellow')}
      </div>
    ` : ''}
  `;
}

function renderBullets(bullets) {
  const card = document.getElementById('bulletsCard');
  card.style.display = '';
  card.classList.add('fade-in');

  document.getElementById('bulletsContent').innerHTML = bullets.map((b, i) => `
    <div class="bullet-item">
      <div class="b-label">Bullet ${i + 1}</div>
      <div class="b-original">🔹 <strong>Original:</strong> ${esc(b.original || 'N/A')}</div>
      <div class="b-rewritten">🔸 <strong>Rewritten:</strong> ${esc(b.rewritten || 'N/A')}</div>
      <div class="b-changes">💡 ${esc(b.changes_made || '')}</div>
    </div>
  `).join('');
}

function renderCover(text) {
  const card = document.getElementById('coverCard');
  card.style.display = '';
  card.classList.add('fade-in');

  document.getElementById('coverContent').innerHTML =
    `<div class="cover-letter-box">${esc(text)}</div>`;
}

function renderCritic(d, revisionCount) {
  const card = document.getElementById('criticCard');
  card.style.display = '';
  card.classList.add('fade-in');

  const score = d.score || 0;
  const rc = revisionCount !== undefined ? revisionCount : (allResults.revision_count || 0);

  document.getElementById('criticContent').innerHTML = `
    ${rc > 0 ? `<div class="revision-badge">🔄 Revised ${rc} time(s)</div>` :
      (score >= 8 ? '<div class="revision-badge" style="background:#dcfce7;color:#166534;">✅ Passed on first attempt</div>' : '')}
    <div style="text-align:center; margin-bottom:1rem;">
      <span class="${scoreColor(score, 10)}" style="font-size:2.5rem; font-weight:800;">${score}</span>
      <span style="font-size:1.2rem; color:#94a3b8;">/10</span>
    </div>
    <div class="critic-grid">
      <div>
        <div class="tags-label">Issues Found</div>
        <ul class="critic-list">
          ${(d.issues || []).map(i => `<li>${esc(i)}</li>`).join('')}
          ${(!d.issues || !d.issues.length) ? '<li style="color:#94a3b8;">None</li>' : ''}
        </ul>
      </div>
      <div>
        <div class="tags-label">Suggestions</div>
        <ul class="critic-list">
          ${(d.suggestions || []).map(s => `<li>${esc(s)}</li>`).join('')}
          ${(!d.suggestions || !d.suggestions.length) ? '<li style="color:#94a3b8;">None</li>' : ''}
        </ul>
      </div>
    </div>
  `;
}

function renderInterview(questions) {
  const card = document.getElementById('interviewCard');
  card.style.display = '';
  card.classList.add('fade-in');

  document.getElementById('interviewContent').innerHTML = questions.map((q, i) => `
    <div class="q-card">
      <div class="q-num">Question ${i + 1}</div>
      <div class="q-text">${esc(q.question || '')}</div>
      <div class="q-meta">📎 <em>Why asked:</em> ${esc(q.why_asked || '')}</div>
      <div class="q-hint">💡 <em>Prep hint:</em> ${esc(q.preparation_hint || '')}</div>
    </div>
  `).join('');
}

function renderMetrics() {
  const match = allResults.match_analysis || {};
  const critic = allResults.critic || {};
  const matchScore = match.match_score || 0;
  const criticScore = critic.score || 0;
  const matched = (match.matched_skills || []).length;
  const missing = (match.missing_skills || []).length;
  const revisions = allResults.revision_count || 0;

  document.getElementById('metricsRow').innerHTML = `
    <div class="metric-card fade-in">
      <div class="m-label">Match Score</div>
      <div class="m-value ${scoreColor(matchScore, 100)}">${matchScore}/100</div>
    </div>
    <div class="metric-card fade-in">
      <div class="m-label">Quality Score</div>
      <div class="m-value ${scoreColor(criticScore, 10)}">${criticScore}/10</div>
    </div>
    <div class="metric-card fade-in">
      <div class="m-label">Skills Matched</div>
      <div class="m-value c-green">${matched}</div>
    </div>
    <div class="metric-card fade-in">
      <div class="m-label">Skills Missing</div>
      <div class="m-value ${missing > 3 ? 'c-red' : missing > 0 ? 'c-orange' : 'c-green'}">${missing}</div>
    </div>
    <div class="metric-card fade-in">
      <div class="m-label">Revisions</div>
      <div class="m-value">${revisions}</div>
    </div>
  `;
}

// ── Download Report ─────────────────────────────────────────

function downloadReport(ext) {
  const r = allResults;
  const jd = r.jd_analysis || {};
  const match = r.match_analysis || {};
  const critic = r.critic || {};

  let lines = ['# Resume JD Tailor Agent — Report\n'];

  lines.push('## 1. JD Keyword Summary\n');
  lines.push(`**Seniority Level:** ${jd.seniority_level || 'N/A'}\n`);
  lines.push(`**Top Keywords:** ${(jd.top_keywords || []).join(', ')}\n`);
  lines.push(`**Must-Have:** ${(jd.must_have_skills || []).join(', ')}\n`);
  lines.push(`**Nice-to-Have:** ${(jd.nice_to_have_skills || []).join(', ')}\n`);

  lines.push('## 2. Resume Match Analysis\n');
  lines.push(`**Score:** ${match.match_score || 0}/100\n`);
  lines.push(`**Explanation:** ${match.score_explanation || ''}\n`);
  lines.push(`**Matched:** ${(match.matched_skills || []).join(', ')}\n`);

  lines.push('## 3. Missing Skills\n');
  (match.missing_skills || []).forEach(s => lines.push(`- ${s}`));
  lines.push('');

  lines.push('## 4. Rewritten Resume Bullets\n');
  (r.bullets || []).forEach(b => {
    lines.push(`**Original:** ${b.original || 'N/A'}`);
    lines.push(`**Rewritten:** ${b.rewritten || 'N/A'}`);
    lines.push(`*Changes:* ${b.changes_made || ''}\n`);
  });

  lines.push('## 5. Cover Letter\n');
  lines.push((r.cover_letter || '') + '\n');

  lines.push('## 6. Critic Review\n');
  lines.push(`**Score:** ${critic.score || 'N/A'}/10\n`);
  if (critic.issues) { lines.push('**Issues:**'); critic.issues.forEach(i => lines.push(`- ${i}`)); }
  if (critic.suggestions) { lines.push('\n**Suggestions:**'); critic.suggestions.forEach(s => lines.push(`- ${s}`)); }
  lines.push('');

  lines.push('## 7. Interview Questions\n');
  (r.interview_questions || []).forEach((q, i) => {
    lines.push(`### Q${i+1}: ${q.question || ''}`);
    lines.push(`**Why asked:** ${q.why_asked || ''}`);
    lines.push(`**Prep hint:** ${q.preparation_hint || ''}\n`);
  });

  const text = lines.join('\n');
  const blob = new Blob([text], { type: ext === 'md' ? 'text/markdown' : 'text/plain' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `resume_jd_tailor_report.${ext}`;
  a.click();
  URL.revokeObjectURL(url);
}
