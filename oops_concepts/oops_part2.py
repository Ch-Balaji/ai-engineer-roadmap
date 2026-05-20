class Employee:
    raise_percentage = 1.04 # Class variable
    count = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@infossy.com"
        Employee.count += 1
        self.count += 1
        
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def increase_pay(self):
        self.pay = int(self.pay * self.raise_percentage) # 4%

emp1 = Employee("Rahul", "Sharma", 800000)
print(Employee.count)
print(emp1.count)
















