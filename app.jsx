const { useState, useEffect, useRef } = React;

function PhaseTabBox({ phase }) {
  const [activeTab, setActiveTab] = useState(0);
  const section = phase.sections[activeTab];
  return (
    <div className="tabbox">
      <div className="tabbox__tabs" role="tablist">
        {phase.sections.map((s, i) => (
          <button key={i} role="tab" aria-selected={i === activeTab}
            className={`tabbox__tab ${i === activeTab ? 'active' : ''}`}
            onClick={() => setActiveTab(i)}>
            <span className="tabbox__tab-num">{s.n}</span>
            <span className="tabbox__tab-title">{s.title}</span>
          </button>
        ))}
      </div>
      <div className="tabbox__panel" role="tabpanel">
        <div className="tabbox__panel-content" key={activeTab}>
          <div className="tabbox__panel-num">Module {section.n}</div>
          <h3 className="tabbox__panel-title">{section.title}</h3>
          <ul className="tabbox__items">
            {section.items.map((item, ii) => (
              <li key={ii} className="tabbox__item">
                <span className="tabbox__item-marker">{String(ii + 1).padStart(2, '0')}</span>
                <span>{item}</span>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}

function App() {
  const [dockVisible, setDockVisible] = useState(false);
  const [theme, setTheme] = useState(() => {
    if (typeof window === 'undefined') return 'dark';
    const stored = localStorage.getItem('roadmap-theme');
    if (stored) return stored;
    if (document.documentElement.dataset.theme) return document.documentElement.dataset.theme;
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) return 'light';
    return 'dark';
  });
  const toggleTheme = () => setTheme(t => (t === 'light' ? 'dark' : 'light'));
  const phaseRefs = useRef([]);
  const capstoneRefs = useRef([]);
  const agendaRef = useRef(null);
  const dockNodeRefs = useRef([]);
  const progressFillRef = useRef(null);
  const progressDotRef = useRef(null);
  const scrollFrame = useRef(null);
  const lastActiveIdx = useRef(-1);
  const lastDockVisible = useRef(false);
  const phaseMetrics = useRef([]);

  useEffect(() => {
    document.documentElement.dataset.theme = theme;
    localStorage.setItem('roadmap-theme', theme);
  }, [theme]);

  useEffect(() => {
    const recomputeMetrics = () => {
      phaseMetrics.current = phaseRefs.current.filter(Boolean).map(el => {
        const pt = parseFloat(window.getComputedStyle(el).paddingTop) || 0;
        return { el, paddingTop: pt };
      });
    };

    const update = () => {
      scrollFrame.current = null;
      const scrollTop = window.scrollY;
      const winH = window.innerHeight;
      const metrics = phaseMetrics.current;
      if (!metrics.length) return;

      const firstPhaseTop = metrics[0].el.getBoundingClientRect().top + scrollTop;
      const visible = scrollTop > firstPhaseTop - winH * 0.15;
      if (visible !== lastDockVisible.current) {
        lastDockVisible.current = visible;
        setDockVisible(visible);
      }

      const navOffset = window.innerWidth <= 700 ? 24 : 56;
      const firstTop = metrics[0].el.getBoundingClientRect().top + scrollTop + metrics[0].paddingTop - navOffset;
      const lastM = metrics[metrics.length - 1];
      const lastTop = lastM.el.getBoundingClientRect().top + scrollTop + lastM.paddingTop - navOffset;
      const phaseRange = lastTop - firstTop;
      const phaseProgress = phaseRange <= 0 ? 0 : (scrollTop - firstTop) / phaseRange;
      const pct = Math.min(1, Math.max(0, phaseProgress)) * 100;
      if (progressFillRef.current) progressFillRef.current.style.width = pct + '%';
      if (progressDotRef.current) progressDotRef.current.style.left = pct + '%';

      const probeLine = window.innerWidth <= 700 ? 96 : 160;
      let active = 0;
      for (let i = 0; i < metrics.length; i++) {
        const rect = metrics[i].el.getBoundingClientRect();
        if (rect.top + metrics[i].paddingTop <= probeLine) active = i;
      }
      if (active !== lastActiveIdx.current) {
        const prev = lastActiveIdx.current;
        lastActiveIdx.current = active;
        dockNodeRefs.current.forEach((node, i) => {
          if (!node) return;
          node.classList.toggle('active', i === active);
          node.classList.toggle('passed', i < active);
        });
      }
    };

    const onScroll = () => {
      if (scrollFrame.current != null) return;
      scrollFrame.current = window.requestAnimationFrame(update);
    };

    const onResize = () => {
      recomputeMetrics();
      onScroll();
    };

    recomputeMetrics();
    update();
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onResize);
    return () => {
      window.removeEventListener('scroll', onScroll);
      window.removeEventListener('resize', onResize);
      if (scrollFrame.current != null) window.cancelAnimationFrame(scrollFrame.current);
    };
  }, []);

  useEffect(() => {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('in-view'); });
    }, { threshold: 0.15, rootMargin: '0px 0px -10% 0px' });
    document.querySelectorAll('.reveal').forEach(el => io.observe(el));
    return () => io.disconnect();
  }, []);

  const scrollToElement = (el, mobileOffset = 24, desktopOffset = 72, includePadding = false) => {
    if (!el) return;
    const navOffset = window.innerWidth <= 700 ? mobileOffset : desktopOffset;
    const pt = includePadding
      ? parseFloat(window.getComputedStyle(el).paddingTop) || 0
      : 0;
    const top = el.getBoundingClientRect().top + window.scrollY + pt - navOffset;
    const prefersReduced = window.matchMedia
      && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const isMobile = window.innerWidth <= 700;
    window.scrollTo({
      top: Math.max(0, top),
      behavior: prefersReduced || isMobile ? 'auto' : 'smooth'
    });
  };

  const scrollToPhase = (i) => {
    const el = phaseRefs.current[i];
    if (!el) return;
    scrollToElement(el, 24, 56, true);
  };
  const scrollToCapstone = (i) => scrollToElement(capstoneRefs.current[i], 24, 72, false);
  const scrollToAgenda = () => scrollToElement(agendaRef.current, 24, 72, false);

  const totalSections = window.ROADMAP.reduce((a, p) => a + p.sections.length, 0);

  const capstoneTiles = window.CAPSTONES.map((c, i) => ({
    n: c.n,
    title: c.title.split(/[—:]|on /)[0].trim(),
    domain: c.domain,
    color: ['pink', 'mustard', 'teal-deep'][i]
  }));

  return (
    <React.Fragment>
      <nav className="nav">
        <div className="nav__brand">
          <span className="nav__brand-mark">A</span>
          <span><b>Agent Engineer</b> · 2026 Roadmap</span>
        </div>
        <div className="nav__right">
          <div className="nav__meta">
            <span><b>26</b> weeks</span>
            <span><b>9</b> phases</span>
            <span><b>3</b> capstones</span>
          </div>
          <button
            className="theme-toggle"
            onClick={toggleTheme}
            aria-label="Toggle theme">
            <span className="theme-toggle__track">
              <span className="theme-toggle__thumb">
                {theme === 'light' ? '☀' : '☾'}
              </span>
            </span>
          </button>
        </div>
      </nav>

      {/* HERO */}
      <header className="hero" data-screen-label="01 Hero">
        <div className="hero__blob" />
        <div className="hero__blob-2" />
        <div className="hero__blob-3" />
        <div className="hero__eyebrow">
          <span className="hero__eyebrow-dot" />
          The 2026 Edition · 26 Weeks · 9 Phases
        </div>
        <h1 className="hero__title">
          The only roadmap<br />
          you need to become a<br />
          <span className="hero__title-100x">100× AI Engineer</span> <em>in 2026.</em>
        </h1>
        <p className="hero__sub">
          A complete, production-grade journey from <em>script kid to agent engineer</em>.
          Every module grounded in real enterprise AI engineering — from Python fundamentals
          all the way to multi-agent systems shipping in regulated domains.
        </p>
        <div className="hero__actions">
          <button className="hero__cta" type="button" onClick={scrollToAgenda}>
            Explore the roadmap
            <span aria-hidden="true">↓</span>
          </button>
        </div>
        <div className="hero__stats">
          <div>
            <div className="hero__stat-num">{window.ROADMAP.length}</div>
            <div className="hero__stat-label">Phases</div>
          </div>
          <div>
            <div className="hero__stat-num">{totalSections}</div>
            <div className="hero__stat-label">Modules</div>
          </div>
          <div>
            <div className="hero__stat-num">26</div>
            <div className="hero__stat-label">Weeks</div>
          </div>
          <div>
            <div className="hero__stat-num">{window.CAPSTONES.length}</div>
            <div className="hero__stat-label">Capstones</div>
          </div>
        </div>
      </header>

      {/* AGENDA — 9 phase tiles */}
      <section className="agenda reveal" ref={agendaRef} data-screen-label="02 Agenda">
        <div className="agenda__head">
          <h2 className="agenda__title">What we'll <em>cover.</em></h2>
          <div className="agenda__sub">
            A complete production-grade journey. Every module grounded in real enterprise AI engineering.
          </div>
        </div>
        <div className="agenda__grid agenda__grid--phases">
          {window.ROADMAP.map((p) => (
            <button key={p.id}
              type="button"
              className="agenda__tile"
              data-color={p.color}
              aria-label={`Jump to phase ${String(p.id).padStart(2, '0')}: ${p.title}`}
              onClick={() => scrollToPhase(p.id - 1)}>
              <div className="agenda__tile-glow" />
              <div className="agenda__tile-num">{String(p.id).padStart(2, '0')}</div>
              <div className="agenda__tile-title">{p.short}</div>
              <div className="agenda__tile-weeks">{p.weeks}</div>
              <div className="agenda__tile-arrow">→</div>
            </button>
          ))}
        </div>

        {/* Projects in their own row */}
        <div className="agenda__projects-head">
          <span className="agenda__projects-label">◆ Capstone Projects</span>
          <span className="agenda__projects-line" />
        </div>
        <div className="agenda__grid agenda__grid--projects">
          {capstoneTiles.map((c) => (
            <button key={`cap-${c.n}`}
              type="button"
              className="agenda__tile is-capstone"
              data-color={c.color}
              aria-label={`Jump to capstone project ${c.n}: ${c.title}`}
              onClick={() => scrollToCapstone(c.n - 1)}>
              <div className="agenda__tile-glow" />
              <div className="agenda__tile-cap-label">Project {c.n}</div>
              <div className="agenda__tile-title">{c.title}</div>
              <div className="agenda__tile-domain">{c.domain}</div>
              <div className="agenda__tile-arrow">→</div>
            </button>
          ))}
        </div>
      </section>

      {/* INSTRUCTOR */}
      <section className="instructor reveal" data-screen-label="03 Instructor">
        <div className="instructor__card">
          <div className="instructor__photo">
            <img src="uploads/balaji-chippada.png" alt="Balaji Chippada" />
          </div>
          <div className="instructor__body">
            <div className="instructor__label">Your Instructor</div>
            <h3 className="instructor__name">Balaji Chippada</h3>
            <div className="instructor__role">AI/ML practitioner · Production-scale agentic AI builder</div>
            <p className="instructor__bio">
              I have spent <span>8 years in the AI/ML industry</span> and watched the field move from traditional
              machine learning into agentic AI. Along the way, I have built <span>production-scale agentic
              applications</span> and seen what actually matters when these systems leave the demo stage.
              I am also a tutor in the AI and data science space, and over the last couple of years
              I have mentored and taught <span>3,000+ students and working professionals</span> transform their careers.
              If I had to start all over again in 2026, this is exactly how I would begin. This roadmap
              is the curriculum I wish someone had handed me on day one.
            </p>
            <div className="instructor__chips">
              <span className="instructor__chip">8 Years AI/ML</span>
              <span className="instructor__chip">LangGraph</span>
              <span className="instructor__chip">Agentic AI</span>
              <span className="instructor__chip">Production RAG</span>
              <span className="instructor__chip">Multi-Agent Systems</span>
              <span className="instructor__chip">LLMOps</span>
            </div>
          </div>
          <div className="instructor__cta">
            <div className="instructor__connect-label">Connect with me</div>
            <div className="instructor__socials">
              <a className="instructor__social" href="https://www.linkedin.com/in/balaji-chippada-0317/" target="_blank" rel="noopener noreferrer" aria-label="Connect with Balaji Chippada on LinkedIn">
                <svg viewBox="0 0 24 24" aria-hidden="true">
                  <path d="M6.7 9.2H3.2v11.3h3.5V9.2ZM4.9 3.5C3.8 3.5 3 4.3 3 5.4s.8 1.9 1.9 1.9 1.9-.8 1.9-1.9-.8-1.9-1.9-1.9Zm15.6 10.6c0-3.3-1.8-5.2-4.4-5.2-1.8 0-2.8 1-3.2 1.7V9.2H9.5v11.3H13v-6.1c0-1.6.8-2.5 2-2.5s1.9.8 1.9 2.5v6.1h3.6v-6.4Z" />
                </svg>
              </a>
              <a className="instructor__social" href="https://www.youtube.com/@balajichippada" target="_blank" rel="noopener noreferrer" aria-label="Open Balaji Chippada on YouTube">
                <svg viewBox="0 0 24 24" aria-hidden="true">
                  <path d="M21.6 7.2a3 3 0 0 0-2.1-2.1C17.7 4.6 12 4.6 12 4.6s-5.7 0-7.5.5a3 3 0 0 0-2.1 2.1C2 9 2 12 2 12s0 3 .4 4.8a3 3 0 0 0 2.1 2.1c1.8.5 7.5.5 7.5.5s5.7 0 7.5-.5a3 3 0 0 0 2.1-2.1C22 15 22 12 22 12s0-3-.4-4.8ZM10 15.5v-7l6 3.5-6 3.5Z" />
                </svg>
              </a>
              <a className="instructor__social" href="https://www.instagram.com/inside.datascience/" target="_blank" rel="noopener noreferrer" aria-label="Open Inside Data Science on Instagram">
                <svg viewBox="0 0 24 24" aria-hidden="true">
                  <path d="M7.5 2.8h9A4.7 4.7 0 0 1 21.2 7.5v9a4.7 4.7 0 0 1-4.7 4.7h-9a4.7 4.7 0 0 1-4.7-4.7v-9a4.7 4.7 0 0 1 4.7-4.7Zm0 2A2.7 2.7 0 0 0 4.8 7.5v9a2.7 2.7 0 0 0 2.7 2.7h9a2.7 2.7 0 0 0 2.7-2.7v-9a2.7 2.7 0 0 0-2.7-2.7h-9Zm4.5 3.1a4.1 4.1 0 1 1 0 8.2 4.1 4.1 0 0 1 0-8.2Zm0 2a2.1 2.1 0 1 0 0 4.2 2.1 2.1 0 0 0 0-4.2Zm4.4-2.4a1 1 0 1 1 0 2 1 1 0 0 1 0-2Z" />
                </svg>
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* DOCK */}
      <div className={`dock ${dockVisible ? 'visible' : ''}`}>
        {window.ROADMAP.map((p, i) => (
          <button key={p.id}
            type="button"
            aria-label={`Jump to phase ${String(p.id).padStart(2, '0')}: ${p.title}`}
            ref={el => dockNodeRefs.current[i] = el}
            className="dock__node"
            data-color={p.color}
            onClick={() => scrollToPhase(i)}>
            {String(p.id).padStart(2, '0')}
            <span className="dock__node-tooltip">{p.short}</span>
          </button>
        ))}
        <div className="dock__progress">
          <div className="dock__progress-fill" ref={progressFillRef} />
          <div className="dock__progress-dot" ref={progressDotRef} />
        </div>
      </div>

      {/* PHASES */}
      <section className="phases">
        {window.ROADMAP.map((phase, i) => (
          <article key={phase.id} className="phase"
            ref={el => phaseRefs.current[i] = el}
            data-screen-label={`${String(phase.id).padStart(2, '0')} ${phase.title}`}>
            <div className="phase__index">
              <span className="phase__num-prefix" data-color={phase.color}>Phase {String(phase.id).padStart(2, '0')}</span>
              <span className="phase__num">{String(phase.id).padStart(2, '0')}</span>
              <div className="phase__num-bar" data-color={phase.color} />
              <div className="phase__weeks-block" data-color={phase.color}>
                <div className="phase__weeks-label">Time frame</div>
                <div className="phase__weeks">{phase.weeks}</div>
                <div className="phase__weeks-detail">{phase.weeksDetail}</div>
                <div className="phase__diff">
                  <span>Difficulty</span>
                  <span className="phase__diff-score">{phase.difficulty}/5</span>
                  <span className="phase__diff-dots" aria-label={`Difficulty ${phase.difficulty} out of 5`}>
                    {[1,2,3,4,5].map(d => (
                      <span key={d} className={`phase__diff-dot ${d <= phase.difficulty ? 'on' : ''}`} />
                    ))}
                  </span>
                </div>
              </div>
              {phase.capstone && (
                <div className="phase__capstone-pill">Capstone {phase.capstone}</div>
              )}
            </div>
            <div className="phase__body">
              <h2 className="phase__title">
                <span className="phase__title-accent" data-color={phase.color} />
                {phase.title}
              </h2>
              <p className="phase__summary">{phase.summary}</p>
              <PhaseTabBox phase={phase} />
              <div className="phase__endstate reveal">
                <div className="phase__endstate-label">End state</div>
                <div className="phase__endstate-text">{phase.endState}</div>
              </div>
            </div>
          </article>
        ))}
      </section>

      {/* CAPSTONES */}
      <section className="capstones reveal" data-screen-label="Capstones">
        <div className="capstones__eyebrow">Three Capstone Projects</div>
        <h2 className="capstones__title">Theory bound to <em>production reality.</em></h2>
        <p className="capstones__intro">
          Each capstone lands at the end of a phase cluster. They aren't toys — they're the proof
          that the curriculum stuck.
        </p>
        <div className="capstone-grid">
          {window.CAPSTONES.map((c, i) => (
            <article key={c.n}
              className="capstone"
              ref={el => capstoneRefs.current[i] = el}>
              <div className="capstone__left">
                <div className="capstone__num">CAPSTONE {String(c.n).padStart(2, '0')}</div>
                <div className="capstone__title">{c.title}</div>
                <div className="capstone__phase">{c.phase}</div>
                <div className="capstone__domain">{c.domain}</div>
                <div className="capstone__stack">
                  {c.stack.map((s, i) => (
                    <span key={i} className="capstone__stack-pill">{s}</span>
                  ))}
                </div>
              </div>
              <div className="capstone__build">
                <div className="capstone__build-label">What you build</div>
                {c.build.map((b, i) => (
                  <div key={i} className="capstone__build-item">
                    <span className="capstone__build-num">{String(i + 1).padStart(2, '0')}</span>
                    <span>{b}</span>
                  </div>
                ))}
                <div className="capstone__proves">
                  <span className="capstone__proves-label">Proves</span>
                  {c.proves}
                </div>
              </div>
            </article>
          ))}
        </div>
      </section>

      <footer className="footer reveal">
        <h2 className="footer__title">
          The journey ends where the <em>real work</em> begins.
        </h2>
        <div className="footer__meta">26 weeks · 9 phases · 3 capstones · one engineer</div>
      </footer>
    </React.Fragment>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
