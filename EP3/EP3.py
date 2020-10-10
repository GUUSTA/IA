from csp import Constraint, CSP
from typing import Dict, List, Optional

class ZooZoneConstraint(Constraint[str, str]):
    def __init__(self, place1: str, place2: str) -> None: