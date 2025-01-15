class Employee:
    def __init__(self,name,salary,title,manager=None):
        self._name=name
        self._salary=salary
        self._title=title
        self._manager=manager
        # why below can work??
        if manager: #manager here is an instance, not just a string, or the manager_name
            manager.addEmployee(self)

    def calculateBonus(self,multiplier):
        bonus=self._salary*multiplier
        return bonus
    
    # def __repr__(self):
    #     return f"name: {self._name}; salary: {self._salary}"
    
