from employee import Employee

class Manager(Employee):
    def __init__(self, name, salary, title, manager=None):
        super().__init__(name, salary, title, manager)
        self._employees=[]

    
    def addEmployee(self, employee):
        self._employees.append(employee)
        return
    def calculateBonus(self, multiplier):
        return (self._salary+self.total_subsalary()) * multiplier
    def total_subsalary(self):
        sum=0
        for employee in self._employees:
            if isinstance(employee, Manager):
                sum+=employee._salary+employee.total_subsalary()
            else:
                sum+=employee._salary
    
        return sum
    


manager_emily=Manager("emily","100","manager1")
print(manager_emily._employees)
employee_linda=Employee("linda","50","employee1",manager_emily)
print(manager_emily._employees[0].__dict__) # can use __dict__ to replace the def __repr__ instance in the Employee class