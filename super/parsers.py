import argparse

from datetime import date
from trackdate import valid_date, valid_month, valid_year


def create_super_parser():
    super_parser = argparse.ArgumentParser(
        description="""Keep track of the supermarket inventory.
        Log products as 'bought' or 'sold',
        show information on a product or current inventory
        or report on profit and revenue
        on certain days or over time period"""
    )
    # Creating the subparser.
    subparsers = super_parser.add_subparsers(
        dest="command",
        help="Sub-commands")

    # subparser for buy command
    buy_parser = subparsers.add_parser(
        "buy",
        help="""Log a product into the inventory.
        Follow with the required named-arguments product-name (--product),
        price (--price) and expiration-date (--expiration).""",
    )

    # using named-arguments for the buy and sell sub-commands
    # because if arguments were positional,
    # their order would be hard to remember
    # If arguments are required, the 'required' option is set to True

    buy_parser.add_argument(
        "--product",
        required=True,
        help="Enter the product name.",
    )
    buy_parser.add_argument(
        "--buydate",
        required=True,
        default="today",
        type=valid_date,
        help="""Enter buy-date in format YYYY-MM-DD.""",
    )
    buy_parser.add_argument(
        "--price",
        required=True,
        type=float,
        help="Enter price as float with 1 decimal.",
    )
    buy_parser.add_argument(
        "--expiration",
        required=True,
        type=valid_date,
        help="Enter expiration date in format YYYY-MM-DD.",
    )
    buy_parser.add_argument(
        "--quantity",
        required=True,
        default=1,
        type=int,
        help="""Enter number of products bought on the same date,
        for the same price and with a similar expiration date.""",
    )

    # subparser for sell command,
    sell_parser = subparsers.add_parser(
        "sell",
        help="""Log a product as sold.
        Follow with the required named-arguments product-name (--product)
        and sell-price (--price).""",
    )
    sell_parser.add_argument(
        "--product",
        required=True,
        help="Enter product name. Required argument.",
    )
    sell_parser.add_argument(
        "--selldate",
        required=True,
        default="today",
        type=valid_date,
        help="""Enter sell-date in format YYYY-MM-DD.""",
    )
    sell_parser.add_argument(
        "--price",
        required=True,
        type=float,
        help="""Enter price as float, will be rounded to two decimals.
        Required argument.""",
    )
    sell_parser.add_argument(
        "--quantity",
        required=True,
        default=1,
        type=int,
        help=""""Enter number of products sold on the same date,
        for the same price.""",
    )

    # --------------------------------------------------------------------------------------------------------------------

    # subparser for show-product command
    product_parser = subparsers.add_parser(
        "show-product",
        help="""Shows buy, sell and expiry data for product, by product id.""",
    )
    product_parser.add_argument(
        "product_id",
        type=int,
        help="Enter the id assigned to the product when bought (bought_id)",
    )

    # subparser for show-inventory command
    inventory_parser = subparsers.add_parser(
        "show-inventory",
        help="""Shows inventory on a given date.
        Enter inventory date as today, yesterday or as format YYYY-MM-DD'.
        The inventory can be exported to a csv or excel file,
        by using the flags --to-csv or --to-excel respectively""",
    )
    inventory_parser.add_argument(
        "date",
        type=valid_date,
        help="Enter inventory date as today, yesterday or as YYYY-MM-DD",
    )

    inventory_parser.add_argument(
        "--to-csv",
        action="store_true",
        # sets arg.csv as True: can be used to enable a feature
        help="Save inventory as csv-file",
    )
    inventory_parser.add_argument(
        "--to-excel",
        action="store_true",
        # sets arg.to-excel as True: can be used to enable a feature
        help="Save inventory as Excel spreadsheet",
    )

    # -------------------------------------------------------------------------------

    # subparser for report-total command
    report_total_parser = subparsers.add_parser(
        "report-total",
        help="""Report on total revenue or profit for a given day,
        month or year. Choose report-type (revenue or profit), then choose
        and set reporting period with named-arguments
        --date, --month or --year". If using --day, one can enter
        'today', 'yesterday' or a date in format 'YYYY-MM-DD """,
    )
    report_total_parser.add_argument(
        "type_of_report",  # argparse won't allow use of word 'report-type'
        choices=["revenue", "profit"],
        help="""Choose type of report.
        Then choose and set reporting period
        with named arguments --day, --month or --year""",
    )

    report_total_parser.add_argument(
        "--day",
        type=valid_date,
        help="""Enter report date as today,
        yesterday or as format YYYY-MM-DD, default = 'today""",
    )

    report_total_parser.add_argument(
        "--month",
        type=valid_month,
        help="Enter report month in format YYYY-MM"
    )
    report_total_parser.add_argument(
        "--year",
        type=valid_year,
        help="Enter the year for which you want a report in format YYYY"
    )

    # ---------------------------------------------------------------------------------

    # subparser for report-period command
    report_period = subparsers.add_parser(
        "report-period",
        help="""Plot daily revenue, profit or product-sales over a given month.
        Follow with report-type:
        choose from 'revenue', 'profit', 'revenue-profit' (both),
        or 'product-sales. Then enter month in format "YYYY-MM".
        If report-type is product-sales, use the named-argument --product
        to enter the product name. For all report types,
        you can choose to save the output data to csv or excel file,
        or to the plot to a  jpeg or pdf file with the following flags:
        --to-csv --to-excel, --to-jpeg and --to-pdf""",
    )

    report_period.add_argument(
        "type_of_report",  # argparse won't allow use of word 'report-type'
        choices=["revenue", "profit", "revenue-profit", "product-sales"],
        help="""Choose which type of report to show. Choose from:
        'revenue', 'profit', 'revenue-profit', 'product-sales'""",
    )

    report_period.add_argument(
        "report_month",
        type=valid_month,
        help="Enter report-month in format YYYY-MM"
    )

    report_period.add_argument(
        "--product", help="Enter the name of product you want to see sales of"
    )

    report_period.add_argument(
        "--to-csv",
        action="store_true",
        # sets arg.to-excel as True:  can be used to enable a feature
        help="Save plot data in csv file",
    )

    report_period.add_argument(
        "--to-excel",
        action="store_true",
        # sets arg.to-excel as True:  can be used to enable a feature
        help="Save plot data as table in as Excel spreadsheet",
    )

    report_period.add_argument(
        "--to-pdf",
        action="store_true",
        # sets arg.to-excel as True: can be used to enable a feature
        help="Save figure as PDF",
    )

    report_period.add_argument(
        "--to-jpeg",
        action="store_true",
        # sets arg.to-excel as True: can be used to enable a feature
        help="Save figure as JPEG image",
    )

    # -----------------------------------------------------------------------------------------------------

    # subparser for advance-date command
    change_parser = subparsers.add_parser(
        "change-date",
        help="""Move the date that this program has stored as 'today'
        forward or backward by given numbers of days.
        'Today' can be moved back using a negative number.""",
    )
    change_parser.add_argument(
        "no_of_days",
        type=int,
        help="Number of days the program's date will be moved to.",
    )

    # subparser for set-date command
    set_parser = subparsers.add_parser(
        "set-date",
        help="""Set the date that this program has stored as 'today'"""
    )
    set_parser.add_argument(
        "date_to_set",
        type=date.fromisoformat,
        help="Enter date in format YYYY-MM-DD",
    )
    # subparser for show-date command
    subparsers.add_parser("show-date",
                          help="Show date that this program use as 'today'")

    # ---------------------------------------------------------------------------------------------------------------------------

    return super_parser.parse_args()
