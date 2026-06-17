# V__ — Python OOP Part 5: Abstract Classes & Polymorphism

---

## Video Metadata

| Field | Value |
|---|---|
| Video # | V0__ |
| Slug | `oop-05-abstract-classes-polymorphism` |
| Playlist | Phase 1 — Python Foundations / OOP Series |
| Target length | 20–22 min |
| Slot | Mon / Wed / Fri 7 PM IST |
| Previous video | V0__ — Inheritance & super() |
| Next video | V0__ — Magic Methods & Operator Overloading |

## Roadmap Mapping

```
- Phase: 1 — Python Foundations
- Sections covered: 1.2 (Inheritance, encapsulation, polymorphism)
- Prerequisites needed: OOP Parts 1–4
- Capstone contribution: No (but directly explains the agent architecture)
```

## Visual / Production Plan

| Segment | Medium |
|---|---|
| 0:00–0:30 Hook | Mac screen — try to instantiate BaseAgent, get TypeError |
| 0:30–2:00 Bridge | Face-cam + sketchbook |
| 2:00–6:00 ABC and @abstractmethod | Mac screen — building an abstract Shape class |
| 6:00–10:00 Template Method Pattern | Mac screen — the execute() skeleton |
| 10:00–14:00 Polymorphism | Mac screen — treating different objects the same way |
| 14:00–17:00 Bridge to real project | Mac screen — Pipeline iterating over agents |
| 17:00–19:00 Common Mistakes | Sketchbook |
| 19:00–20:00 Recap + Cliffhanger | Sketchbook + face-cam |

---

## HOOK (0:00 – 0:30)

**On screen**: Terminal — try to create a BaseAgent instance.

```python
from agents.base import BaseAgent
agent = BaseAgent(llm_client)
# TypeError: Can't instantiate abstract class BaseAgent
# with abstract methods _process, _validate_input, _format_output
```

**Spoken**:

> Python just refused to create this object. Not a bug — by design. `BaseAgent` is an abstract class. It's a contract that says: "You can't use me directly. You must create a subclass and implement these three methods first." If you forget even one, Python blocks you at creation time — not at runtime when your pipeline is halfway through processing a resume.
>
> This is the most powerful pattern in the entire agent codebase. Let me show you how it works.

---

## CONTEXT BRIDGE (0:30 – 2:00)

**Spoken**:

> Last video — inheritance. Subclasses get parent behavior for free. But we identified a gap: nothing *forces* a subclass to implement specific methods. You could create a broken agent that inherits from BaseAgent but never defines `_process()`, and you wouldn't know until runtime.
>
> Abstract classes fix that. They define a contract — "these methods MUST exist" — and Python enforces it at instantiation time. Combined with polymorphism — treating different objects through the same interface — this is what makes the pipeline work.

---

## THE SOLUTION — Concept Teaching (2:00 – 14:00)

### Concept 1: ABC and @abstractmethod (2:00 – 6:00)

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class — cannot be instantiated directly."""

    @abstractmethod
    def area(self):
        """Every shape MUST define how to calculate its area."""
        ...

    @abstractmethod
    def perimeter(self):
        """Every shape MUST define how to calculate its perimeter."""
        ...

    def description(self):
        """Concrete method — inherited by all shapes as-is."""
        return f"{self.__class__.__name__}: area={self.area():.2f}"
```

```python
# This FAILS:
shape = Shape()
# TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter

# This WORKS — all abstract methods implemented:
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

c = Circle(5)
print(c.area())         # 78.54
print(c.description())  # Circle: area=78.54 — inherited concrete method works!
```

> Two rules:
> 1. A class that inherits from `ABC` and has `@abstractmethod` methods cannot be instantiated.
> 2. A subclass MUST implement ALL abstract methods, or it's also abstract (can't be instantiated).
>
> The abstract class is a contract. "You want to be a Shape? Fine — but you MUST tell me your area and perimeter."

```python
# This ALSO fails — forgot perimeter:
class BadSquare(Shape):
    def area(self):
        return self.side ** 2
    # No perimeter defined!

sq = BadSquare()
# TypeError: Can't instantiate abstract class BadSquare with abstract method perimeter
```

> Caught at creation time. Not at runtime. Not in production. At the moment you try to create the object.

### Concept 2: Template Method Pattern (6:00 – 10:00)

> Here's where abstract classes get really powerful. The Template Method pattern.

```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    """Template Method: the algorithm skeleton is fixed, steps are customizable."""

    def process(self, raw_data):
        """The TEMPLATE — defines the algorithm structure.
        Subclasses DON'T override this. They override the steps."""
        validated = self._validate(raw_data)
        transformed = self._transform(validated)
        result = self._format(transformed)
        return result

    @abstractmethod
    def _validate(self, data):
        """Each processor defines its own validation."""
        ...

    @abstractmethod
    def _transform(self, data):
        """Each processor defines its own transformation."""
        ...

    @abstractmethod
    def _format(self, data):
        """Each processor defines its own output format."""
        ...
```

> The `process()` method is concrete — it defines the ORDER of operations. Validate, then transform, then format. Every subclass follows this order.
>
> But the *details* of each step? Abstract. Each subclass fills in its own logic.

```python
class CSVProcessor(DataProcessor):
    def _validate(self, data):
        if not data.strip():
            raise ValueError("Empty CSV")
        return data

    def _transform(self, data):
        rows = [line.split(",") for line in data.strip().split("\n")]
        return rows

    def _format(self, data):
        return {"rows": len(data), "data": data}


class JSONProcessor(DataProcessor):
    def _validate(self, data):
        import json
        return json.loads(data)  # Raises if invalid JSON

    def _transform(self, data):
        return {k: v for k, v in data.items() if v is not None}

    def _format(self, data):
        return {"fields": len(data), "data": data}
