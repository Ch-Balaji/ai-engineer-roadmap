# V__— Python OOP Part 1: Classes & Instances

---

## Video Metadata

| Field | Value |
|---|---|
| Video # | V0__ |
| Slug | `oop-01-classes-and-instances` |
| Playlist | Phase 1 — Python Foundations / OOP Series |
| Target length | 20–22 min |
| Slot | Mon / Wed / Fri 7 PM IST |
| Previous video | (last Core Python video) |
| Next video | V0__ — Class Variables vs Instance Variables |

## Roadmap Mapping

```
- Phase: 1 — Python Foundations
- Sections covered: 1.2 (Object-Oriented Python — Classes, __init__, instance vs class methods)
- Prerequisites needed: 1.1 (Core Python — functions, type hints)
- Capstone contribution: No (but builds toward v2_oop agent architecture)
```

## Visual / Production Plan

| Segment | Medium |
|---|---|
| 0:00–0:45 Hook | Mac screen — live demo of resume agent running |
| 0:45–2:30 Bridge | Mac screen (show pipeline.py + base.py briefly) → face-cam |
| 2:30–8:00 Concept 1 (Classes & Instances) | Mac screen — VS Code, building Employee class from scratch |
| 8:00–12:00 Concept 2 (__init__ and instance variables) | Mac screen — VS Code + terminal |
| 12:00–16:00 Concept 3 (Methods) | Mac screen — adding methods, self explained |
| 16:00–18:00 Bridge to real project | Mac screen — show BaseAgent.__init__ side by side with Employee |
| 18:00–20:00 Common Mistakes | Sketchbook ❌ vs ✅ |
| 20:00–22:00 Recap + Cliffhanger | Sketchbook cheat sheet → face-cam |

---

## HOOK (0:00 – 0:45) — Pattern: Live Demo First

**On screen**: Mac terminal — running the resume_jd_tailor_agent. Paste a resume and JD. The pipeline runs. Output streams:

```
✓ [JD Extractor] Step 0: OK (1340ms)
✓ [Resume Matcher] Step 1: OK (1890ms)
✓ [Resume Rewriter] Step 2: OK (2100ms)
✓ [Cover Letter Writer] Step 3: OK (1560ms)
✓ [Critic] Step 4: OK (980ms)
✓ [Interview Generator] Step 6: OK (1200ms)
```

**Spoken (≤45 sec)**:

> Look at this. Six AI agents — each one reads a resume, analyzes a job description, rewrites bullets, writes a cover letter, critiques its own work, and generates interview questions. All automated. All running through one pipeline.
>
> Now let me show you the code that makes this work.
>
> *[Switch to pipeline.py — scroll to show the 6 agent objects]*
>
> Six objects. One base class they all inherit from. About five OOP concepts holding the whole thing together.
>
> By the end of this series, you'll understand every line here. Today — we start with the most fundamental one: what a class actually is, and how you create instances of it.

---

## CONTEXT BRIDGE (0:45 – 2:30)

**Spoken**:

> If you've been following the roadmap, you already know functions, decorators, type hints — the core Python toolkit. But here's the thing — once your code grows past a few hundred lines, functions alone start to get messy. You end up passing the same five variables into every function. You lose track of what belongs together.
>
> Classes solve that. They let you bundle data and behavior into one unit. And every serious Python project — Django, FastAPI, LangChain, every agent framework — is built on classes.
>
> This is Phase 1, section 1.2. Object-Oriented Python. We're going to break this into a series because there's a lot to cover — inheritance, abstract classes, magic methods — but today, just the foundation. Classes and instances.

---

## THE PROBLEM (2:30 – 4:00)

**Medium**: Mac screen — VS Code with a simple script.

**Spoken**:

> Let's say you're building an internal tool for your company. You need to represent employees — each one has a name, email, department, salary. And you need to perform actions on them — give raises, generate reports, send notifications.
>
> Without classes, here's what you'd do:

```python
# Without classes — just dictionaries and functions
emp1_first = "Ravi"
emp1_last = "Kumar"
emp1_email = "ravi.kumar@company.com"
emp1_pay = 50000

emp2_first = "Priya"
emp2_last = "Sharma"
emp2_email = "priya.sharma@company.com"
emp2_pay = 60000

def give_raise(first, last, pay, percent):
    return int(pay * (1 + percent / 100))

# Every time — pass everything manually
emp1_pay = give_raise(emp1_first, emp1_last, emp1_pay, 10)
```

