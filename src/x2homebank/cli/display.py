from click import echo, secho

from ..importer.importer import TransactionImporter
from ..transaction_list import TransactionList


def display_csv(importer: TransactionImporter, filename: str, color=True, date_ascending=False) -> TransactionList:
    transactions = importer.load_from_file(filename)
    display_transactions(transactions, color=color,
                         date_ascending=date_ascending)
    if importer.skipped_lines:
        echo("")
        echo("WARNING:")
        echo("  Skipped line numbers: {}".format(", ".join([str(x) for x in importer.skipped_lines])))
    return transactions


def display_transactions(transactions: TransactionList, color=True, date_ascending=False):
    for transaction in transactions.get_transactions(ascending=date_ascending):
        d = (transaction.payee[:30], transaction.memo[:24])
        out_line = "  {:<30}  {:<24}".format(*d)
        echo("{:%Y-%m-%d}  ".format(transaction.date), nl=False)
        if color and transaction.amount > 0:
            secho("{:>+10.2f}".format(transaction.amount), fg="green",
                  nl=False)
        elif color and transaction.amount < 0:
            secho("{:>+10.2f}".format(transaction.amount), fg="red", nl=False)
        else:
            echo("{:>+10.2f}".format(transaction.amount), nl=False)

        echo(out_line)
