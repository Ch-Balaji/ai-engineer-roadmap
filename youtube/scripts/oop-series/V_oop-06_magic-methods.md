# V__ — Python OOP Part 6: Magic Methods & Operator Overloading

---

## Video Metadata

| Field | Value |
|---|---|
| Video # | V0__ |
| Slug | `oop-06-magic-methods` |
| Playlist | Phase 1 — Python Foundations / OOP Series |
| Target length | 20–22 min |
| Slot | Mon / Wed / Fri 7 PM IST |
| Previous video | V0__ — Abstract Classes & Polymorphism |
| Next video | (Next section — Dataclasses / Pydantic, or Phase 1.3 Data Structures) |

## Roadmap Mapping

```
- Phase: 1 — Python Foundations
- Sections covered: 1.2 (Object-Oriented Python — completes the section)
- Prerequisites needed: OOP Parts 1–5
- Capstone contribution: No (but completes OOP foundation for all later phases)
```

## Visual / Production Plan

| Segment | Medium |
|---|---|
| 0:00–0:30 Hook | Mac screen — `if result:` and `for step in pipeline:` working on custom objects |
| 0:30–2:00 Bridge | Face-cam |
| 2:00–6:00 __repr__ and __str__ | Mac screen — debugging vs display |
| 6:00–10:00 __len__, __bool__, __contains__ | Mac screen — making objects work with len(), if, in |
| 10:00–14:00 __iter__ and __getitem__ | Mac screen — making objects iterable |
| 14:00–16:00 __add__, __eq__ and arithmetic | Mac screen — operator overloading |
| 16:00–18:30 Bridge to real project | Mac screen — all magic methods from models.py |
| 18:30–20:00 Common Mistakes | Sketchbook |
| 20:00–22:00 Series Recap + What's Next | Sketchbook + face-cam |

---

## HOOK (0:00 – 0:30)

**On screen**: Terminal running this code:

```python
result = pipeline.run(resume_text=resume, jd_text=jd)

if result:                    # How does 'if' work on a custom object?
    print(result)             # How does print() know what to show?
    print(len(pipeline))      # How does len() work on a Pipeline?

for step in pipeline:         # How does 'for' work on a Pipeline?
    print(step)
```

**Spoken**:

> `if`, `print`, `len`, `for` — these all work on built-in types like lists and strings. But here they're working on *our* custom objects. `Pipeline` isn't a list. `AgentResult` isn't a boolean. Yet Python treats them like they are.
>
> Magic methods. The double-underscore methods that let your objects plug into Python's built-in syntax. By the end of this video, your objects will feel like they belong in the standard library.

---

## CONTEXT BRIDGE (0:30 – 2:00)

**Spoken**:

> We've built classes, used inheritance, defined abstract contracts. But our objects still feel like second-class citizens. You can't `print()` them nicely. You can't check `if agent_result:` to see if it succeeded. You can't loop over pipeline results with `for`.
>
> Magic methods — also called dunder methods (double underscore) — are the hooks Python calls behind the scenes. When you write `len(x)`, Python actually calls `x.__len__()`. When you write `if x:`, Python calls `x.__bool__()`. Define these methods, and your objects integrate seamlessly with the language.

---

## THE SOLUTION — Concept Teaching (2:00 – 16:00)

### Concept 1: __repr__ and __str__ (2:00 – 6:00)

```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def __repr__(self):
        """For developers — unambiguous, ideally copy-pasteable."""
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        """For end users — readable, friendly."""
        return f"{self.first} {self.last} — ₹{self.pay:,}"
```

```python
emp = Employee("Ravi", "Kumar", 50000)

repr(emp)   # "Employee('Ravi', 'Kumar', 50000)"
str(emp)    # "Ravi Kumar — ₹50,000"
print(emp)  # "Ravi Kumar — ₹50,000" — print() uses __str__

# In the REPL or debugger:
emp         # Employee('Ravi', 'Kumar', 50000) — uses __repr__
```

