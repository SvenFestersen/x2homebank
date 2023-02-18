from datetime import datetime
from typing import TextIO

from .importer import TransactionImporter
from ..transaction import Transaction, PaymentType
from ..transaction_list import TransactionList


class IngImporter(TransactionImporter):
    """Import transactions from CSV files in ING format."""

    encoding = "latin1"
    ignore_header_lines = 14

    def read(self, f: TextIO) -> TransactionList:
        self.skipped_lines = []
        date_reader = lambda x: datetime.strptime(x, "%d.%m.%Y")
        transactions = TransactionList()

        line_no = 0

        for line in f:
            line_no += 1
            if line_no <= self.ignore_header_lines:
                continue

            values = tuple(x.strip() for x in line.strip().split(";"))
            skip_line = False

            # parse date
            try:
                t_date = date_reader(values[1]).date()
            except (ValueError, IndexError):
                skip_line = True

            t_payment = PaymentType.NONE

            # parse amount
            try:
                t_amount = float(values[7].replace(".", "").replace(",", "."))
            except (ValueError, IndexError):
                skip_line = True

            if not skip_line:
                transaction = Transaction(t_date, t_payment, values[3],
                                          values[2], values[4], t_amount,
                                          "", [])
                transactions.add(transaction)
            else:
                self.skipped_lines.append(line_no)

        return transactions
