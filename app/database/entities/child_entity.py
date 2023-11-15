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
    child_ethnicity: str
    child_religion: str
    child_clothing_number: str
    child_shoe_number: str
    child_school_name: str
    child_school_degree: str
    child_school_period: str
    child_activities: List[str]

    parent_name: str
    parent_gender: str
    parent_birthdate: str
    parent_cpf: str
    parent_rg: str
    parent_household_income: str
    parent_housing: Tuple[str, str]
    parent_authorization: str
    parent_address: Tuple[str, str, str, str]
    parent_contacts: List[str]

    def __post_init__(self) -> None:
        self.child_first_name = self.child_name.split(' ')[0]
