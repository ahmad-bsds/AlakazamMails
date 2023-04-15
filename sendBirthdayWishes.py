import random
from mailSendSystem import send_mail
import datetime as dt
import pandas as pd

# What today date is.
now = dt.datetime.now()
today_date = (12, 28)

# reading birthday file.
data = pd.read_csv('birthdays.csv')
# Getting most resent birthday.
birthday_dict = {(row['Month'], row['Day']): row for (index, row) in data.iterrows()}  # check iter rows not items.
print(birthday_dict)

# we used index, or we might write _ for just unpack.
# /HERE KEY DIFFERENT BECAUSE WE CANT UNPACK IT SO MAKE IT A KEY.

def send_wish(email, password):
    # Check if today is same as birthday:
    for birthdays in birthday_dict:
        print(birthdays)
        if today_date == birthdays:
            birthday_person = birthday_dict[today_date]  # birthday_dict[key], All data of birthday person or,
            # row in dictionary comprehension.
            file_path = f"birthdayMsg{random.randint(1, 3)}.txt"
            # Open a file and getting random wishes letter.
            with open(file_path) as msg:
                wishes = msg.read()
                wishes = wishes.replace('[Name]', birthday_person['Name'])
            send_mail(email, password, 'Happy Birthday!!', wishes, birthday_person['E-Mail'])
            print('Mail Sent successfully!!')

# use pythonanywhere.com to run code on daily basis.
