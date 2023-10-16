from typing import Optional

from tinydb import TinyDB

from app import constants


class LocalConnection:
    """Class to represent a local connection."""

    def __init__(self) -> None:
        self.database: Optional[TinyDB] = None

    def __enter__(self, *args, **kwargs) -> 'LocalConnection':
        self.database = TinyDB(constants.DATABASE_PATH, indent=2)
        return self

    def __exit__(self, *args, **kwargs) -> None:
        self.database.close()
        self.database = None
