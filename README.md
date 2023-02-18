# x2homebank
This repository provides a Python package to display and convert transaction
CSV files obtained from German online banking portals to a format that's
suitable for import into Homebank
(http://homebank.free.fr/help/misc-csvformat.html).

## Supported Banks
Currently, only two German banks are supported:

| Bank        | Website                  | Script               |
|-------------|--------------------------|----------------------|
| Consorsbank | https://consorsbank.de   | consorsbank2homebank |
| ING         | https://ing.de           | ing2homebank         |

## Usage
The `x2homebank` package provides tree command line tools: `x2homebank` for
processing files in Homebank format, `consorsbank2homebank` for files in
Consorsbank format and `ing2homebank` for files downloaded from ING.

All three tools support the command `show` that reads a CSV file and displays
the transactions it finds in that file, e.g.

    ing2homebank show /path/to/ing.csv

The `consorsbank2homebank` and `ing2homebank` tools support the additional
command `convert` that read the content of the input CSV file and writes it
to a CSV file in Homebank format, e.g.

    ing2homebank convert /path/to/ing.csv /path/to/export.csv

Note that the export file is overwritten if it already exists.

## Installation
To install the x2homebank scripts, run

    python setup.py install
  
with root privileges. The only dependency is *click*
(see https://click.palletsprojects.com/), which is installed automatically by
the setup script.
