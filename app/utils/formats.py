from datetime import date, datetime
from typing import Tuple, Union


def format_housing(housing: Tuple[str, str]) -> str:
    """
    Formats a housing tuple into a string.

    :param housing: A tuple containing housing info.

    :return: A formatted string containing housing info.
    """
    type_housing = f'Tipo: {housing[0]}'
    paid_monthly = f'Mensalidade: R$ {housing[1] if len(housing[1]) else "000.00"}'
    return '\n'.join((type_housing, paid_monthly))


def format_address(address: Tuple[str, str, str, str]) -> str:
    """
    Formats an address tuple into a string.

    :param address: A tuple containing address info.

    :return: A formatted string containing address info.
    """
    street = f'Rua: {address[0]}'
    district = f'Bairro: {address[1]}'
    city = f'Cidade: {address[2]}'
    state = f'Estado: {address[3]}'
    return '\n'.join((street, district, city, state))


def format_str_to_date(value: str) -> Union[date, str]:
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
            return datetime.strptime(formatted_value, date_format).date()

        except ValueError:
            pass

    return value


def format_str_to_age(born: str) -> Union[str, int]:
    """
    Convert a string to a datetime object and calculate the age or return the original string.

    :param born: A string representing a date.

    :return: A datetime object if the string can be converted, or the original string.
    """
    today = date.today()
    formatted_born = format_str_to_date(born)

    if isinstance(formatted_born, date):
        return (
            today.year - formatted_born.year - ((today.month, today.day) < (formatted_born.month, formatted_born.day))
        )

    return born
