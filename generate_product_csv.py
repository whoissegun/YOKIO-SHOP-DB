import csv
import random
import string
from lists_of_prods import *

# Set the number of lines to generate
num_lines = 1000

# Set the number of characters in each field
field_length = 10

# Open a new CSV file for writing
with open('products.csv', 'w', newline='') as csvfile:
  # Create a CSV writer object
  writer = csv.writer(csvfile)

  # Write the header row
  writer.writerow(['productid', 'product name', 'product supplier', 'price', 'quantity', 'category'])

  # Generate and write the random lines
  for i in range(num_lines):
    # Generate a random product ID
    productid = ''.join(random.choices(string.ascii_uppercase + string.digits, k=field_length))

    # Generate a random product name
    product_names = nike_products+tommy_hilfiger_clothing+infinix_devices+tecno_devices+macbook_models+asus_devices+google_devices+samsung_devices+iphones+adidas_products+balenciaga_products+microsoft_products+coca_cola_brands+alienware_products+bose_products+airpods_products+gucci_products+sony_products+hp_products+rolex_products+prada_products

    product_name = random.choice(product_names)

    # Generate a random supplier name
    if product_name in nike_products:
        supplier_name = 'Nike'
    elif product_name in tommy_hilfiger_clothing:
        supplier_name = 'Tommy Hilfiger'
    elif product_name in infinix_devices:
        supplier_name = 'Infinix'
    elif product_name in tecno_devices:
        supplier_name = 'Tecno'
    elif product_name in macbook_models or product_name in airpods_products or product_name in iphones:
        supplier_name = 'Apple'
    elif product_name in asus_devices:
        supplier_name = 'Asus'
    elif product_name in google_devices:
        supplier_name = 'Google'
    elif product_name in samsung_devices:
        supplier_name = 'Samsung'
    elif product_name in adidas_products:
        supplier_name = 'Adidas'
    elif product_name in balenciaga_products:
        supplier_name = 'Balenciaga'
    elif product_name in microsoft_products:
        supplier_name = 'Microsoft'
    elif product_name in coca_cola_brands:
        supplier_name = 'Coca Cola'
    elif product_name in alienware_products:
        supplier_name = 'Alienware'
    elif product_name in bose_products:
        supplier_name = 'Bose'
    elif product_name in gucci_products:
        supplier_name = 'Gucci'
    elif product_name in sony_products:
        supplier_name = 'Sony'
    elif product_name in hp_products:
        supplier_name = 'HP'
    elif product_name in rolex_products:
        supplier_name = 'Rolex'
    else:
        supplier_name = 'Prada'

    # Generate a random price
    rnd = random.uniform(100, 1000)
    price = round(rnd, 2)

    # Generate a random quantity
    quantity = random.randint(0, 700)

    # Assigning a category
    if product_name in nike_products:
        category = 'Clothing'
    elif product_name in tommy_hilfiger_clothing:
        category = 'Clothing'
    elif product_name in infinix_devices:
        category = 'Electronics'
    elif product_name in tecno_devices:
        category = 'Electronics'
    elif product_name in macbook_models or product_name in airpods_products or product_name in iphones:
        category = 'Electronics'
    elif product_name in asus_devices:
        category = 'Electronics'
    elif product_name in google_devices:
        category = 'Electronics'
    elif product_name in samsung_devices:
        category = 'Electronics'
    elif product_name in adidas_products:
        category = 'Clothing'
    elif product_name in balenciaga_products:
        category = 'Clothing'
    elif product_name in microsoft_products:
        category = 'Electronics'
    elif product_name in coca_cola_brands:
        category = 'Food'
    elif product_name in alienware_products:
        category = 'Electronics'
    elif product_name in bose_products:
        category = 'Electronics'
    elif product_name in gucci_products:
        category = 'Clothing'
    elif product_name in sony_products:
        category = 'Electronics'
    elif product_name in hp_products:
        category = 'Electronics'
    elif product_name in rolex_products:
        category = 'Clothing'
    else:
        category = 'Clothing'

    # Write the line to the CSV file
    writer.writerow([productid, product_name, supplier_name, price, quantity, category])
