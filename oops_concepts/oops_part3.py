import datetime

class Employee:
    # ── Class variables ──────────────────────────────
    raise_percentage = 1.04
    num_of_employees = 0
    company = "Infosys"

    # ── Constructor ──────────────────────────────────
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@infosys.com"
        Employee.num_of_employees += 1

    # ── REGULAR METHOD — uses `self` (instance data) ─
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_percentage)

    def full_name(self):
        return f"{self.first} {self.last}"

    # ── CLASS METHOD — uses `cls` (class data) ───────
    @classmethod
    def set_raise_percentage(cls, amount):
        cls.raise_percentage = amount

    @classmethod
    def from_csv(cls, csv_row):
        first, last, pay = csv_row.split("-")
        return cls(first, last, int(pay))

    # ── STATIC METHOD — no self, no cls ──────────────
    @staticmethod
    def is_workday(day):
        return day.weekday() < 5


# ── Using each kind ──────────────────────────────────

# 1. Regular method — needs an instance
emp1 = Employee("Rahul", "Sharma", 800000)
emp1.apply_raise()
print(emp1.pay)                                  # 832000
print(emp1.full_name())                          # Rahul Sharma

# 2. Class method — called on the class
Employee.set_raise_percentage(1.07)
print(Employee.raise_percentage)                 # 1.07


# 4. Static method — no instance, no class state
my_date = datetime.date(2024, 4, 15)             # Monday
weekend = datetime.date(2024, 4, 14)             # Sunday
print(Employee.is_workday(my_date))              # True
print(Employee.is_workday(weekend))              # False