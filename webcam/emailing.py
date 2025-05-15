import mimetypes
import smtplib
from email.message import EmailMessage

# Use your 16-character Gmail App Password (NOT your regular password)
PASSWORD = "zksrqbxzqoqytcjd"
SENDER = "vishal.work47@gmail.com"
RECEIVER = "vishal.work47@gmail.com"

def send_email(image_path):
    email_msg = EmailMessage()
    email_msg["Subject"] = "New customer showed up!"
    email_msg["From"] = SENDER
    email_msg["To"] = RECEIVER
    email_msg.set_content("Hey, we just saw a new customer!")

    # Read the image content
    with open(image_path, "rb") as file:
        content = file.read()

    # Guess the MIME type
    mime_type, _ = mimetypes.guess_type(image_path)
    if mime_type is None:
        maintype, subtype = "application", "octet-stream"
    else:
        maintype, subtype = mime_type.split("/")

    # Attach the image
    email_msg.add_attachment(content, maintype=maintype, subtype=subtype, filename=image_path)

    # Send the email
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.send_message(email_msg)
    gmail.quit()

if __name__ == "__main__":
    send_email(image_path="images/19.png")