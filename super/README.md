# SuperPy User Guide

## SuperPy Description

SuperPy is a python Command Line Interface (CLI) program to keep track of a supermarket inventory and report on income data.

With command line arguments a user can:

- log products as bought or sold into an inventory,
- retrieve information on products based on product ID,
- report on profit, revenue or product sales over time,
- set, view and change the date that the program views as 'today'

SuperPy uses csv-files to keep track of product sales, and python classes to create ledgers and reports on profit and revenue over time. Report plots will show directly on the CLI but can be exported as tables to excel files, or as figures to PDF and JPEG files.

The following modules need to be installed in order to run SuperPy:

- Python (3.11.2)
- Matplotlib (3.7.1)
- pandas (2.0.0)
- Tabulate (0.9.0)

If starting a new inventory, begin with logging products using the 'buy' subcommand.

## SuperPy commands

To start SuperPy, open the superpy folder in the CLI and type the command:

`./superpy> python main.py `

followed by one of the sub-commands.

Each sub-command is explained below, and examples are provided.

&nbsp;

## The DATE commands

SuperPy keeps track of date. The date that this program views as 'today', is stored internally in a csv-file as the variable 'today'. This date can be viewed, set and moved forward or backwards by the user with the following commands:

`show-date`  
_Shows the date that SuperPy has stored as 'today'._  
`set-date <date>`  
_Sets date to input date, enter in format YYYY-MM-DD._  
`change-date <number of days>`  
_Advances the date a specific number of days, entered as an integer. Date can also be moved backward by entering a negative integer._

Only the very first time the SuperPy program is used by a user, the today variable is set automatically to the current date. After this, the today variable has to be changed by the user with `set-date` or `change-date` before logging products as bought/sold or when otherwise using the 'today' value on the command-line.

### Examples of DATE commands

```
$ python main.py show-date
This program has today's date stored as 2023-04-04
```

```
$ python main.py set-date 2023-04-17
This program has today's date stored as 2023-04-17
```

```
$ python main.py change-date 2
This program's date has been changed to 2023-04-06
```

```
$python main.py change-date -2
This program's date has been changed to 2023-04-02
```

&nbsp;

## The BUY command: logging products as bought

With the 'buy' command a user can log a product into the inventory. The buy-command is followed by named-arguments to store product information.

When an user logs product for the first time a csv-file 'bought.csv' will be created in the SuperPy folder. Afterwards, anytime a user logs products as bought, these products will be added to this file. Products get assigned a 'biught_id' based on the order they are added to the csv-file.

### Examples of BUY:

Loggin a product as bought for the very first time:

```
$ python main.py buy --product apple --price 1.4 --expiration 2025-03-01 --buydate 2023-01-10 --quantity 10
Created bought.csv
Logged apple in 'bought.csv' with product_id 1
```

&nbsp;

## The SELL command: logging products as sold

With the 'sell' command a user can log a product from the inventory as sold. The sell-command is followed by named-arguments to store product information.

When an user logs products as sold for the first time, a csv file sold.csv will be created in the SuperPy folder. Afterwards, anytime a user logs products as sold, these products will be added to this file. The program assigns a sold product a new (sold-)id, and links this to the bought-id of the product.

### Examples of SELL:

Loggin a product as sold for the very first time:

```
$ python main.py sell --product apple --price 2.0 --selldate 2023-02-12 --quantity 5
Created sold.csv
Added apple to 'sold.csv' with sold-id 1 and bought-id 1
```

&nbsp;

### Show inventory:


## The SHOW-PRODUCT command:

## Retrieving product info

With the show-product subcommand a user can retrieve information on the buy, sell and expiry data of a product, given the product id.

The show-product command is followed by only one positional argument:

`product-id`  
_The ID assigned to the product when it was logged as bought (ie. bought id). Entered as integer, required._

### Examples of SHOW-PRODUCT

Showing data on a sold product:

```
$ python main.py show-product 4

 Product ID: 4
 Product bought on: 2023-01-12
 Product expires on: 2023-03-15

 Product sold on: 2023-01-15
 Product sold for: $1.5
 Product sold for: $1.5

```

Showing data on an expired (not sold) product:

```
$ python main.py set-date 2023-05-05
This program's date has been set to 2023-05-05
$ python main.py show-product 8

 Product ID: 8
 Product name: apple
 Product bought on: 2023-03-20
 Product bought for: $0.5
 Product expires on: 2023-05-01

PRODUCT EXPIRED
```

&nbsp;

## The SHOW-INVENTORY command: show the inventory on a specific day

The show-inventory command reports on the inventory on a specific day. It is followed by the required positional argument 'date'. The inventory is then shown in the CLI in a table. The data can be exported to a csv or excel-file, by using the optional flags.

Required positional argument:  
`inventory-date`  
_The inventory date given as 'today', 'yesterday' or as date in format YYYY-MM-DD_

Flags (optional arguments):  
`--to-csv`  
_When this flag is entered the inventory is saved as a csv-file in the folder superpy/reports_  
`--to-excel`  
_When this flag is entered the inventory is saved as an excel-file in the folder superpy/reports_

The inventory will only shows products which were already bought before the input date and which have not been sold or only sold after the input date. The inventory does not include expired products.



## Examples of SHOW-PRODUCT

Show inventory on 13th of January 2023:

```
$ python main.py show-inventory 2023-01-13
+------+-----------+------------+-------------+--------------+
|   id | product   | buy_date   |   buy_price | expiration   |
|------+-----------+------------+-------------+--------------|
|    1 | yoghurt   | 2023-01-12 |         0.5 | 2025-03-15   |
|    2 | kiwi      | 2023-01-12 |         0.9 | 2025-03-15   |
|    3 | apple     | 2023-01-12 |         0.3 | 2025-03-15   |
+------+-----------+------------+-------------+--------------+
```

