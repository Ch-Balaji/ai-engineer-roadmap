# V__ — Python OOP Part 2: Class Variables vs Instance Variables

---

## Video Metadata

| Field | Value |
|---|---|
| Video # | V0__ |
| Slug | `oop-02-class-vs-instance-variables` |
| Playlist | Phase 1 — Python Foundations / OOP Series |
| Target length | 18–20 min |
| Slot | Mon / Wed / Fri 7 PM IST |
| Previous video | V0__ — Classes & Instances |
| Next video | V0__ — Classmethods & Staticmethods |

## Roadmap Mapping

```
- Phase: 1 — Python Foundations
- Sections covered: 1.2 (Object-Oriented Python — instance vs class methods)
- Prerequisites needed: OOP Part 1 (Classes & Instances)
- Capstone contribution: No
```

## Visual / Production Plan

| Segment | Medium |
|---|---|
| 0:00–0:30 Hook | Mac screen — show a bug caused by misusing class vs instance variable |
| 0:30–2:00 Bridge | Face-cam + sketchbook diagram |
| 2:00–6:00 Class variables explained | Mac screen — VS Code + terminal |
| 6:00–10:00 Instance vs class — the namespace trick | Mac screen — `__dict__` exploration |
| 10:00–14:00 When to use which | Mac screen — `raise_amount` vs `num_of_employees` |
| 14:00–16:00 Bridge to real project | Mac screen — show `PipelineStep` enum, `_execution_count` |
| 16:00–18:00 Common Mistakes | Sketchbook |
| 18:00–20:00 Recap + Cliffhanger | Sketchbook + face-cam |

---

## HOOK (0:00 – 0:30) — Pattern: Production Incident

**Spoken**:

> Watch this. I have two employees. I change the raise percentage for one of them. But somehow — the other one's raise also changed. Or did it? Let me run this again with a slight tweak... now only one changed.
>
> Same code, different behavior depending on one line. If you don't understand the difference between class variables and instance variables, this bug will find you in production. Today we fix that.

---

## CONTEXT BRIDGE (0:30 – 2:00)

**Spoken**:

> Last video we built our Employee class — `__init__`, instance variables, methods. Each employee carries its own data. That's instance-level.
>
> But what about data that's shared across *all* employees? A company-wide raise percentage. A counter of how many employees exist. That data doesn't belong to any one instance — it belongs to the class itself.
>
> That's what class variables are. And the interaction between class variables and instance variables is one of the most misunderstood things in Python OOP.

---

## THE SOLUTION — Concept Teaching (2:00 – 14:00)

### Concept 1: Class Variables (2:00 – 6:00)

```python
class Employee:
    # Class variable — shared by ALL instances
    raise_amount = 1.04  # 4% raise
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_employees += 1

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
```

> `raise_amount` lives on the class, not on any instance. Every employee sees the same value — unless you override it on a specific instance.
>
> `num_of_employees` — I'm using `Employee.num_of_employees` explicitly here, not `self`. Why? Because there's no scenario where one instance should have a different employee count. It's truly class-level.

### Concept 2: The Namespace Trick — `__dict__` (6:00 – 10:00)

```python
emp1 = Employee("Ravi", "Kumar", 50000)
emp2 = Employee("Priya", "Sharma", 60000)

print(emp1.__dict__)
# {'first': 'Ravi', 'last': 'Kumar', 'pay': 50000}
# Notice: no raise_amount here!

print(Employee.__dict__)
# {..., 'raise_amount': 1.04, 'num_of_employees': 2, ...}
```

> The instance doesn't *have* `raise_amount`. When you access `emp1.raise_amount`, Python looks in the instance first, doesn't find it, then looks in the class. That's the lookup chain.
>
> Now watch what happens when I assign it on the instance:

```python
emp1.raise_amount = 1.05

print(emp1.__dict__)
# {'first': 'Ravi', 'last': 'Kumar', 'pay': 50000, 'raise_amount': 1.05}
# NOW it's in the instance namespace!

print(emp1.raise_amount)       # 1.05 — from instance
print(emp2.raise_amount)       # 1.04 — still from class
print(Employee.raise_amount)   # 1.04 — class unchanged
```

> Assigning on the instance *creates* a new attribute on that instance. It doesn't modify the class variable. This is the source of the bug from the hook.

### Concept 3: `self.raise_amount` vs `Employee.raise_amount` (10:00 – 14:00)

