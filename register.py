#!/usr/bin/python3
import cgi

# Function to save user data to a text file
def save_user_info(name, email, password):
    with open("registered_users.txt", "a") as file:
        file.write(f"{name},{email},{password}\n")

# Print HTTP header
print("Content-type: text/html\n\n")

# Get form data
form = cgi.FieldStorage()

# Extract form values
name = form.getvalue("name")
email = form.getvalue("email")
password = form.getvalue("password")

# Save user info to file
if name and email and password:
    if not '@nyu.edu' in email:
        print("<h2>Sorry only nyu students are allowed on this site!</h2>")
        print("<a href='index.html'><button>Go Back</button></a>")
    else:
        save_user_info(name, email, password)
        print("<h2>Registration Successful!</h2>")
        print("<a href='index.html'><button>Login</button></a>")
else:
    print("<h2>Registration Failed. Please fill in all fields.</h2>")
