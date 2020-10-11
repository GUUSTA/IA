from csp import Constraint, CSP
from typing import Dict, List, Optional

class ZooZoneConstraint(Constraint[str, str]):
    def __init__(self, animal1: str, animal2: str) -> None:
        super().__init__([animal1, animal2])
        self.animal1: str = animal1
        self.animal2: str = animal2

    def satisfied(self, assignment: Dict[str, str]) -> bool:
        # If either animal is not in the assignment then it is not
        # yet possible for their colors to be conflicting
        if self.animal1 not in assignment or self.animal2 not in assignment:
            return True
        
        if self.animal1 == "Leao":
            return assignment[self.animal1] == ["Zona 1"]
        elif self.animal1 == "Antilope":
            return assignment[self.animal1] != ["Zona 2"] and assignment[self.animal1] != ["Zona "] # Fazer verificao de adjacencia
        elif self.animal1 == "Suricate":
            return assignment[self.animal1] != assignment["Javali"]
        elif self.animal1 == "Javali":
            return assignment[self.animal1] != assignment["Suricate"]

        # check the color assigned to animal1 is not the same as the
        # color assigned to animal2
        # return assignment[self.animal1] != assignment[self.animal2]


if __name__ == "__main__":
    variables: List[str] = ["Leao", "Antilope", "Hiena",
                            "Tigre", "Pavao", "Suricate", "Javali"]
    domains: Dict[str, List[str]] = {}
    for variable in variables:
        domains[variable] = ["Zona 1", "Zona 2", "Zona 3", "Zona 4"]
    csp: CSP[str, str] = CSP(variables, domains)
    csp.add_constraint(ZooZoneConstraint("Leao", "Tigre"))
    csp.add_constraint(ZooZoneConstraint("Leao", "Pavao"))
    csp.add_constraint(ZooZoneConstraint("Tigre", "Pavao"))
    csp.add_constraint(ZooZoneConstraint("Tigre", "Suricate"))
    csp.add_constraint(ZooZoneConstraint("Tigre", "Javali"))
    csp.add_constraint(ZooZoneConstraint("Hiena", "Leao"))
    csp.add_constraint(ZooZoneConstraint("Hiena", "Antilope"))
    csp.add_constraint(ZooZoneConstraint("Hiena", "Javali"))
    csp.add_constraint(ZooZoneConstraint("Hiena", "Pavao"))
    csp.add_constraint(ZooZoneConstraint("Hiena", "Suricate"))
    csp.add_constraint(ZooZoneConstraint("Hiena", "Tasmania"))
    solution: Optional[Dict[str, str]] = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        print(solution)