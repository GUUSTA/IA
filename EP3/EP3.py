from csp import Constraint, CSP
from typing import Dict, List, Optional

class ZooZoneConstraint(Constraint[str, str]):
    def __init__(self, animal1: str, animal2: str) -> None:
        super().__init__([animal1, animal2])
        self.animal1: str = animal1
        self.animal2: str = animal2

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        # print(assignment)
        # print(self.animal1)
        # print(self.animal2)
        if self.animal1 == "Leao" and assignment[self.animal1] in assignment:
            if assignment[self.animal1] == 1:
                return True
        if self.animal1 == "Antilope":
            if "Leao" in assignment and "Tigre" in assignment:
                return assignment[self.animal1] != (assignment["Leao"] + 1) and assignment[self.animal1] != (assignment["Tigre"] + 1) and assignment[self.animal1] != (assignment["Tigre"] - 1) 
        if self.animal1 not in assignment or self.animal2 not in assignment:
            return True
        return assignment[self.animal1] != assignment[self.animal2]


if __name__ == "__main__":
    variables: List[str] = ["Leao", "Antilope", "Hiena", "Tigre", "Pavao", "Suricate", "Javali"]
    domains: Dict[str, List[int]] = {}
    for variable in variables:
        domains[variable] = [1, 2, 3, 4]
    csp: CSP[str, str] = CSP(variables, domains)
    csp.add_constraint(ZooZoneConstraint("Leao", "Tigre"))
    csp.add_constraint(ZooZoneConstraint("Leao", "Pavao"))
    csp.add_constraint(ZooZoneConstraint("Leao", "Antilope"))
    csp.add_constraint(ZooZoneConstraint("Antilope", "Leao"))
    csp.add_constraint(ZooZoneConstraint("Antilope", "Tigre"))
    csp.add_constraint(ZooZoneConstraint("Hiena", "Leao"))
    csp.add_constraint(ZooZoneConstraint("Hiena", "Antilope"))
    csp.add_constraint(ZooZoneConstraint("Hiena", "Javali"))
    csp.add_constraint(ZooZoneConstraint("Hiena", "Pavao"))
    csp.add_constraint(ZooZoneConstraint("Hiena", "Suricate"))
    csp.add_constraint(ZooZoneConstraint("Tigre", "Pavao"))
    csp.add_constraint(ZooZoneConstraint("Tigre", "Suricate"))
    csp.add_constraint(ZooZoneConstraint("Tigre", "Javali"))
    csp.add_constraint(ZooZoneConstraint("Tigre", "Antilope"))
    csp.add_constraint(ZooZoneConstraint("Tigre", "Leao"))
    csp.add_constraint(ZooZoneConstraint("Pavao", "Leao"))
    csp.add_constraint(ZooZoneConstraint("Pavao", "Tigre"))
    csp.add_constraint(ZooZoneConstraint("Suricate", "Tigre"))
    csp.add_constraint(ZooZoneConstraint("Suricate", "Hiena"))
    csp.add_constraint(ZooZoneConstraint("Javali", "Tigre"))
    csp.add_constraint(ZooZoneConstraint("Javali", "Hiena"))
    solution: Optional[Dict[str, str]] = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        print(solution)