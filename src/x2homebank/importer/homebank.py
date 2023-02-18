from datetime import datetime
from typing import TextIO

from .importer import TransactionImporter
from ..transaction import Transaction, PaymentType
from ..transaction_list import TransactionList


class HomebankImporter(TransactionImporter):
    """Import transactions from CSV files in Homebank format."""

    ignore_header_lines = 1

    def read(self, f: TextIO) -> TransactionList:
        self.skipped_lines = []
        date_reader = lambda x: datetime.strptime(x, "%Y-%m-%d")
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
                t_date = date_reader(values[0]).date()
            except ValueError:
                skip_line = True

            # parse payment info
            try:
                t_payment = PaymentType(int(values[1]))
            except ValueError:
                skip_line = True

            # parse amount
            try:
                t_amount = float(values[5].replace(",", "."))
            except ValueError:
                skip_line = True

            # parse tags
            t_tags = values[7].split(" ")

            if not skip_line:
                transaction = Transaction(t_date, t_payment, values[2],
                                          values[3], values[4], t_amount,
                                          values[6], t_tags)
                transactions.add(transaction)
            else:
                self.skipped_lines.append(line_no)

        return transactions
