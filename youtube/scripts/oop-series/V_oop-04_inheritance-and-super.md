# V__ — Python OOP Part 4: Inheritance & the super() Function

---

## Video Metadata

| Field | Value |
|---|---|
| Video # | V0__ |
| Slug | `oop-04-inheritance-and-super` |
| Playlist | Phase 1 — Python Foundations / OOP Series |
| Target length | 20–22 min |
| Slot | Mon / Wed / Fri 7 PM IST |
| Previous video | V0__ — Classmethods & Staticmethods |
| Next video | V0__ — Abstract Classes & Polymorphism |

## Roadmap Mapping

```
- Phase: 1 — Python Foundations
- Sections covered: 1.2 (Inheritance, encapsulation, polymorphism)
- Prerequisites needed: OOP Parts 1–3
- Capstone contribution: No
```

## Visual / Production Plan

| Segment | Medium |
|---|---|
| 0:00–0:30 Hook | Sketchbook — draw 6 agents, all with same execute() method |
| 0:30–2:00 Bridge | Face-cam |
| 2:00–7:00 Basic inheritance | Mac screen — Employee → Developer, Manager |
| 7:00–11:00 super() and __init__ | Mac screen — extending the constructor |
| 11:00–14:00 Method overriding | Mac screen — customizing behavior in subclasses |
| 14:00–17:00 isinstance, issubclass, MRO | Mac screen + sketchbook |
| 17:00–19:00 Bridge to real project | Mac screen — BaseAgent → JDExtractorAgent |
| 19:00–20:30 Common Mistakes | Sketchbook |
| 20:30–22:00 Recap + Cliffhanger | Sketchbook + face-cam |

---

## HOOK (0:00 – 0:30)

**On screen**: Sketchbook — quickly draw 6 boxes labeled "JD Extractor", "Resume Matcher", "Rewriter", "Cover Letter", "Critic", "Interview". Draw arrows from all 6 pointing to one box: "BaseAgent".

**Spoken**:

> Six agents. Each one does something completely different — one extracts keywords, one writes cover letters, one critiques the output. But they all share the same `execute()` method, the same error handling, the same timing logic. I didn't copy-paste that code six times. I wrote it once, in a base class, and all six agents *inherit* it.
>
> That's inheritance. The mechanism that eliminates duplication and enforces consistency. Let's build it from scratch.

---

## CONTEXT BRIDGE (0:30 – 2:00)

**Spoken**:

> So far we've built one class at a time. Employee with its own data and methods. But real projects don't have just one class — they have families of related classes. Managers are employees. Developers are employees. They share most behavior but differ in specifics.
>
> Inheritance lets you define shared behavior in a parent class and specialize in child classes. Write once, reuse everywhere, override where needed.

---

## THE SOLUTION — Concept Teaching (2:00 – 17:00)

### Concept 1: Basic Inheritance (2:00 – 7:00)

```python
class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@company.com"

    def full_name(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10  # Developers get 10% raises

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        self.employees = employees if employees is not None else []

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
```

> `Developer(Employee)` — that parenthesis is the inheritance syntax. Developer *is an* Employee. It gets everything Employee has — `full_name()`, `apply_raise()`, the email generation — for free.
>
> But it can also add its own attributes (`prog_lang`) and override class variables (`raise_amount = 1.10`).

```python
dev1 = Developer("Ravi", "Kumar", 50000, "Python")
print(dev1.full_name())    # Ravi Kumar — inherited from Employee
print(dev1.prog_lang)      # Python — Developer-specific
dev1.apply_raise()
print(dev1.pay)            # 55000 — uses Developer's raise_amount (1.10)
```

### Concept 2: super() and __init__ (7:00 – 11:00)

> `super().__init__(first, last, pay)` — this calls the parent class's `__init__`. Without it, the Developer wouldn't have `first`, `last`, `pay`, or `email`.

```python
# What happens WITHOUT super().__init__():
class BadDeveloper(Employee):
    def __init__(self, first, last, pay, prog_lang):
        # Forgot super().__init__()!
        self.prog_lang = prog_lang

dev = BadDeveloper("Ravi", "Kumar", 50000, "Python")
print(dev.prog_lang)    # Python — works
print(dev.first)        # AttributeError! — parent never set it
```

> `super()` gives you a reference to the parent class. `super().__init__()` runs the parent's constructor. Then you add your own stuff after.
>
> Think of it as: "Do everything the parent does, *then* do my extra stuff."

### Concept 3: Method Overriding (11:00 – 14:00)

> What if a subclass needs different behavior for an inherited method?

```python
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        self.employees = employees if employees is not None else []

    def full_name(self):
        """Override — managers get a title."""
        return f"Manager {self.first} {self.last}"
```

```python
mgr = Manager("Priya", "Sharma", 80000)
print(mgr.full_name())  # Manager Priya Sharma — overridden version
```

