import sys
import csv
from pathlib import Path
from datetime import datetime

BOUGHT_PATH = Path("bought.csv")
SOLD_PATH = Path("sold.csv")

##############################################################################
# functions logging bought and sold products into csv-files:


def create_csv(path, headings):
    with open(path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headings)
        print(f"Created {path}")


def buy_product(
    product_name, buy_date, buy_price, expiration_date, quantity, b_path=BOUGHT_PATH
):
    # create bought.csv if it doesn't exists and add header
    if not b_path.is_file():
        create_csv(
            b_path,
            [
                "id",
                "product",
                "buy_date",
                "buy_price",
                "expiration",
                "quantity",
            ],
        )

    with open(b_path, "r+", newline="") as file:
        reader = csv.reader(file)
        writer = csv.writer(file)

        next(reader)  # skip column names
        try:
            # compare 'int' version of each id (key=lambda row: int(row[0]),
            # then choose the row with largest id (max),
            # then obtain id (row[0]), convert to integer and add 1
            id = int(max(reader, key=lambda row: int(row[0]))[0]) + 1  #
        except ValueError:  # if file does not have rows yet, set id to 1
            id = 1

        if id >= 1:
            writer.writerow(
                [
                    id,
                    product_name,
                    buy_date,
                    round(buy_price, 2),
                    expiration_date,
                    quantity,
                ]
            )
            print(
                f"""Logged {product_name}
            in 'bought.csv' with product-id {id}"""
            )
            id += 1


def sell_product(
    product_name,
    sell_date,
    sell_price,
    s_quantity,
    b_path=BOUGHT_PATH,
    s_path=SOLD_PATH,
):
    # create a file if it does not exists and add headers
    if not s_path.is_file():
        create_csv(s_path, ["id", "bought_id", "sell_date", "sell_price", "quantity"])

    # check if item is in store and assign bought_id to sold item
    with open(s_path, "r+", newline="") as sold_file, open(
        b_path, "r", newline=""
    ) as bought_file:
        sold_reader = csv.reader(sold_file)
        bought_reader = csv.reader(bought_file)
        sold_writer = csv.writer(sold_file)

        number_of_sold_products = s_quantity
        if number_of_sold_products >= 1:
            for row in sold_reader:
                assigned_ids = [row[1] for row in sold_reader]

            bought_id = None
            bought_quantity = None

            for row in bought_reader:
                if (
                    row[1] == product_name
                    and row[0] not in assigned_ids
                    and datetime.strptime(row[4], "%Y-%m-%d").date() >= sell_date
                    and row[5] >= s_quantity
                ):
                    bought_id = row[0]
                    bought_quantity = row[5]
                    break
            if bought_id is None:
                if s_quantity >= bought_quantity:
                    print("Error: product not in stock")
                elif s_quantity > bought_quantity:
                    print("Error: remaining product(s) not in stock")
                sys.exit()

            # retrieve highest/last id in sold.csv
            sold_file.seek(0)
            next(sold_reader)
            try:
                id = int(max(sold_reader, key=lambda row: int(row[0]))[0]) + 1
            except ValueError:
                id = 1

            # append product with writerow() to sold.csv
            sold_writer.writerow(
                [
                    id,
                    bought_id,
                    sell_date,
                    sell_price,
                    s_quantity,
                ]
            )
            print(
                f"""Added {product_name} to 'sold.csv'
            with sold-id {id} and bought-id {bought_id}"""
            )
            int(bought_quantity) - int(number_of_sold_products)
