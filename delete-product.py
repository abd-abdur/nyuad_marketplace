#!/usr/bin/python3

import cgi
import cgitb; cgitb.enable()
import os

print("Content-Type: text/html\n\n") 
form = cgi.FieldStorage()
product_id = form.getvalue('id')

def delete_product(filename, product_id):
    # Read the products, except the one to delete
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            if not line.startswith(product_id):
                file.write(line)

if product_id:
    delete_product('products.txt', product_id)

print('<p>Product has been deleted. <a href="all_products.py">Return to all products.</a></p>')
