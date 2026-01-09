''' Challenge: Birthday Messages Countdown

Objective: Employ the built-in datetime module and a custom-made module to calculate the remaining days until a specific date and trigger a randomized celebratory message.'''
import datetime, bday_messages

# 1. Get today's date
today = datetime.date.today()

# 2. Define your next birthday date (e.g., July 15 of this year)
next_birthday = datetime.date(2024, 7, 15)

# 3. Calculate the difference in days
days_away = (next_birthday - today).days

# 4. Check if today is your birthday
if today == next_birthday:
    print(bday_messages.random_message)
else:
      print(f"My next birthday is {days_away} days away!")