> The subclass's method takes priority. Python looks in the instance's class first, then walks up the inheritance chain. This is the Method Resolution Order (MRO).

### Concept 4: isinstance, issubclass, MRO (14:00 – 17:00)

```python
dev1 = Developer("Ravi", "Kumar", 50000, "Python")

print(isinstance(dev1, Developer))  # True
print(isinstance(dev1, Employee))   # True — Developer IS an Employee
print(isinstance(dev1, Manager))    # False

print(issubclass(Developer, Employee))  # True
print(issubclass(Manager, Employee))    # True
print(issubclass(Developer, Manager))   # False

# Method Resolution Order
print(Developer.__mro__)
# (<class 'Developer'>, <class 'Employee'>, <class 'object'>)
```

> MRO tells you the lookup order. When you call `dev1.apply_raise()`, Python checks Developer first, then Employee, then `object` (the ultimate base class of everything in Python).

---

## BRIDGE TO REAL PROJECT (17:00 – 19:00)

**Spoken**:

> Now — the resume agent. This is exactly what's happening.

```python
# base.py
class BaseAgent(ABC):
    def __init__(self, llm_client: LLMClient):
        self._llm_client = llm_client
        self._execution_count = 0
        self._total_time_ms = 0.0

    def execute(self, **kwargs) -> AgentResult:
        # validate → process → format → return
        ...
```

```python
# jd_extractor.py
class JDExtractorAgent(BaseAgent):
    def __init__(self, llm_client: LLMClient):
        super().__init__(llm_client)  # ← same pattern!
        # JDExtractor-specific setup if needed

    @property
    def name(self) -> str:
        return "JD Extractor"

    def _process(self, **kwargs) -> Any:
        # JDExtractor-specific LLM call
        ...
```

> Same pattern as Developer inheriting from Employee:
> - `super().__init__(llm_client)` — get the shared setup
> - Override specific methods (`_process`, `_validate_input`) — provide specialized behavior
> - Inherit shared methods (`execute()`) — get timing, logging, error handling for free
>
> Six agents. One base class. Zero duplicated infrastructure code.

---

## COMMON MISTAKES (19:00 – 20:30)

| # | Mistake | Why Wrong | Fix |
|---|---|---|---|
| 1 | Forgetting `super().__init__()` | Parent attributes never get set | Always call `super().__init__()` first in your `__init__` |
| 2 | Using mutable default arguments | `def __init__(self, employees=[])` — all instances share the same list | Use `None` as default, create list inside: `employees if employees is not None else []` |
| 3 | Overriding a method but forgetting to call super() | Loses parent behavior entirely | Call `super().method()` if you want parent behavior + your additions |

---

## RECAP + CLIFFHANGER (20:30 – 22:00)

**Cheat sheet**:

```
INHERITANCE
1. class Child(Parent): — Child inherits everything from Parent.
2. super().__init__() — call parent's constructor to get shared setup.
3. Override methods by redefining them in the child class.
4. MRO: Python looks in child first, then parent, then grandparent...
5. isinstance(obj, Class) — checks the full inheritance chain.
6. "Is-a" relationship: Developer IS an Employee.
```

**Cliffhanger**:

> Inheritance is powerful. But there's a problem — right now, nothing *forces* a subclass to implement specific methods. I could create a new agent that inherits from BaseAgent but forgets to define `_process()`. The code would break at runtime, not at definition time.
>
> What if we could make the base class say: "You MUST implement these methods, or Python won't even let you create an instance"?
>
> That's abstract classes. Next video — `ABC`, `@abstractmethod`, and the Template Method pattern that makes the entire resume agent pipeline work.

---

## YouTube Description

```
Write shared logic once, reuse it in every subclass. Inheritance is how real Python projects eliminate duplication — and how 6 AI agents share one execute() method.

In this video:
• Basic inheritance — child classes get parent behavior for free
• super().__init__() — extending the constructor without losing parent setup
• Method overriding — customizing inherited behavior
• MRO (Method Resolution Order) — how Python decides which method to call
• isinstance and issubclass — checking the inheritance chain
• Real example: BaseAgent → JDExtractorAgent in a production AI system

🗺️ Where this fits in the Roadmap:
Phase 1 — Python Foundations
Section: 1.2 (Inheritance, encapsulation, polymorphism)
Previous: Classmethods & Staticmethods
Next: Abstract Classes & Polymorphism

📂 Code:
GitHub: https://github.com/balajichippada/roadmap-2026-oop-04

⏱️ Timestamps:
0:00 — 6 agents, 1 base class
0:30 — Why inheritance exists
2:00 — Basic inheritance (Developer, Manager)
7:00 — super() and __init__
11:00 — Method overriding
14:00 — isinstance, issubclass, MRO
17:00 — Same pattern in the real project
19:00 — Common mistakes
20:30 — Recap + what's next

#Python #OOP #Inheritance #Roadmap2026 #PythonTutorial
```
