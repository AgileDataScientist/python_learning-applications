import smtplib
import ssl

from email.message import EmailMessage

# Hard-code subject and body of email
subject = "Email from Python"
body = "This is a test from python!"

# Enter the email address and passwords
sender_email = input("Enter a sender email: ")
password = input("Enter a password: ")

# Set Receiver email to sender email
receiver_email = sender_email

# Substantiate an instance of Email Message
message = EmailMessage()

# Populate the fields of the email message
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)


html = f"""
<html>
    <body>
        <h1> {subject} </h1>
        <p>  {body}    </p>
    </body>
</html>
"""
message.add_alternative(html, subtype="html")

context = ssl.create_default_context()
print("Sending email.")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Sent email.")
