import csv
import re
from datetime import datetime
from typing import TextIO

from .importer import TransactionImporter
from ..transaction import Transaction, PaymentType
from ..transaction_list import TransactionList


class ComdirectDialect(csv.Dialect):
    delimiter = ";"
    doublequote = True
    escapechar = "\\"
    lineterminator = "\n"
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL
    skipinitialspace = False
    strict = True


class ComdirectImporter(TransactionImporter):
    """Import transactions from CSV files in Comdirect format."""

    encoding = "latin1"
    ignore_header_lines = 5
    #text_regex = re.compile(r"^(?:Auftraggeber\:|Empfänger\:) (.*?)Buchungstext: (.*?) Ref. (.*?)$")
    text_regex = re.compile(r"^(?:(?:Auftraggeber\:|Empfänger\:) (.*?))? (?:Buchungstext: (.*?))? Ref. (.*?)$")

    def read(self, f: TextIO) -> TransactionList:
        date_reader = lambda x: datetime.strptime(x, "%d.%m.%Y")
        transactions = TransactionList()
        reader = csv.reader(f, dialect=ComdirectDialect())

        line_no = 0

        for row in reader:
            line_no += 1
            if line_no <= self.ignore_header_lines:
                continue
            if len(row) == 0 or row[0] == "Alter Kontostand":
                continue
            if row[0] in "offen":
                self.skipped_lines.append(line_no)
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
                t_amount = float(row[4].replace(".", "").replace(",", "."))
            except ValueError:
                skip_line = True

            # get payee, memo from transaction text
            m = self.text_regex.match(row[3])
            if m is None:
                self.skipped_lines.append(line_no)
                continue
            payee = m.group(1) if m.group(1) is not None else ""
            memo = (m.group(2) if m.group(2) is not None else "") + "; Referenz: " + m.group(3)


            if not skip_line:
                transaction = Transaction(t_date, t_payment, "", payee, memo, t_amount, "", [])
                transactions.add(transaction)
            else:
                self.skipped_lines.append(line_no)
        return transactions