```

> Same `process()` method. Different behavior. The template stays fixed. The steps are pluggable.

### Concept 3: Polymorphism (10:00 – 14:00)

> Polymorphism means: treating different objects through the same interface.

```python
processors = [CSVProcessor(), JSONProcessor()]

for processor in processors:
    result = processor.process(some_data)
    # Don't care WHICH processor — they all have process()
```

> The calling code doesn't need to know whether it's a CSV processor or a JSON processor. It just calls `process()`. The right implementation runs automatically based on the object's type.
>
> This is the power: you can add a new processor (XMLProcessor, YAMLProcessor) without changing any of the code that *uses* processors. Open for extension, closed for modification.

```python
def run_all(processors: list[DataProcessor], data: str):
    """Works with ANY DataProcessor — present or future."""
    for p in processors:
        print(p.process(data))
```

> `run_all` doesn't know about CSVProcessor or JSONProcessor specifically. It knows about `DataProcessor` — the abstract interface. That's polymorphism.

---

## BRIDGE TO REAL PROJECT (14:00 – 17:00)

**Spoken**:

> This is exactly what the resume agent does. Let me show you.

```python
# base.py — the Template Method
class BaseAgent(ABC):
    def execute(self, **kwargs) -> AgentResult:
        """Template: validate → process → format. Always this order."""
        self._validate_input(**kwargs)      # Abstract — each agent defines
        raw_result = self._process(**kwargs) # Abstract — each agent defines
        formatted = self._format_output(raw_result)  # Abstract — each agent defines
        return AgentResult(...)

    @abstractmethod
    def _validate_input(self, **kwargs) -> None: ...

    @abstractmethod
    def _process(self, **kwargs) -> Any: ...

    @abstractmethod
    def _format_output(self, raw_result: Any) -> Any: ...
```

> Template Method. `execute()` is the skeleton — validate, process, format, wrap in AgentResult. Every agent follows this order. But each agent fills in the steps differently.

```python
# pipeline.py — Polymorphism in action
class Pipeline:
    def __init__(self, config):
        self._jd_extractor = JDExtractorAgent(self._llm_client)
        self._resume_matcher = ResumeMatcherAgent(self._llm_client)
        self._critic = CriticAgent(self._llm_client)
        # ... 6 agents total

    def _execute_pipeline(self, ...):
        # Each agent is called the same way:
        jd_result = self._jd_extractor.execute(jd_text=jd_text)
        match_result = self._resume_matcher.execute(resume_text=..., jd_text=...)
        # Same .execute() interface — polymorphism!
```

> The pipeline doesn't care about the internal differences between agents. It calls `.execute()` on each one. The right `_process()` runs based on which agent it is. That's polymorphism powered by abstract classes.

---

## COMMON MISTAKES (17:00 – 19:00)

| # | Mistake | Why Wrong | Fix |
|---|---|---|---|
| 1 | Forgetting to inherit from ABC | `@abstractmethod` has no effect without ABC — class can be instantiated | Always inherit from `ABC` (or use `metaclass=ABCMeta`) |
| 2 | Implementing abstract methods with wrong signature | Python doesn't check signatures — only that the method exists | Match the parent's signature. Use type hints to catch mismatches. |
| 3 | Making everything abstract | If every method is abstract, the base class provides no shared behavior | Keep concrete methods for shared logic (like `execute()`) |
| 4 | Overriding the template method | Defeats the purpose — the whole point is a fixed algorithm skeleton | Override the *steps*, not the template |

---

## RECAP + CLIFFHANGER (19:00 – 20:00)

**Cheat sheet**:

```
ABSTRACT CLASSES & POLYMORPHISM
1. ABC + @abstractmethod = contract. Subclass MUST implement or can't instantiate.
2. Template Method: concrete method defines order, abstract methods define steps.
3. Polymorphism: same interface, different behavior based on object type.
4. Calling code doesn't need to know the specific subclass — just the interface.
5. Add new subclasses without changing existing code.
6. Caught at creation time, not runtime.
```

**Cliffhanger**:

> We've seen `__init__`. We've seen `__repr__` in passing. But Python has dozens of these double-underscore methods — magic methods. `__str__`, `__len__`, `__bool__`, `__iter__`. They let your objects work with `print()`, `len()`, `if`, `for` loops — like built-in types.
>
> In the resume agent, `AgentResult` has `__bool__` so you can write `if result:`. `PipelineState` has `__iter__` so you can write `for step in pipeline:`. Next video — magic methods. Making your objects behave like Python natives.

---

## YouTube Description

```
The pattern that holds the entire AI agent pipeline together — abstract classes and the Template Method. Plus: polymorphism explained with real code, not animal examples.

In this video:
• ABC and @abstractmethod — enforcing contracts at creation time
• Template Method Pattern — fixed algorithm, pluggable steps
• Polymorphism — same interface, different behavior
• Why the pipeline can call .execute() on any agent without knowing its type
• Adding new agents without changing existing code

🗺️ Where this fits in the Roadmap:
Phase 1 — Python Foundations
Section: 1.2 (Inheritance, encapsulation, polymorphism)
Previous: Inheritance & super()
Next: Magic Methods & Operator Overloading

📂 Code:
GitHub: https://github.com/balajichippada/roadmap-2026-oop-05

⏱️ Timestamps:
0:00 — TypeError: Can't instantiate abstract class
0:30 — Why contracts matter
2:00 — ABC and @abstractmethod
6:00 — Template Method Pattern
10:00 — Polymorphism
14:00 — The real agent pipeline
17:00 — Common mistakes
19:00 — Recap + what's next

#Python #OOP #AbstractClass #Polymorphism #Roadmap2026
```