> See the problem? Every employee is scattered across separate variables. Nothing ties them together. Add a third employee and you're copy-pasting. Add a tenth and you're drowning.
>
> Classes fix this. One blueprint. Unlimited employees. Each one carries its own data and its own behavior.

---

## THE SOLUTION — Concept Teaching (4:00 – 16:00)

### Concept 1: Creating a Class (4:00 – 8:00)

| Beat | Content |
|---|---|
| What | A class is a blueprint for creating objects. An instance is one specific object created from that blueprint. |
| When | Any time you have entities with shared structure but unique data — employees, agents, database connections, API clients. |
| Why | Groups related data + behavior. Reusable. Extensible. |
| Code | Build `Employee` class step by step |

**Spoken + Code**:

> A class is just a blueprint. Let me show you.

```python
class Employee:
    pass
```

> That's a valid class. Does nothing yet, but it's valid. `pass` just means "I'll fill this in later."
>
> Now — the class is the blueprint. An *instance* is a specific employee created from that blueprint.

```python
emp1 = Employee()
emp2 = Employee()

print(emp1)  # <__main__.Employee object at 0x...>
print(emp2)  # <__main__.Employee object at 0x...>
```

> Two objects. Same class. Different memory locations. They're independent — changing one doesn't affect the other. This distinction — class vs instance — is the foundation of everything else.

---

### Concept 2: `__init__` and Instance Variables (8:00 – 12:00)

| Beat | Content |
|---|---|
| What | `__init__` is the constructor — runs automatically when you create an instance. Instance variables are data unique to each object. |
| When | Every class you'll ever write has an `__init__`. |
| Why | Automates setup. No more manual assignment after creation. |
| Gotcha | Forgetting `self` — the most common beginner error. |

**Spoken + Code**:

> Right now our Employee is empty. Let's give it data.
>
> I *could* do this manually:

```python
emp1 = Employee()
emp1.first = "Ravi"
emp1.last = "Kumar"
emp1.email = "ravi.kumar@company.com"
emp1.pay = 50000
```

> But that's exactly the mess we were trying to escape. Instead, we use `__init__` — think of it as "initialize." It runs automatically every time you create an instance.

```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@company.com"
```

> Now `self` — this is the part that confuses people. `self` is just the instance being created. When you write `self.first = first`, you're saying "this specific employee's first name is whatever was passed in."
>
> Python passes `self` automatically. You never pass it yourself:

```python
emp1 = Employee("Ravi", "Kumar", 50000)
emp2 = Employee("Priya", "Sharma", 60000)

print(emp1.email)  # ravi.kumar@company.com
print(emp2.email)  # priya.sharma@company.com
```

> Each instance has its own data. `emp1.pay` and `emp2.pay` are completely independent. Change one, the other doesn't move.

---

### Concept 3: Methods (12:00 – 16:00)

| Beat | Content |
|---|---|
| What | A method is a function that belongs to a class. It operates on the instance's data. |
| When | Any action an object should be able to perform on itself. |
| Why | Keeps behavior next to the data it operates on. |
| Code | `full_name()`, `apply_raise()` |

**Spoken + Code**:

> We have data. Now let's add behavior.
>
> Say I want the full name. I *could* do this every time:

```python
print(f"{emp1.first} {emp1.last}")
```

> But that's repetitive. Instead — a method:

```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@company.com"

    def full_name(self):
        return f"{self.first} {self.last}"

    def apply_raise(self, percent):
        self.pay = int(self.pay * (1 + percent / 100))
```

> Notice — every method takes `self` as the first parameter. That's how the method knows *which* employee it's working on.

```python
emp1 = Employee("Ravi", "Kumar", 50000)

print(emp1.full_name())  # Ravi Kumar

print(emp1.pay)          # 50000
emp1.apply_raise(10)
print(emp1.pay)          # 55000
```

> The method modifies *that specific instance's* data. `emp2` is untouched.
>
> One thing — don't forget the parentheses. `emp1.full_name` without `()` gives you the method object, not the result. Common mistake.

---

## BRIDGE TO REAL PROJECT (16:00 – 18:00)

**Medium**: Mac screen — split view: Employee class on left, `base.py` on right.

**Spoken**:

> Now let me show you where this shows up in the real project.
>
> *[Open resume_jd_tailor_agent/v2_oop/agents/base.py]*
>
> Look at `BaseAgent.__init__`:

