from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class AdultEntity:
    """Class to represent an adult."""

    adult_id: int = field(init=False)
    adult_gender: str
    adult_name: str
    adult_birthdate: str
    adult_cpf: str
    adult_rg: str
    adult_ethnicity: str
    adult_religion: str
    adult_marital_status: str
    adult_household_income: str
    adult_residents: str
    adult_housing: Tuple[str, str]
    adult_activities: List[str]
    adult_address: Tuple[str, str, str, str]
    adult_contacts: List[str]

    def __post_init__(self) -> None:
        self.adult_first_name = self.adult_name.split(' ')[0]
