# Birthday Email Wisher 

A small Python script that checks birthdays.csv each day, picks a random birthday letter template, personalises it with the recipient’s name, and sends it via Gmail SMTP when a birthday matches today’s date.

## Features

Reads birthdays from a CSV file

Matches birthdays using today’s (month, day)

Randomly selects one of 3 letter templates

Replaces [NAME] with the person’s name

Sends the email automatically using Gmail SMTP (TLS / port 587)

```
Project Structure
birthday-email-wisher/
├─ main.py
├─ birthdays.csv
└─ letter_templates/
   ├─ letter_1.txt
   ├─ letter_2.txt
   └─ letter_3.txt
```

CSV Format (birthdays.csv)

Your file must include these columns:

name,email,year,month,day
Angela,angela@email.com,1995,12,24
John,john@email.com,2000,2,12


## Letter Templates

Each template should include [NAME] where the name should go, e.g.

Dear [NAME],

Happy Birthday! 🎉
Have an amazing day!

From,
Sohaib

## Setup
1) Install dependencies
```
pip install pandas
```

2) Add your email details

In main.py replace these placeholders:

```
MY_EMAIL = "<EMAIL>"
MY_PASSWORD = "<APP PASSWORD>"
```

For Gmail, use an App Password (recommended) rather than your normal password.

Run
```
python main.py
```

If a birthday matches today’s date, it will send an email and print:
```
Birthday Match Found
```
Otherwise it prints:
```
Birthday Not Found
```

## Customisation Ideas

Add more templates (e.g. letter_4.txt, letter_5.txt)

Support multiple birthdays on the same day

Schedule it to run daily using Task Scheduler (Windows) / cron (macOS/Linux)

## License

This project is free to use and modify for learning and personal projects.