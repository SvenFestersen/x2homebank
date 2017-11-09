# x2homebank
This repository provides Python scripts to convert transaction CSV files obtained from German online banking portals to a
format that's suitable for import into Homebank (http://homebank.free.fr/help/misc-csvformat.html).

## Supported Banks
Currently, only two German banks are supported:

| Bank        | Website                | Script               |
| ----------- | ---------------------- | -------------------- |
| Consorsbank | https://consorsbank.de | consorsbank2homebank |
| ING-DiBa    | https://ing-diba.de    | ingdiba2homebank     |

## Usage
The repository contains one script per bank. To perform a simple conversion, run

    ingdiba2homebank download.csv out.csv
    
This will convert a CSV file "download.csv" downloaded from the ING-DiBa online banking website to a file "out.csv".
Conversion will fail if the output file already exists, i.e. existing data is not overwritten.

The Homebank payment type is set to 0 ("none") by default. To apply a different payment type, e.g. 4 ("transfer") to
all transactions, use the `--payment` parameter:

    ingdiba2homebank download.csv out.csv --payment 4
    
Similarly, it is possible to assign the same category to all transactions using the `--category` parameter:

    ingdiba2homebank download.csv out.csv --category Expenses
    
By default, no category is set. One or more tags can be assigned to all transactions with the `--tag` parameter:

    ingdiba2homebank download.csv out.csv --tag tag1 --tag tag2 --tag tag3

## Installation
To install the x2homebank scripts, run

    python setup.py install
  
with root privileges. Pandas (http://pandas.pydata.org/) is required to install and use the scripts.
The installation script will install the scripts globally, so they are available to all users.
