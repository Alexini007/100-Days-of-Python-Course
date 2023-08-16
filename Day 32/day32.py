import smtplib
import pandas
import datetime as dt

birthdays = pandas.read_csv("birthdays.csv")
print(birthdays["name"][0])

my_email = "**"
password = "**"

today = dt.datetime.today().day
print(today)

# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="**", msg="Subject: Test\n\nlets test")