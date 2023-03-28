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
