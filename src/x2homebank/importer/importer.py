from abc import ABC, abstractmethod
from pathlib import Path
from typing import TextIO, Union, List

from ..transaction_list import TransactionList


class TransactionImporter(ABC):
    """Base class for transaction importers."""

    encoding = "utf8"
    ignore_header_lines = 0

    def __init__(self):
        super().__init__()
        self.skipped_lines: List[int] = []

    def load_from_file(self, filename: Union[Path, str]) -> TransactionList:
        if isinstance(filename, Path):
            with filename.open("r", encoding=self.encoding) as f:
                return self.read(f)
        elif isinstance(filename, str):
            with open(filename, "r", encoding=self.encoding) as f:
                return self.read(f)

    @abstractmethod
    def read(self, f: TextIO) -> TransactionList:
        pass


