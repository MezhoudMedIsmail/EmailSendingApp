import smtplib

# Create a connection to the SMTP server
my_email = "ismailmezhoud2@gmail.com"
password = "kcoa lvch krjd dpvy"

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="mohamedismail.mezhoud@esprit.tn",
        msg="Subject:Hello\n\nThis is my email ."
    )

