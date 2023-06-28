# SuperPy

What I would want to add to the programm is a user interface. I do not think a CLI programm would work in retail.
I learned a lot about transfering data in differnt files. But I would not say I liked the assignment Due to lack of user interface.

for the next assignemnt I will also add a virtual environment.

The technical aspects I like in this assignment are:

**1. The collection class Stock**

Superpy contains the classes Product and Stock. The class Stock has a 'get_product' method which loads product data from the csv-files and creates a product instance for each bought product and updates it with information from the the sold-file.

The collection class Stock then loads all these Product instances into an instance list, or 'stock'. Each time a user needs a report, such as profit or product-sales, class methods specific to the type of report requested can be invoked on an up-to-date stock.

The advantage of structuring the code in this way, is that the class Stock provides a data structure which is better geared towards generating reports, than extracting the specific data directly from the two 'bought' and 'sold' csv-files everytime a report is queried.

**2. Using differnt libaries**
Using Panda's and other libaries to plot the reports and create nice profit overviews en reports for the user.