> Rule: `__repr__` is for developers (debugging, logging). `__str__` is for users (display). If you only define one, define `__repr__` — Python falls back to it when `__str__` is missing.
>
> Without these? You get `<__main__.Employee object at 0x7f...>`. Useless.

### Concept 2: __len__, __bool__, __contains__ (6:00 – 10:00)

```python
class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add(self, employee):
        self.members.append(employee)

    def __len__(self):
        """len(team) returns number of members."""
        return len(self.members)

    def __bool__(self):
        """A team is 'truthy' if it has members."""
        return len(self.members) > 0

    def __contains__(self, employee):
        """Support 'in' operator: if emp in team."""
        return employee in self.members
```

```python
team = Team("AI Platform")
print(len(team))       # 0
print(bool(team))      # False — empty team

team.add(emp)
print(len(team))       # 1
print(bool(team))      # True — has members

if team:               # Uses __bool__
    print("Team exists!")

if emp in team:        # Uses __contains__
    print("Ravi is on the team")
```

> `__bool__` is especially powerful. It lets you write `if result:` instead of `if result.success == True:`. Cleaner. More Pythonic.

### Concept 3: __iter__ and __getitem__ (10:00 – 14:00)

```python
class Team:
    ...

    def __iter__(self):
        """Make Team iterable — support 'for member in team'."""
        return iter(self.members)

    def __getitem__(self, index):
        """Support indexing: team[0], team[1], team[-1]."""
        return self.members[index]
```

```python
team = Team("AI Platform")
team.add(Employee("Ravi", "Kumar", 50000))
team.add(Employee("Priya", "Sharma", 60000))

# for loop works:
for member in team:
    print(member)

# Indexing works:
print(team[0])   # Ravi Kumar — ₹50,000
print(team[-1])  # Priya Sharma — ₹60,000

# Slicing works (if __getitem__ handles slices):
print(team[0:1])
```

> `__iter__` makes your object work with `for` loops, `list()`, unpacking (`a, b = team`). `__getitem__` adds indexing and slicing. Together, your object behaves like a collection.

### Concept 4: Arithmetic — __add__, __eq__ (14:00 – 16:00)

```python
class Employee:
    ...

    def __add__(self, other):
        """emp1 + emp2 returns combined salary."""
        return self.pay + other.pay

    def __eq__(self, other):
        """Two employees are equal if same email."""
        if not isinstance(other, Employee):
            return NotImplemented
        return self.email == other.email
```

```python
emp1 = Employee("Ravi", "Kumar", 50000)
emp2 = Employee("Priya", "Sharma", 60000)

print(emp1 + emp2)    # 110000 — combined salary
print(emp1 == emp2)   # False — different emails
```

> You can overload `+`, `-`, `*`, `<`, `>`, `==` — any operator. But be careful: only do it when the operation makes intuitive sense. `emp1 + emp2` returning combined salary is debatable. `vector1 + vector2` returning a new vector? That's natural.

---

## BRIDGE TO REAL PROJECT (16:00 – 18:30)

**Spoken**:

> The resume agent uses magic methods everywhere. Let me show you the real code.

```python
# models.py — AgentResult
@dataclass
class AgentResult:
    agent_name: str
    step: PipelineStep
    data: Any
    success: bool = True
    ...

    def __str__(self) -> str:
        status = "✓" if self.success else "✗"
        return f"{status} [{self.agent_name}] Step {self.step.value}: ..."

    def __bool__(self) -> bool:
        """Result is truthy if successful."""
        return self.success

    def __repr__(self) -> str:
        return f"AgentResult(agent={self.agent_name!r}, success={self.success})"
```

> `if result:` — checks `__bool__`, which returns `self.success`. Clean.
> `print(result)` — calls `__str__`, shows `✓ [JD Extractor] Step 0: OK`.

```python
# models.py — PipelineState
@dataclass
class PipelineState:
    results: list[AgentResult] = field(default_factory=list)
    ...

    def __len__(self) -> int:
        return len(self.results)

    def __iter__(self):
        return iter(self.results)
```

> `len(pipeline)` — number of completed steps.
> `for step in pipeline:` — iterates over results.

