# V__ — Python OOP Part 3: Classmethods & Staticmethods

---

## Video Metadata

| Field | Value |
|---|---|
| Video # | V0__ |
| Slug | `oop-03-classmethods-staticmethods` |
| Playlist | Phase 1 — Python Foundations / OOP Series |
| Target length | 18–20 min |
| Slot | Mon / Wed / Fri 7 PM IST |
| Previous video | V0__ — Class Variables vs Instance Variables |
| Next video | V0__ — Inheritance & super() |

## Roadmap Mapping

```
- Phase: 1 — Python Foundations
- Sections covered: 1.2 (Object-Oriented Python — instance vs class methods)
- Prerequisites needed: OOP Part 1 + 2
- Capstone contribution: No
```

## Visual / Production Plan

| Segment | Medium |
|---|---|
| 0:00–0:30 Hook | Mac screen — show `AgentResult.failure()` call, ask "how does this work?" |
| 0:30–2:00 Bridge | Face-cam |
| 2:00–7:00 Regular methods vs classmethods | Mac screen — VS Code |
| 7:00–12:00 Classmethods as alternative constructors | Mac screen — `from_string()`, `from_dict()` |
| 12:00–15:00 Staticmethods | Mac screen — utility functions that belong to the class |
| 15:00–17:00 Bridge to real project | Mac screen — `AgentResult.failure()`, `SeniorityLevel.from_string()` |
| 17:00–19:00 Common Mistakes + Recap | Sketchbook |
| 19:00–20:00 Cliffhanger | Face-cam |

---

## HOOK (0:00 – 0:30)

**On screen**: Show this code from the real project:

```python
return AgentResult.failure("JD Extractor", PipelineStep.JD_EXTRACTION, "Input was empty")
```

**Spoken**:

> See this? `AgentResult.failure()`. We're not calling it on an instance — we're calling it on the *class itself*. And it returns a new `AgentResult` object. How? This isn't a regular method. It's a classmethod — an alternative constructor. Today I'll show you what that means, when to use it, and how it's different from a staticmethod.

---

## CONTEXT BRIDGE (0:30 – 2:00)

**Spoken**:

> Last video — class variables vs instance variables. We saw that class-level data is shared. Now the natural question: can we have class-level *methods* too? Methods that work with the class itself, not with a specific instance?
>
> Three types of methods in Python: regular methods (take `self`), classmethods (take `cls`), and staticmethods (take neither). Each has a specific job. Let's see all three.

---

## THE SOLUTION — Concept Teaching (2:00 – 15:00)

### Concept 1: Regular Methods vs Classmethods (2:00 – 7:00)

```python
class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    # Regular method — works with the INSTANCE (self)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Classmethod — works with the CLASS (cls)
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
```

> Regular methods take `self` — they operate on a specific instance. Classmethods take `cls` — they operate on the class itself.
>
> `set_raise_amount` changes the raise for *all* employees, not just one:

```python
Employee.set_raise_amount(1.05)
print(Employee.raise_amount)  # 1.05 — changed for everyone
```

> You can also call it on an instance — `emp1.set_raise_amount(1.06)` — but `cls` still refers to the class, not the instance. The class gets modified either way.

### Concept 2: Classmethods as Alternative Constructors (7:00 – 12:00)

> The most powerful use of classmethods — alternative constructors. Sometimes you want to create an object from different input formats.

```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @classmethod
    def from_string(cls, emp_str):
        """Create an Employee from a dash-separated string."""
        first, last, pay = emp_str.split("-")
        return cls(first, last, int(pay))

    @classmethod
    def from_dict(cls, data: dict):
        """Create an Employee from a dictionary."""
        return cls(data["first"], data["last"], data["pay"])
```

> `cls` here is the class itself. `return cls(...)` is the same as `return Employee(...)` — but using `cls` means it works correctly with inheritance too. If a subclass calls `from_string`, `cls` will be the subclass, not `Employee`.

```python
emp = Employee.from_string("Ravi-Kumar-50000")
print(emp.first)  # Ravi

emp2 = Employee.from_dict({"first": "Priya", "last": "Sharma", "pay": 60000})
print(emp2.full_name())  # Priya Sharma
```

> Real-world examples: `datetime.fromtimestamp()`, `dict.fromkeys()`, `int.from_bytes()` — all classmethods acting as alternative constructors.

### Concept 3: Staticmethods (12:00 – 15:00)

> A staticmethod doesn't take `self` or `cls`. It's just a regular function that logically belongs to the class but doesn't need access to instance or class data.

