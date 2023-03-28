import datetime as dt

# creating an object: current time.
now = dt.datetime.now()
print(f"Now is: {now}")
year = now.year
month = now.month
day = now.day
date = now.date()
weekday = now.weekday()

# etcetra there are too many things.

print(f"Now year is: {year}")
print(f"Now month is: {month}")
print(f"Now day is: {day}")
print(f"Now date is: {date}")
print(f"Current weekday is: {weekday}")  # Remember: computer starts from zero so,
# if there is monday then week day will be 0.

# Storing date of birth:
dob = dt.datetime(year=2002, month=12, day=28)
print(f"Date of birth is: {dob}")
