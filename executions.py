import mysql.connector
import gc
from instantiate_from_csv import *
import os
db_password = os.getenv("db_password")
yokio_shop = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = db_password,
    database = "yokio_shop"
)

cursor = yokio_shop.cursor()

def insert_cus_records():
    Customers.csv_instantiate('people-1000.csv')
    for obj in gc.get_objects():
        if isinstance(obj,Customers):
            cursor.execute("INSERT INTO customers VALUES(%s,%s,%s,%s,%s)",(obj.cus_id,obj.f_name,obj.l_name,obj.email,obj.phone))

def insert_prod_records():
    Products.csv_instantiate('products.csv')
    for obj in gc.get_objects():
        if isinstance(obj,Products):
            cursor.execute("INSERT INTO products VALUES(%s,%s,%s,%s,%s,%s)",(obj.prod_id,obj.prod_name,obj.prod_supplier,obj.price,obj.quantity,obj.category))
def insert_order_records():
    Orders.csv_instantiate('orders.csv')
    for obj in gc.get_objects():
        if isinstance(obj,Orders):
            cursor.execute("INSERT INTO orders VALUES(%s,%s,%s,%s)",(obj.order_id,obj.date_of_order,obj.cus_id,obj.productid))
def delete_cus_records(cus_id):
    cursor.execute(f"DELETE FROM customers WHERE cus_id = %s",(cus_id,))

def delete_prod_records(productid):
    cursor.execute(f"DELETE FROM products WHERE productid = %s",(productid,))

def delete_orders_records(order_id):
    cursor.execute(f"DELETE FROM orders WHERE order_id = %s",(order_id,))



yokio_shop.commit()