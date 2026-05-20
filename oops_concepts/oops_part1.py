class Employee:
    count = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@infossy.com"
        

    def full_name(self):
        return f"{self.first} {self.last}"
    
    def increase_pay(self, percentage):
        self.pay = int(self.pay * (1+ percentage/100))

    #pass
print(Employee.count)
emp1 = Employee("Rahul", "Sharma", 800000) #
print(emp1.__dict__)
# emp2 = Employee("Priya", "Patel", 900000) #


