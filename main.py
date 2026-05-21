import smtplib

# Your Gmail
email_sender = "yourgmail@gmail.com"

# App Password
email_password = "your_app_password"

# Receiver Email
email_receiver = "receiver@gmail.com"

# Subject
subject = "Automation Email"

# Body
body = """
Hello,

This email was sent automatically using Python.

Thank You
"""

# Create Message
message = f"Subject: {subject}\n\n{body}"

try:
    # Connect to Gmail Server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # Login
    server.login(email_sender, email_password)

    # Send Email
    server.sendmail(email_sender, email_receiver, message)

    print("Email Sent Successfully!")

    # Close Server
    server.quit()

except Exception as e:
    print("Error:", e)