Show inventory and save data both as excel spreadsheet and csv-file:

```
$ python main.py show-inventory 2023-01-16 --to-excel --to-csv
+------+-----------+------------+-------------+--------------+
|   id | product   | buy_date   |   buy_price | expiration   |
|------+-----------+------------+-------------+--------------|
|    5 | mango     | 2023-01-15 |           2 | 2023-04-01   |
+------+-----------+------------+-------------+--------------+
Inventory saved as 'Inventory on 2023-01-16.csv' in Superpy/reports folder
Inventory saved as 'Inventory on 2023-01-16.xlsx' in Superpy/reports folder
```

&nbsp;

## The REPORT-TOTAL command:

## reporting on total profit and revenue

The 'report-total' commands returns total revenue or profit for a given day, month or year.
The report-total command is followed by the required positional argument 'report-type', which can be either profit or revenue.
The reporting period needs to be set with one of the named-arguments --day, --month or --year:

Required positional argument:  
`type-of-report`  
_The type of report the user wants to obtain. Choices are "revenue" or "profit"._

Named arguments, choose one of three:  
`--day`  
_Returns revenue or profit for a given date. Date can be entered as 'today', 'yesterday' or as format YYYY-MM-DD._  
`--month`  
_Returns revenue or profit for a given month. Enter in format YYYY-MM_  
`--year`  
_Returns revenue or profit for a given year. Enter in format YYYY_

## Examples of REPORT-TOTAL

```
$ python main.py report-total revenue --day 2023-01-12
Total revenue on 2023-01-12: 2.0
```

```
$ python main.py report-total revenue --year 2023
Total revenue in 2023: 9.5
```

```
$ python main.py report-total profit --day 2023-01-12
Total profit on 2023-01-12: -0.4
```

```
$ python main.py report-total profit --month 2023-01
Total profit in January 2023: 1.2
```

&nbsp;

## The REPORT-PERIOD command:

## reporting revenue, profit or sales over time.

With the report-period command a user can plot daily revenue, profit or product-sales over a given month. This subcommand is followed with the two positional arguments 'report-type' and 'month'. The 'report-type' can be set to 'revenue', 'profit', 'revenue-profit' (to show both in the same plot), or product-sales. The latter returns the number of sold items per day over a given month, for a specific product . When 'report-type' is set to 'product-sales', the user should follow the 'report-month' argument with the named-argument '--product' and the product name for which the user wants to see sales. The data of all report-types can be saved as a csv-file or an excel-spreadsheet, and the plots can be exported to JPEG or PDF with the following flags '--to-csv', '--to-excel', '--to-jpeg' and '--to-pdf'.

Required positional arguments:

`report-type`  
_The type of report, choices are 'revenue', 'profit', 'revenue-profit' (showing both), or 'product-sales'_  
`report-month`  
_The month for which daily revenue, profit or product-sales data will be calculated. Enter in format YYYY-MM._

Named-arguments:  
`--product`  
_The name of the product for which sales will be reported.
This argument is only required when report-type is set to 'product-sales'._

Flags:  
`--to-csv`  
_Saves plot data in csv file._  
`--to-excel`  
_Saves plot data as table in as Excel spreadsheet._  
`--to-pdf`  
_Saves plot figure as PDF._  
`--to-jpeg`  
_Saves plot figure as JPEG image._

### Examples of REPORT-PERIOD

Reporting revenue for January 2023 and saving data in an Excel-spreadsheet.

```
$ python main.py report-period profit 2023-01 --to-excel
+-------+----------+
|   Day |   Profit |
|-------+----------|
|     1 |      0   |
|     2 |      0   |
|     3 |      0   |
|     4 |      0   |
|     5 |      0   |
|     6 |      0   |
|     7 |      0   |
|     8 |      0   |
|     9 |      0   |
|    10 |     -1.4 |
|    11 |      0   |
|    12 |     -0.4 |
|    13 |      0   |
|    14 |      3   |
|    15 |     -0.5 |
|    16 |      0   |
|    17 |      0   |
|    18 |      0   |
|    19 |      3   |
|    20 |     -2.5 |
|    21 |      0   |
|    22 |      0   |
|    23 |      0   |
|    24 |      0   |
|    25 |      0   |
|    26 |      0   |
|    27 |      0   |
|    28 |      0   |
|    29 |      0   |
|    30 |      0   |
|    31 |      0   |
+-------+----------+
Table saved as 'profit for January 2023.xlsx' in Superpy/reports folder
```

Plotting the daily sales of apples over Januray 2023 and saving the figure as PDF:

```
$ python main.py report-period product-sales  2023-01 --product apple --to-pdf
+-------+-------------------------+
|   Day |   Number of apples sold |
|-------+-------------------------|
|     1 |                       0 |
|     2 |                       0 |
|     3 |                       0 |
|     4 |                       0 |
|     5 |                       0 |
|     6 |                       0 |
|     7 |                       0 |
|     8 |                       0 |
|     9 |                       0 |
|    10 |                       0 |
|    11 |                       0 |
|    12 |                       1 |
|    13 |                       0 |
|    14 |                       0 |
|    15 |                       0 |
|    16 |                       0 |
|    17 |                       0 |
|    18 |                       0 |
|    19 |                       0 |
|    20 |                       0 |
|    21 |                       0 |
|    22 |                       2 |
|    23 |                       1 |
|    24 |                       1 |
|    25 |                       1 |
|    26 |                       0 |
|    27 |                       0 |
|    28 |                       0 |
|    29 |                       0 |
|    30 |                       0 |
|    31 |                       0 |
+-------+-------------------------+
Figure saved as 'product-sales for January 2023.pdf' in Superpy/reports folder
```
