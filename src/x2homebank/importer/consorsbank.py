import csv
from datetime import datetime
from typing import TextIO

from .importer import TransactionImporter
from ..transaction import Transaction, PaymentType
from ..transaction_list import TransactionList


class ConsorsbankDialect(csv.Dialect):
    delimiter = ";"
    doublequote = True
    escapechar = "\\"
    lineterminator = "\n"
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL
    skipinitialspace = False
    strict = True


class ConsorsbankImporter(TransactionImporter):
    """Import transactions from CSV files in Consorsbank format."""

    ignore_header_lines = 6

    def read(self, f: TextIO) -> TransactionList:
        date_reader = lambda x: datetime.strptime(x, "%d.%m.%Y")
        transactions = TransactionList()
        reader = csv.reader(f, dialect=ConsorsbankDialect())

        line_no = 0

        for row in reader:
            line_no += 1
            if line_no <= self.ignore_header_lines:
                continue

            skip_line = False
            # parse date
            try:
                t_date = date_reader(row[1]).date()
            except ValueError:
                skip_line = True

            t_payment = PaymentType.NONE
            # parse amount
            try:
                t_amount = float(row[10].replace(".", "").replace(",", "."))
            except ValueError:
                skip_line = True

            if not skip_line:
                transaction = Transaction(t_date, t_payment, row[5], row[2], row[6], t_amount, "", [])
                transactions.add(transaction)
            else:
                self.skipped_lines.append(line_no)
        return transactions

