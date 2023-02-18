from abc import ABC, abstractmethod
from pathlib import Path
from typing import TextIO, Union, List

from ..transaction_list import TransactionList


class TransactionExporter(ABC):

    def __init__(self):
        super().__init__()
        self.n_exported = 0

    def save_to_file(self, transactions: TransactionList, filename: Union[Path, str]):
        if isinstance(filename, Path):
            with filename.open("w") as f:
                return self.write(transactions, f)
        elif isinstance(filename, str):
            with open(filename, "w") as f:
                return self.write(transactions, f)

    @abstractmethod
    def write(self, transactions: TransactionList, f: TextIO):
        pass
