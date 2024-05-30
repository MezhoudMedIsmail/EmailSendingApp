import smtplib
import datetime as dt
import random

my_email = "ismailmezhoud2@gmail.com"
password = "*********" #your generated password from App passwwords

now = dt.datetime.now()  # current date and time
day_of_week = now.weekday()  # current day of the week

if day_of_week == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="***THE EMAIL YOU WANT TO SEND TO***",
            msg=f"Subject:Hello\n\n {quote} ."
        )





