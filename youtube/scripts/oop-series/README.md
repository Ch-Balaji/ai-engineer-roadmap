# OOP in Python — Video Series Plan

**Roadmap Phase**: 1 — Python Foundations  
**Section**: 1.2 — Object-Oriented Python  
**Total Videos**: 6  
**Hook**: The `resume_jd_tailor_agent/v2_oop/` codebase — show the finished product first, then teach the concepts that make it work.

---

## Series Overview

| # | Video | Core Concepts | Code From Project |
|---|---|---|---|
| 1 | Classes & Instances | `class`, `__init__`, instance variables, methods | `BaseAgent.__init__`, `Pipeline.__init__` |
| 2 | Class Variables & Instance Variables | shared vs per-instance data, `__dict__` | `PipelineStep` enum, `_execution_count` |
| 3 | Classmethods & Staticmethods | `@classmethod`, `@staticmethod`, alternative constructors | `AgentResult.failure()`, `SeniorityLevel.from_string()` |
| 4 | Inheritance & the `super()` Function | subclassing, `super().__init__()`, method overriding | `BaseAgent` → `JDExtractorAgent`, `ResumeMatcherAgent` |
| 5 | Abstract Classes & Polymorphism | `ABC`, `@abstractmethod`, Template Method pattern | `BaseAgent` abstract methods, `Pipeline` treating all agents uniformly |
| 6 | Magic Methods & Operator Overloading | `__str__`, `__repr__`, `__len__`, `__bool__`, `__iter__` | `AgentResult`, `PipelineState`, `MatchAnalysis` |

---

## The Hook Strategy (applies to Video 1 opener, referenced in all others)

Open Video 1 by screen-sharing the `resume_jd_tailor_agent` running live:
- Paste a resume + JD → watch the pipeline run through 7 agents
- Show the terminal output: `✓ [JD Extractor] Step 0: OK (1200ms)`
- Then show `pipeline.py` — 6 agent objects composed together
- Then show `base.py` — one abstract class, all agents inherit from it

**The line**: "This entire system — 6 agents, a pipeline, a critic loop — runs on about 5 OOP concepts. By the end of this series, you'll be able to build this yourself. Today we start with the first one: classes."

---

## Shared Rules

- All code examples start simple (Employee class) then bridge to the real project code
- Every video ends with "here's where this shows up in the resume agent" — screen-share the actual file
- English technical terms: `class`, `instance`, `constructor`, `inheritance`, `polymorphism`, `abstract`, `method`, `attribute` — never translated
- Telugu delivery, English code and jargon
- Each video is self-contained but references the series arc
