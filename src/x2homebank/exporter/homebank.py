from typing import TextIO

from .exporter import TransactionExporter
from ..transaction_list import TransactionList


class HomebankExporter(TransactionExporter):
    """Export transactions in Homebank CSV format."""

    date_format = "%Y-%m-%d"

    def write(self, transactions: TransactionList, f: TextIO):
        self.n_exported = 0
        f.write("date;payment;info;payee;memo;amount;category;tags\n")
        for transaction in transactions.transactions:
            ex_date = transaction.date.strftime(self.date_format)
            ex_payment = transaction.payment.value
            data = [ex_date, str(ex_payment), transaction.info,
                    transaction.payee, transaction.memo,
                    str(transaction.amount), transaction.category,
                    " ".join(transaction.tags)]
            f.write(";".join(data))
            f.write("\n")
            self.n_exported += 1
