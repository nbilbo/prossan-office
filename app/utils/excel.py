from typing import Dict, List

import pandas as pd

from app.database.entities import AdultEntity, ChildEntity
from app.utils.formats import format_str_to_age, format_str_to_date


def export_children_to_excel(values: Dict[str, List[ChildEntity]], file_path: str) -> None:
    """
    Export child registers to an Excel file.

    :param values: A dictionary where keys represent activities and values are lists of ChildEntity objects.
    :param file_path: The file path to save the Excel document.

    :return: None
    """
    with pd.ExcelWriter(file_path) as writer:
        for activity, registers in values.items():
            data = {
                'Nome': [register.child_name for register in registers],
                'Gênero': [register.child_gender for register in registers],
                'Nascimento': [format_str_to_date(register.child_birthdate) for register in registers],
                'Idade': [format_str_to_age(register.child_birthdate) for register in registers],
                'CPF': [register.child_cpf for register in registers],
                'RG': [register.child_rg for register in registers],
            }
            data_frame = pd.DataFrame(data)
            data_frame.to_excel(writer, sheet_name=activity, index=False)


def export_adults_to_excel(values: Dict[str, List[AdultEntity]], file_path: str) -> None:
    """
    Export adult registers to an Excel file.

    :param values: A dictionary where keys represent activities and values are lists of AdultEntity objects.
    :param file_path: The file path to save the Excel document.

    :return: None
    """
    with pd.ExcelWriter(file_path) as writer:
        for activity, registers in values.items():
            data = {
                'Nome': [register.adult_name for register in registers],
                'Gênero': [register.adult_gender for register in registers],
                'Nascimento': [format_str_to_date(register.adult_birthdate) for register in registers],
                'Idade': [format_str_to_age(register.adult_birthdate) for register in registers],
                'CPF': [register.adult_cpf for register in registers],
                'RG': [register.adult_rg for register in registers],
            }
            data_frame = pd.DataFrame(data)
            data_frame.to_excel(writer, sheet_name=activity, index=False)
