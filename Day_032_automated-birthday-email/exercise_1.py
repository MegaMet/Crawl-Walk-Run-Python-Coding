EMAIL = "example@email.com"
PASSWORD = "password"

import smtplib


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user= EMAIL, password= PASSWORD)
    connection.sendmail(from_addr= EMAIL,
                        to_addrs= "sample@email.com",
                        msg= "Subject:Hello\n\nThis is a test")
