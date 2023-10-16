from typing import Any, Dict, List, Optional

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
