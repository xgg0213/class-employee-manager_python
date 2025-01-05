class Employee:
    def __init__(self,name,salary,title,manager=None):
        self._name=name
        self._salary=salary
        self._title=title
        self._manager=manager
        # why below can work??
        if manager:
            manager.addEmployee(self)

    def calculateBonus(self,multiplier):
        bonus=self._salary*multiplier
        return bonus
    