> In `apply_raise`, I used `self.raise_amount`. Why not `Employee.raise_amount`?
>
> Using `self` gives flexibility — if a specific employee negotiated a different raise, you can override it per instance. Using the class name locks it to the class value for everyone.
>
> For `num_of_employees`, I used `Employee.num_of_employees` because there's no use case for one instance having a different count. It's always global.
>
> Rule of thumb: use `self.x` when subclasses or instances might need to override. Use `ClassName.x` when the value must be universal.

---

## BRIDGE TO REAL PROJECT (14:00 – 16:00)

**Spoken**:

> In the resume agent project, here's where this shows up.
>
> *[Open models.py]*

```python
class PipelineStep(int, Enum):
    JD_EXTRACTION = 0
    RESUME_MATCHING = 1
    BULLET_REWRITING = 2
    ...
```

> `PipelineStep` is essentially a class variable pattern — fixed values shared across all usage. No instance overrides this.
>
> *[Open base.py]*

```python
def __init__(self, llm_client: LLMClient):
    self._execution_count = 0      # Instance variable — each agent tracks its own
    self._total_time_ms = 0.0      # Instance variable — unique per agent
```

> `_execution_count` is instance-level. The JD Extractor might run 3 times, the Critic might run 5 times. Each tracks its own count. If this were a class variable, all agents would share one counter — completely wrong.

---

## COMMON MISTAKES (16:00 – 18:00)

| # | Mistake | Why Wrong | Fix |
|---|---|---|---|
| 1 | Using a mutable class variable (list/dict) | All instances share the *same* list object — appending in one affects all | Use mutable defaults in `__init__` as instance variables |
| 2 | Thinking `self.x = value` modifies the class variable | It creates a new instance attribute, shadowing the class variable | Use `ClassName.x = value` to modify the class variable |
| 3 | Counting instances with `self.count += 1` | Creates per-instance count that's always 1 | Use `ClassName.count += 1` |

**Live demo of mistake 1** — the mutable class variable trap:

```python
class Employee:
    skills = []  # DANGER — shared mutable!

    def add_skill(self, skill):
        self.skills.append(skill)

emp1 = Employee()
emp2 = Employee()
emp1.add_skill("Python")
print(emp2.skills)  # ['Python'] — WHAT?!
```

---

## RECAP + CLIFFHANGER (18:00 – 20:00)

**Cheat sheet**:

```
CLASS vs INSTANCE VARIABLES
1. Class variable = defined in class body, shared by all instances.
2. Instance variable = defined in __init__ with self, unique per object.
3. Python looks in instance first, then class (namespace chain).
4. Assigning on instance creates a NEW attribute — doesn't modify class.
5. Use ClassName.x for truly global data. Use self.x for overridable data.
6. NEVER use mutable objects (list, dict) as class variables.
```

**Cliffhanger**:

> We've seen class variables. But there's a natural next question — if we have class variables, are there also class *methods*? Methods that operate on the class itself, not on an instance?
>
> Yes. And there's also something called a static method — which belongs to the class but doesn't care about the class *or* the instance.
>
> Next video — classmethods, staticmethods, and alternative constructors. The `AgentResult.failure()` method in our project? That's a classmethod. I'll show you why.

---

## YouTube Description

```
The #1 source of subtle OOP bugs in Python — class variables vs instance variables. Learn the namespace lookup chain and never get bitten again.

In this video:
• Class variables — shared data across all instances
• Instance variables — unique data per object
• The __dict__ namespace trick that reveals everything
• self.x vs ClassName.x — when to use which
• The mutable class variable trap (lists and dicts)
• How this shows up in a real AI agent codebase

🗺️ Where this fits in the Roadmap:
Phase 1 — Python Foundations
Section: 1.2 (Object-Oriented Python)
Previous: Classes & Instances
Next: Classmethods & Staticmethods

📂 Code:
GitHub: https://github.com/balajichippada/roadmap-2026-oop-02

⏱️ Timestamps:
0:00 — The bug that class variables cause
0:30 — Why shared data needs a different approach
2:00 — Class variables explained
6:00 — The namespace lookup chain (__dict__)
10:00 — self.x vs ClassName.x
14:00 — Same pattern in the real project
16:00 — Common mistakes (mutable trap!)
18:00 — Recap + what's next

#Python #OOP #ClassVariables #Roadmap2026 #PythonTutorial
```
