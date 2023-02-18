import click

from ..exporter.homebank import HomebankExporter
from ..importer.ing import IngImporter
from .display import display_csv


@click.group()
def ing2homebank():
    """
    A tool to process financial transaction CSV files in ING format.

    Use 'show' to list all transactions in a given CSV file or 'convert' to
    convert the CSV file to Homebank format.

    See http://homebank.free.fr for more information on Homebank.
    """


@click.command()
@click.argument("input_filename", type=click.Path())
@click.option("--color/--no-color", default=True,
              help="Enable/disable colored output.")
@click.option("--date-descending", "sort_direction", flag_value="descending",
              default=True,
              help="Sort transactions in descending date order (default).")
@click.option("--date-ascending", "sort_direction", flag_value="ascending",
              help="Sort transactions in ascending date order.")
def show(input_filename: str, color: bool, sort_direction: str):
    """Read a CSV file in ING format and list the transactions."""
    date_ascending = sort_direction == "ascending"
    display_csv(IngImporter(), input_filename, color, date_ascending)


@click.command()
@click.argument("input_filename", type=click.Path())
@click.argument("output_filename", type=click.Path())
def convert(input_filename: str, output_filename: str):
    """Convert a CSV file in ING format to Homebank format."""
    importer = IngImporter()
    exporter = HomebankExporter()
    transactions = importer.load_from_file(input_filename)
    exporter.save_to_file(transactions, output_filename)
    click.echo()
    click.echo("{} transactions exported.".format(exporter.n_exported))


def main():
    ing2homebank.add_command(show)
    ing2homebank.add_command(convert)
    ing2homebank()
