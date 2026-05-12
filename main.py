class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def yearly_salary(self):
        return self.salary * 12

emp = Employee("Ali", 5000000)
print(emp.yearly_salary())
