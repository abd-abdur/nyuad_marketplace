#!/usr/bin/python3
import cgi
import cgitb; cgitb.enable()  # Enables detailed error reporting

def save_user_info(name, email, password):
    with open("registered_users.txt", "a") as file:
        file.write(f"{name},{email},{password}\n")

print("Content-type: text/html\n\n")
form = cgi.FieldStorage()

name = form.getvalue("name")
email = form.getvalue("email")
password = form.getvalue("password")

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register - NYUAD Marketplace</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .header_section h1, .footer_section p {
            text-align: center;
            padding: 10px;
        }
        form {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        input[type="text"], input[type="email"], input[type="password"] {
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            padding: 10px;
            color: white;
            background-color: #007BFF;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        footer {
            background-color: #343a40;
            color: #ffffff;
            position: absolute;
            bottom: 0;
            width: 100%;
            padding: 20px 0;
        }
    </style>
</head>
<body>

<div class="container">
    <header class="header_section">
        <h1>NYUAD Marketplace - Registration</h1>
        <nav>
        </nav>
    </header>

    <section class="mt-5">
        <form id="register-form" action="register.py" method="post" class="form-signin">
""")

if name and email and password:
    if '@nyu.edu' not in email:
        print("<h2>Sorry, only NYU students are allowed on this site!</h2>")
        print("<a href='index.html'><button type='button'>Go Back</button></a>")
    else:
        save_user_info(name, email, password)
        print("<h2>Registration Successful!</h2>")
        print("<a href='homepage.html'><button type='button'>Home</button></a>")
else:
    print("<h2>Registration Failed. Please fill in all fields.</h2>")


print("""
        </form>
    </section>
</div>

<footer class="footer_section">
    <p>&copy; 2024 All Rights Reserved By NYUAD Marketplace</p>
</footer>
</body>
</html>
""")
