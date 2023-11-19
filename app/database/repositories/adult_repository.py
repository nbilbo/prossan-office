import re
from collections import defaultdict
from typing import Any, Dict, List, Optional, Set

from tinydb import Query

from app.database.connections import LocalConnection
from app.database.entities import AdultEntity


class AdultRepository:
    """
    A class for managing adult records in a database.

    This class provides methods to perform various operations on adult records, including insertion, retrieval, update,
    and deletion.
    """

    @staticmethod
    def insert_one(values: Dict[str, Any]) -> int:
        """
        Insert a single adult record into the database.

        :param values: A dictionary containing the data for the adult record.

        :return: The document ID of the inserted record.
        """
        with LocalConnection() as connection:
            database = connection.database
            table = database.table('adults')
            document_id = table.insert(values)
            return document_id

    @staticmethod
    def select_one(adult_id: int) -> Optional[AdultEntity]:
        """
        Retrieve a single adult record by its ID.

        :param adult_id: The ID of the adult record to retrieve.

        :return: An AdultEntity representing the retrieved record, or None if not found.
        """
        with LocalConnection() as connection:
            database = connection.database
            table = database.table('adults')
            register = table.get(doc_id=adult_id)

            if register is not None:
                adult_entity = AdultEntity(**register)
                adult_entity.adult_id = register.doc_id
                return adult_entity

            return None

    @staticmethod
    def select_many() -> List[AdultEntity]:
        """
        Retrieve multiple adult records from the database.

        :return: A list of AdultEntity objects representing the retrieved records.
        """
        registers: List[AdultEntity] = []

        with LocalConnection() as connection:
            database = connection.database
            table = database.table('adults')

            for register in table.all():
                adult = AdultEntity(**register)
                adult.adult_id = register.doc_id
                registers.append(adult)

        return registers[::-1]

    @staticmethod
    def update_one(adult_id: int, values: Dict[str, Any]) -> None:
        """
        Update the data of a single adult record identified by its ID.

        :param adult_id: The ID of the adult record to update.

        :param values: A dictionary containing the updated data for the adult record.

        :return: None
        """
        with LocalConnection() as connection:
            database = connection.database
            table = database.table('adults')
            table.update(values, doc_ids=[adult_id])

    @staticmethod
    def delete_one(adult_id: int) -> None:
        """
        Delete a single adult record from the database by its ID.

        :param adult_id: The ID of the adult record to delete.

        :return: None
        """
        with LocalConnection() as connection:
            database = connection.database
            table = database.table('adults')
            table.remove(doc_ids=[adult_id])

    @staticmethod
    def order_by_activities() -> Dict[str, List[AdultEntity]]:
        """
        Order adult registers by activities.

        :return: A dictionary with activities as keys and lists of adult registers as values.
        """
        registers = AdultRepository.select_many()
        result = defaultdict(list)

        for register in registers:
            result['geral'].append(register)
            for activity in register.adult_activities:
                result[activity].append(register)

        return dict(result)

    @staticmethod
    def get_activities() -> Set[str]:
        """
        Get unique adult activities.

        :return: A set containing unique adult activities.
        """
        activities = set()

        for register in AdultRepository.select_many():
            activities.update(register.adult_activities)

        return activities

    @staticmethod
    def search_many(searched: str) -> List[AdultEntity]:
        """
        Search for multiple adult records based on a search query.

        :param searched:The search query used to find matching adult records.

        :return:  list of AdultEntity objects matching the search query.
        """
        registers = []
        query = Query()

        with LocalConnection() as connection:
            database = connection.database
            table = database.table('adults')

            documents = table.search(
                (query.adult_name.matches(searched, flags=re.IGNORECASE))
                | (query.adult_cpf.matches(searched, flags=re.IGNORECASE))
                | (query.adult_rg.matches(searched, flags=re.IGNORECASE))
            )

            for document in documents:
                adult = AdultEntity(**document)
                adult.adult_id = document.doc_id
                registers.append(adult)

        return registers[::-1]
