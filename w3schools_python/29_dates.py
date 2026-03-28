# Python Dates

import datetime

# Current date and time
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)

# Create specific date
birthday = datetime.date(2000, 5, 15)
print(birthday)

# Format date
print(now.strftime("%d/%m/%Y %H:%M"))
print(now.strftime("%A, %B %d, %Y"))

# Date arithmetic
tomorrow = now + datetime.timedelta(days=1)
print("Tomorrow:", tomorrow.date())
