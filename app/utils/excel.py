from datetime import datetime
from typing import Dict, List, Union

import pandas as pd

from app.database.entities import AdultEntity, ChildEntity


def str_to_date(value: str) -> Union[datetime, str]:
    """
    Convert a string to a datetime object or return the original string.

    :param value: A string representing a date.
    :return: A datetime object if the string can be converted, or the original string.
    """
    date_formats = ['%m/%d/%Y', '%d/%m/%Y']
    formatted_value = value.replace('-', '/')

    if not len(value):
        return value

    for date_format in date_formats:
        try:
            return datetime.strptime(formatted_value, date_format)

        except ValueError:
            pass

    return formatted_value


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
                'CPF': [register.child_cpf for register in registers],
                'RG': [register.child_rg for register in registers],
                'Nascimento': [str_to_date(register.child_birthdate) for register in registers],
                'Endereço': ['\n'.join(register.parent_address) for register in registers],
                'Contatos': ['\n'.join(register.parent_contacts) for register in registers],
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
                'CPF': [register.adult_cpf for register in registers],
                'RG': [register.adult_rg for register in registers],
                'Nascimento': [str_to_date(register.adult_birthdate) for register in registers],
                'Endereço': ['\n'.join(register.adult_address) for register in registers],
                'Contatos': ['\n'.join(register.adult_contacts) for register in registers],
            }
            data_frame = pd.DataFrame(data)
            data_frame.to_excel(writer, sheet_name=activity, index=False)