```python
# models.py — MatchAnalysis
class MatchAnalysis(BaseModel):
    match_score: int = Field(default=0, ge=0, le=100)
    ...

    def __bool__(self) -> bool:
        """A match analysis is 'truthy' if score > 0."""
        return self.match_score > 0
```

> `if match:` — truthy only if there's a real score. No need to check `.match_score > 0` explicitly.
>
> See the pattern? Magic methods make the code that *uses* these objects read like English.

---

## COMMON MISTAKES (18:30 – 20:00)

| # | Mistake | Why Wrong | Fix |
|---|---|---|---|
| 1 | Defining `__str__` but not `__repr__` | Debugger/REPL shows useless `<object at 0x...>` | Always define `__repr__`. `__str__` is optional. |
| 2 | `__eq__` without `__hash__` | Objects become unhashable — can't use in sets or as dict keys | If you define `__eq__`, also define `__hash__` (or set `__hash__ = None` if mutable) |
| 3 | Overloading operators that don't make semantic sense | `emp1 + emp2` is confusing — what does "adding employees" mean? | Only overload when the operation is intuitive for the domain |
| 4 | Forgetting `return NotImplemented` in comparison methods | Python can't try the reverse operation | Return `NotImplemented` (not `NotImplementedError`) for unsupported types |

---

## SERIES RECAP + WHAT'S NEXT (20:00 – 22:00)

**Sketchbook — full series cheat sheet**:

```
PYTHON OOP — THE COMPLETE PICTURE

Part 1: Classes & Instances
  → class, __init__, self, instance variables, methods

Part 2: Class Variables vs Instance Variables
  → shared vs unique data, namespace lookup, __dict__

Part 3: Classmethods & Staticmethods
  → @classmethod (alternative constructors), @staticmethod (utilities)

Part 4: Inheritance & super()
  → subclassing, super().__init__(), method overriding, MRO

Part 5: Abstract Classes & Polymorphism
  → ABC, @abstractmethod, Template Method, same interface different behavior

Part 6: Magic Methods
  → __str__, __repr__, __len__, __bool__, __iter__, __add__, __eq__

TOGETHER: These 6 concepts built the entire resume agent pipeline.
```

**Closing**:

> Six videos. Six concepts. And now you can read every line of the resume agent's OOP architecture. `BaseAgent` with its abstract methods. `Pipeline` composing agents. `AgentResult` with its magic methods. `PipelineState` that's iterable.
>
> This is section 1.2 complete. Next up in the roadmap — Dataclasses and Pydantic models. You've already seen them in the project (`@dataclass`, `BaseModel`). Next video, we'll understand exactly what they give you on top of regular classes — and why every agent framework uses Pydantic for tool schemas.
>
> See you then.

---

## YouTube Description

```
Make your Python objects work with print(), len(), if, for, and operators — like they're built-in types. The final piece of OOP that makes code read like English.

In this video:
• __repr__ and __str__ — debugging vs display
• __len__, __bool__, __contains__ — len(), if, in
• __iter__ and __getitem__ — for loops and indexing
• __add__, __eq__ — operator overloading
• Every magic method used in the real AI agent project
• Full series recap — 6 OOP concepts that built the pipeline

🗺️ Where this fits in the Roadmap:
Phase 1 — Python Foundations
Section: 1.2 (Object-Oriented Python — series finale)
Previous: Abstract Classes & Polymorphism
Next: Dataclasses & Pydantic Models

📂 Code:
GitHub: https://github.com/balajichippada/roadmap-2026-oop-06

⏱️ Timestamps:
0:00 — if result: — how does that work?
0:30 — What are magic methods?
2:00 — __repr__ and __str__
6:00 — __len__, __bool__, __contains__
10:00 — __iter__ and __getitem__
14:00 — __add__ and __eq__
16:00 — Real project: all magic methods in action
18:30 — Common mistakes
20:00 — Full series recap + what's next

#Python #OOP #MagicMethods #DunderMethods #Roadmap2026
```
