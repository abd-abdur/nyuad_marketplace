#!/usr/bin/env python3
import cgi
import html

def save_review(name, review, email):
    with open('reviews.txt', 'a') as file:
        file.write(f"{name},{email},{review}\n")

def main():
    print("Content-type: text/html\n")
    form = cgi.FieldStorage()
    name = form.getvalue('customer_name')
    review = form.getvalue('review_text')
    email = form.getvalue('customer_email', 'No Email Provided')

    # Escape HTML special characters to prevent XSS attacks
    name = html.escape(name)
    review = html.escape(review)
    email = html.escape(email)

    # Save the review
    save_review(name, review, email)

    # Generate the response with enhanced styling
    print(f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="css/style.css">
        <title>Review Submitted</title>
        <style>
            body {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f3e5f5; /* Light purple background */
            }}
            .thank-you-container {{
                text-align: center;
                padding: 20px;
                border-radius: 8px;
                background: #ffffff;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                width: 90%;
                max-width: 600px;
            }}
            h1 {{
                color: #913684; /* Deep purple */
            }}
            .btn {{
                background-color: #f3a2ff; /* Light pink */
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                text-transform: uppercase;
                transition: background-color 0.3s ease;
            }}
            .btn:hover {{
                background-color: #e191f7; /* Slightly darker pink */
                cursor: pointer;
            }}
        </style>
    </head>
    <body>
        <div class="thank-you-container">
            <h1>Thank you for your feedback, {name}!</h1>
            <p>Your review is very important to us.</p>
            <a href="review.html" class="btn">Return to Reviews</a>
        </div>
    </body>
    </html>""")

if __name__ == "__main__":
    main()
