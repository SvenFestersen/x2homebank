import click

from ..importer.homebank import HomebankImporter
from .display import display_csv


@click.group()
def x2homebank():
    """
    A tool to process financial transaction CSV files in Homebank format.

    Use 'show' to list all transactions in a given CSV file.

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
    """Read a CSV file in Homebank format and list the transactions."""
    date_ascending = sort_direction == "ascending"
    display_csv(HomebankImporter(), input_filename, color, date_ascending)


def main():
    x2homebank.add_command(show)
    x2homebank()
