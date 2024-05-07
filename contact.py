#!/usr/bin/python3
import cgi
import cgitb

# Enable debugging
cgitb.enable()

# Print HTTP header and message card
print("Content-type: text/html\n")

def generate_message_card(name, email, phone, message):
    # Save contact form data to a file
    
    with open("contact.txt", "a") as file:
        file.write(f"{name},{email},{phone},{message}\n")
        
    return f"""
    <style>
        .card {{
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            font-family: Arial, sans-serif;
        }}
        .card h2 {{
            color: #333;
        }}
        .card p {{
            color: #666;
        }}
        .card a {{
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
             background-color: #fff;
            color: #b20fdb;
            outline: 1px solid #b20fdb;
        }}
        .card a:hover {{
            color: #fff;
            background-color: #b20fdb;
        }}
    </style>
    <div class="card">
        <h2>Thank you, {name}!</h2>
        <p>We have received your message and will get back to you soon.</p>
        <p><strong>Your Message:</strong></p>
        <p>{message}</p>
        <a href="homepage.html">Go back to homepage</a>
    </div>
    """
    
# Get form data
form = cgi.FieldStorage()

# Extract form values
name = form["name"].value
email = form["email"].value
phone = form["phone"].value
message = form["message"].value

# Generate message card
message_card = generate_message_card(name, email, phone, message)


print(message_card)