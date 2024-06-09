import os
import random
import pandas
import smtplib
import datetime as dt

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

now = dt.datetime.now()
todays_date = (now.day, now.month)

birthday_data = pandas.read_csv("birthdays.csv")
birthday_dict = {(row["day"], row["month"]): row for (i, row) in birthday_data.iterrows()}

if (todays_date in birthday_dict):
    birthday_target = birthday_dict[todays_date]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_target["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=birthday_target["email"],
                            msg=f"Subject:Happy Birth!\n\n{contents}")


