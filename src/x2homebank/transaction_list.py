from typing import List

from .transaction import Transaction


class TransactionList:

    def __init__(self):
        super().__init__()
        self._transactions: List[Transaction] = []

    def get_transactions(self, ascending=True) -> List[Transaction]:
        return sorted(self._transactions, key=lambda x: x.date, reverse=not ascending)

    transactions = property(get_transactions)

    def add(self, transaction: Transaction):
        self._transactions.append(transaction)