```python
def __init__(self, llm_client: LLMClient):
    self._llm_client = llm_client
    self._execution_count = 0
    self._total_time_ms = 0.0
```

> Same pattern. Takes `self`. Stores instance variables. Every agent that inherits from this gets an `llm_client`, an execution counter, and a timer — automatically.
>
> And methods:

```python
def execute(self, **kwargs) -> AgentResult:
    # validate → process → format → return result
    ...
```

> `execute()` is a method — just like our `apply_raise()`. It operates on the instance's data. The only difference? This one calls an LLM instead of doing math.
>
> Same concepts. Same `self`. Same pattern. The project just has more of it.

---

## COMMON MISTAKES (18:00 – 20:00)

**Medium**: Sketchbook ❌ vs ✅

| # | Mistake | Why Wrong | Fix |
|---|---|---|---|
| 1 | Forgetting `self` in method definition | `def full_name():` → TypeError: takes 0 positional arguments but 1 was given | Always include `self` as first parameter in instance methods |
| 2 | Forgetting `()` when calling a method | `emp1.full_name` returns `<bound method ...>` not the name | `emp1.full_name()` — parentheses execute the method |
| 3 | Modifying the class instead of the instance | `Employee.pay = 70000` sets a class-level attribute, doesn't change any instance | Use `emp1.pay = 70000` or a method like `apply_raise()` |
| 4 | Putting logic outside `__init__` that should be inside | Setting attributes after creation is fragile and easy to forget | If every instance needs it, put it in `__init__` |

**Show mistake 1 live in terminal** — trigger the error, read the traceback, fix it.

---

## RECAP + CLIFFHANGER (20:00 – 22:00)

**Sketchbook cheat sheet (hand-drawn)**:

```
CLASSES & INSTANCES
1. Class = blueprint. Instance = one specific object.
2. __init__ runs automatically on creation — your constructor.
3. self = the instance being operated on. Always first param.
4. Instance variables (self.x) = data unique to each object.
5. Methods = functions inside a class. They get self automatically.
```

**Cliffhanger**:

> So now you can create classes, store data, and add behavior. But here's a question — what if there's data that should be the same for *every* employee? A company-wide raise percentage. A count of total employees. That's not instance data — it belongs to the class itself.
>
> Next video — class variables vs instance variables. When to use each. And why getting it wrong causes bugs that are incredibly hard to find.
>
> See you then.

---

## YouTube Description

```
Stop writing scattered variables and disconnected functions. Learn how classes actually work in Python — and see them in a real AI agent project.

In this video:
• What a class is and how to create instances
• __init__ — the constructor that runs automatically
• self — what it is and why every method needs it
• Instance variables — data unique to each object
• Methods — behavior that belongs to the object
• How this maps to a real multi-agent AI system

🗺️ Where this fits in the Roadmap:
Phase 1 — Python Foundations
Section: 1.2 (Object-Oriented Python)
Prerequisite: 1.1 (Core Python — functions, type hints)
Next video: Class Variables vs Instance Variables
Full Roadmap: https://github.com/balajichippada/roadmap-2026

📂 Code:
GitHub: https://github.com/balajichippada/roadmap-2026-oop-01

⏱️ Timestamps:
0:00 — Hook: The AI agent system you'll build
0:45 — Why classes matter
2:30 — The problem without classes
4:00 — Creating your first class
8:00 — __init__ and instance variables
12:00 — Methods and self
16:00 — Same pattern in the real project
18:00 — Common mistakes
20:00 — Recap + what's next

📬 Connect:
Sunday live (free, 7 PM IST): {channel live link}
1:1 doubt clearing & resume help (form): {wait-list link}

#Python #OOP #AgenticAI #Roadmap2026 #PythonClasses
```

---

## Pre-Record Checklist

- [ ] Hook ≤45s, shows the real project running
- [ ] No "guys", direct address only
- [ ] English jargon preserved: `class`, `instance`, `constructor`, `__init__`, `self`, `method`, `attribute`
- [ ] Roadmap mapping filled
- [ ] Code examples start simple (Employee), bridge to real project (BaseAgent)
- [ ] Open loop: "by the end of this series you'll understand every line"
- [ ] Common mistakes includes one live error in terminal
- [ ] Cliffhanger to next video (class variables)
- [ ] GitHub repo with clean Employee examples + link to v2_oop for reference
