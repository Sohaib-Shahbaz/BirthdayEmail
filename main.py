import datetime as dt
import pandas as pd
import random
import smtplib

MY_EMAIL = "<EMAIL>"
MY_PASSWORD = "<APP PASSWORD>"
now = dt.datetime.now()
month = now.month
day = now.day
today=(month, day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(row["month"], row["day"]): row for (index, row) in data.iterrows()}

if today in birthdays_dict:
    print("Birthday Match Found")
    print(birthdays_dict[today])

    birthday_person = birthdays_dict[today]
    person_name = birthday_person["name"]
    person_email = birthday_person["email"]

    template_num = random.randint(1, 3)
    with open(f"letter_templates/letter_{template_num}.txt", "r") as letter_file:
        letter = letter_file.read()

    letter = letter.replace("[NAME]", person_name)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person_email,
            msg=f"Subject:HAPPY BIRTHDAY!\n\n{letter}"
        )
else:
    print("Birthday Not Found")
