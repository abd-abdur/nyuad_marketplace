#!/usr/bin/python3

import cgi
import html

print("Content-Type: text/html\n\n")

def get_next_id(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            last_line = lines[-1]
            last_id = int(last_line.split(',')[0])
            return last_id + 1
    except (FileNotFoundError, IndexError):
        return 1

def save_product_info(product_name, description, price, contact, image_url, filename="products.txt"):
    try:
        id = get_next_id(filename)
        with open(filename, "a") as file:
            file.write(f"{id},{product_name},{description},{price},{contact}, {image_url}\n")
        return True
    except IOError as e:
        return False

def html_head(title="Add Product"):
    print(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        <link href='/css/style.css' rel='stylesheet'> 
    </head>
    <body>
    """)

def html_footer():
    print('''
    </body>
    </html>
    ''')

def main():
    form = cgi.FieldStorage()

    # Sanitize inputs by escaping special HTML characters
    product_name = html.escape(form.getvalue("product_name", ""))
    description = html.escape(form.getvalue("description", ""))
    price = html.escape(form.getvalue("price", ""))
    contact = html.escape(form.getvalue("contact", ""))
    image_url = html.escape(form.getvalue("image_url", ""))

    html_head("Product Addition Confirmation")

    if product_name and description and price and contact and image_url:
        if save_product_info(product_name, description, price, contact, image_url):
            print("<h2>Product Added Successfully!</h2>")
            print("<div>")
            print(f"<p>Name: {product_name}</p>")
            print(f"<p>Description: {description}</p>")
            print(f"<p>Price: {price}</p>")
            print(f"<p>contact: {contact}</p>")
            print(f"<p><img src='{image_url}' alt='Product Image'></p>")
            print("</div>")
        else:
            print("<h2>Failed to save product. There was a problem writing to the file.</h2>")
    else:
        print("<h2>Failed to add product. Please ensure all fields are filled.</h2>")

    print("<a href='all_products.py'>View All Products</a>")
    html_footer()

main()
