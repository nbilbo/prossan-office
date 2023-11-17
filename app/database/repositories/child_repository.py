from collections import defaultdict
from typing import Any, Dict, List, Optional, Set

from app.database.connections import LocalConnection
from app.database.entities import ChildEntity


class ChildRepository:
    """
    A class for managing child records in a database.

    This class provides methods to perform various operations on adult records, including insertion, retrieval, update,
    and deletion.
    """

    @staticmethod
    def insert_one(values: Dict[str, Any]) -> int:
        """
        Insert a single child record into the database.

        :param values: A dictionary containing the data for the child record.

        :return: The document ID of the inserted record.
        """
        with LocalConnection() as connection:
            database = connection.database
            table = database.table('children')
            document_id = table.insert(values)

            return document_id

    @staticmethod
    def select_one(child_id: int) -> Optional[ChildEntity]:
        """
        Retrieve a single adult record by its ID.

        :param child_id: The ID of the adult record to retrieve.

        :return: An ChildEntity representing the retrieved record, or None if not found.
        """
        with LocalConnection() as connection:
            database = connection.database
            table = database.table('children')
            register = table.get(doc_id=child_id)

            if register is not None:
                child_entity = ChildEntity(**register)
                child_entity.child_id = register.doc_id
                return child_entity

            return None

    @staticmethod
    def select_many() -> List[ChildEntity]:
        """
        Retrieve multiple child records from the database.

        :return: A list of ChildEntity objects representing the retrieved records.
        """
        registers = []

        with LocalConnection() as connection:
            database = connection.database
            table = database.table('children')

            for register in table.all():
                child = ChildEntity(**register)
                child.child_id = register.doc_id
                registers.append(child)

        return registers[::-1]

    @staticmethod
    def update_one(child_id: int, values: Dict[str, Any]) -> None:
        """
        Update the data of a single child record identified by its ID.

        :param child_id: The ID of the adult record to update.

        :param values: A dictionary containing the updated data for the child record.

        :return: None
        """
        with LocalConnection() as connection:
            database = connection.database
            table = database.table('children')
            table.update(values, doc_ids=[child_id])

    @staticmethod
    def delete_one(child_id: int) -> None:
        """
        Delete a single child record from the database by its ID.

        :param child_id: The ID of the adult record to delete.

        :return: None
        """
        with LocalConnection() as connection:
            database = connection.database
            table = database.table('children')
            table.remove(doc_ids=[child_id])

    @staticmethod
    def order_by_activities() -> Dict[str, List[ChildEntity]]:
        """
        Order child registers by activities.

        :return: A dictionary with activities as keys and lists of child registers as values.
        """
        registers = ChildRepository.select_many()
        result = defaultdict(list)

        for register in registers:
            result['geral'].append(register)
            for activity in register.child_activities:
                result[activity].append(register)

        return dict(result)

    @staticmethod
    def get_activities() -> Set[str]:
        """
        Get unique child activities.

        :return: A set containing unique child activities.
        """
        activities = set()

        for register in ChildRepository.select_many():
            activities.update(register.child_activities)

        return activities
