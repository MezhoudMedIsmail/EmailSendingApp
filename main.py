import smtplib
import datetime as dt
import random

my_email = "ismailmezhoud2@gmail.com"
password = "kcoa lvch krjd dpvy"

now = dt.datetime.now()  # current date and time
day_of_week = now.weekday()  # current day of the week

if day_of_week == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="mohamedismail.mezhoud@esprit.tn",
            msg=f"Subject:Hello\n\n {quote} ."
        )





