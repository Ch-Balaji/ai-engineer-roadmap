# Resume JD Tailor Agent — v2 (OOP Refactor)

This is the **Object-Oriented Programming** refactored version of the Resume JD Tailor Agent.
Built as a teaching example for a Python OOP YouTube tutorial series.

## OOP Concepts Demonstrated

| Concept | Where to Find It |
|---------|-----------------|
| **Classes & Objects** | Every agent is a class instance |
| **Inheritance** | `BaseAgent` → `JDExtractorAgent`, `ResumeMatcherAgent`, etc. |
| **Abstract Base Classes** | `BaseAgent` with `@abstractmethod` |
| **Encapsulation** | Private methods (`_validate`, `_format_prompt`), properties |
| **Polymorphism** | All agents share `.execute()` interface but behave differently |
| **Composition** | `Pipeline` is composed of multiple `Agent` objects |
| **Dataclasses** | `AgentResult`, `PipelineConfig`, `LLMResponse` |
| **Custom Exceptions** | `LLMError`, `RateLimitError`, `ValidationError`, etc. |
| **Decorators** | `@retry`, `@rate_limit`, `@log_execution` |
| **Context Managers** | `LLMClient` as context manager (`with` statement) |
| **Properties** | Computed attributes with `@property` |
| **Class Methods** | Factory patterns (`Agent.from_config()`) |
| **Static Methods** | Utility functions that don't need instance state |
| **Magic/Dunder Methods** | `__repr__`, `__str__`, `__len__` on result objects |
| **Type Hints** | Full typing throughout |
| **SOLID Principles** | Single Responsibility, Open/Closed, etc. |

## Project Structure

```
v2_oop/
├── README.md
├── requirements.txt
├── .env.example
├── config.py              # Configuration with dataclasses
├── exceptions.py          # Custom exception hierarchy
├── decorators.py          # @retry, @rate_limit, @log_execution
├── models.py              # Pydantic/dataclass data models
├── llm_client.py          # LLMClient class (context manager)
├── prompts.py             # PromptTemplate class
├── agents/
│   ├── __init__.py
│   ├── base.py            # Abstract BaseAgent class
│   ├── jd_extractor.py    # JDExtractorAgent
│   ├── resume_matcher.py  # ResumeMatcherAgent
│   ├── resume_rewriter.py # ResumeRewriterAgent
│   ├── cover_letter.py    # CoverLetterAgent
│   ├── critic.py          # CriticAgent
│   └── interview.py       # InterviewAgent
├── pipeline.py            # Pipeline orchestrator (composition)
├── server.py              # FastAPI server
└── static/                # (symlink or copy from v1)
```

## Running

```bash
cd projects/resume-jd-tailor-agent/v2_oop
pip install -r requirements.txt
uvicorn server:app --reload --port 8502
```

## Key Differences from v1 (POC)

| v1 (POC) | v2 (OOP) |
|-----------|----------|
| Plain functions | Class-based agents |
| No error handling | Custom exception hierarchy + try/except |
| No rate limiting | Exponential backoff decorator |
| Global LLM client | `LLMClient` class with context manager |
| Dict results | Typed dataclass/Pydantic models |
| Prompts as strings | `PromptTemplate` class with validation |
| No logging | `@log_execution` decorator |
| No retry logic | `@retry` with configurable backoff |
