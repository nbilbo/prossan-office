from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class ChildEntity:
    """Class to represent a child."""

    child_id: int = field(init=False)
    child_gender: str
    child_name: str
    child_birthdate: str
    child_cpf: str
    child_rg: str
    child_activities: List[str]

    parent_name: str
    parent_gender: str
    parent_birthdate: str
    parent_cpf: str
    parent_rg: str
    parent_address: Tuple[str, str, str, str]
    parent_contacts: List[str]
