import csv
import random
from datetime import datetime, timedelta
import mysql.connector
import string

# Set the number of orders to generate
num_orders = 1000
field_length = 10

# Connecting to database
yokio_shop = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "Conduction@05",
    database = "yokio_shop"
)

cursor = yokio_shop.cursor()
cursor1 = yokio_shop.cursor()

# Selecting random customerid and product ids from their tables and adding inputting them as foreign keys in the orders table
query = "SELECT cus_id FROM customers"

cursor.execute(query)


# Fetch all rows of the query result
rows_cus = cursor.fetchall()
query1 = "SELECT productid FROM products"
cursor.execute(query1)
rows_prod = cursor.fetchall()

cus_ids = [''.join(random.choice(rows_cus)) for _ in range(num_orders)]

productids = [''.join(random.choice(rows_prod)) for _ in range(num_orders)]



# Generate a list of random order id's
order_ids = [''.join(random.choices(string.ascii_uppercase + string.digits, k=field_length)) for _ in range(num_orders)]

# Generate a list of random dates
min_date = datetime.today() - timedelta(days=365)
max_date = datetime.today()
dates = [min_date + timedelta(days=random.randint(0, 365)) for _ in range(num_orders)]

# Format the dates as strings in the 'yyyy-mm-dd' format
formatted_dates = [date.strftime('%Y-%m-%d') for date in dates]

# Zip the order id's and formatted dates together
orders = list(zip(order_ids, formatted_dates,cus_ids,productids))

# Write the orders to a CSV file
with open('orders.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['order-id', 'date-of-order','cus_id','productid'])
    for order in orders:
        writer.writerow(order)