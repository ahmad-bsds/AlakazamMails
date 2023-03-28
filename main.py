# Send Email using python code:
# SMTP (Simple Mail Transfer Protocol) module helps us to send email.
# library name is smtplib
EMAIL = 'newera0176@gmail.com'
PASS = 'ejtucwcokpcmzlwf'  # Special password created in --> Google manage my account --> search for App Password then,
# create a password.
import smtplib


def send_mail(email, password, subject, massege, receiver):
    # Establishing a connection.
    with smtplib.SMTP('smtp.gmail.com') as connection:
        # Security layer.
        connection.starttls()
        # Logining to email.
        connection.login(user=email, password=password)
        # Sending mail.
        connection.sendmail(
            from_addr=email,  # address from send.
            to_addrs=receiver,  # address where send.
            msg=f"""Subject: {subject}\n\n 
            {massege}.
            """
        )


# Send mail on a specific weekday.
import datetime as dt

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    send_mail(EMAIL, PASS, 'Monday Motivation', 'If not not now, then when!', 'muhammadahmad01756@gmail.com')
    print("Mail Sent!!")
