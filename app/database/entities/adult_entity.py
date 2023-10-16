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
    adult_activities: List[str]
    adult_address: Tuple[str, str, str, str]
    adult_contacts: List[str]