```python
class Employee:
    ...

    @staticmethod
    def is_workday(day):
        """Check if a day is a workday (Mon-Fri)."""
        # day.weekday(): 0=Mon, 6=Sun
        return day.weekday() < 5
```

```python
import datetime
my_date = datetime.date(2026, 5, 11)  # Monday
print(Employee.is_workday(my_date))  # True
```

> If your method doesn't use `self` or `cls` anywhere in its body, it should probably be a staticmethod. It's a signal to other developers: "this function is related to the class conceptually, but it doesn't depend on any instance or class state."
>
> Rule of thumb:
> - Needs instance data? → Regular method (`self`)
> - Needs to modify or create from the class? → Classmethod (`cls`)
> - Needs neither? → Staticmethod

---

## BRIDGE TO REAL PROJECT (15:00 – 17:00)

**Spoken**:

> Back to the resume agent. Remember the hook?

```python
# From models.py — AgentResult
@classmethod
def failure(cls, agent_name: str, step: PipelineStep, error: str) -> "AgentResult":
    return cls(
        agent_name=agent_name,
        step=step,
        data=None,
        success=False,
        error=error,
    )
```

> `AgentResult.failure(...)` — a classmethod as an alternative constructor. Instead of writing `AgentResult(success=False, error=..., data=None, ...)` every time something fails, you call `AgentResult.failure("agent name", step, "what went wrong")`. Cleaner. Semantic. Self-documenting.
>
> And from the same project:

```python
# From models.py — SeniorityLevel
@classmethod
def from_string(cls, value: str) -> "SeniorityLevel":
    """Fuzzy match a string to a seniority level."""
    value_lower = value.lower().strip()
    for member in cls:
        if member.value.lower() in value_lower:
            return member
    return cls.UNKNOWN
```

> Another alternative constructor — takes a messy string from an LLM response and maps it to a clean enum value. Classmethod. Same pattern.

---

## COMMON MISTAKES (17:00 – 19:00)

| # | Mistake | Why Wrong | Fix |
|---|---|---|---|
| 1 | Using `@classmethod` when you need instance data | `cls` doesn't have access to `self.first`, `self.pay`, etc. | If you need instance data, use a regular method |
| 2 | Using `@staticmethod` when you actually need `cls` | Can't create instances or access class variables | If you're returning `cls(...)`, you need `@classmethod` |
| 3 | Forgetting `@classmethod` decorator | Method gets `self` instead of `cls` — breaks when called on class | Always add the decorator |

**Cheat sheet**:

```
THREE TYPES OF METHODS
1. Regular method: def method(self) — needs instance data
2. @classmethod: def method(cls) — needs class, alternative constructors
3. @staticmethod: def method() — needs neither, utility function

WHEN TO USE CLASSMETHOD:
- Alternative constructors (from_string, from_dict, from_json)
- Factory methods (failure(), create_default())
- Modifying class-level state

WHEN TO USE STATICMETHOD:
- Utility functions logically grouped with the class
- No self or cls needed anywhere in the body
```

---

## CLIFFHANGER (19:00 – 20:00)

**Spoken**:

> Three types of methods. Three types of variables. You now have the full vocabulary of a single class.
>
> But here's the thing — in the resume agent, there isn't just one class. There's `BaseAgent`, and then `JDExtractorAgent`, `ResumeMatcherAgent`, `CriticAgent` — six agents, all inheriting from the same base.
>
> Inheritance. The mechanism that lets you write shared logic once and reuse it everywhere. Next video — inheritance, the `super()` function, and why the resume agent has a base class at all.

---

## YouTube Description

```
Three types of methods in Python classes — and when to use each one. Plus: alternative constructors, the pattern used in datetime, dict, and real AI agent code.

In this video:
• Regular methods (self) — instance-level behavior
• @classmethod (cls) — alternative constructors & class-level operations
• @staticmethod — utility functions grouped with the class
• Real examples: AgentResult.failure(), SeniorityLevel.from_string()
• When to use which — the decision framework

🗺️ Where this fits in the Roadmap:
Phase 1 — Python Foundations
Section: 1.2 (Object-Oriented Python)
Previous: Class Variables vs Instance Variables
Next: Inheritance & super()

📂 Code:
GitHub: https://github.com/balajichippada/roadmap-2026-oop-03

⏱️ Timestamps:
0:00 — What is AgentResult.failure()?
0:30 — Three types of methods
2:00 — Regular methods vs classmethods
7:00 — Alternative constructors (the killer use case)
12:00 — Staticmethods
15:00 — Real project examples
17:00 — Common mistakes
19:00 — Recap + what's next

#Python #OOP #Classmethod #Staticmethod #Roadmap2026
```
