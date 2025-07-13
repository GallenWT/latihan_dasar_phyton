import datetime

def count_age(birthday):
    today = datetime.date.today()
    age_year = today.year - birthday.year
    age_month = today.month - birthday.month
    age_date = today.day - birthday.day

    if age_date < 0:
        age_month -= 1
        month_before = today.month - 1 or 12
        year_before = today.year if today.month != 1 else today.year - 1
        day_in_month = (datetime.date(today.year, today.month, 1) - datetime.date(year_before, month_before, 1)).days
        age_date += day_in_month

    if age_month < 0:
        age_year -= 1
        age_month += 12

    return age_year, age_month, age_date

def days_to_birthday(birthday):
    today = datetime.date.today()
    next_birthday = datetime.date(today.year, birthday.month, birthday.day)

    if next_birthday < today:
        next_birthday = datetime.date(today.year + 1, birthday.month, birthday.day)

    days_left = (next_birthday - today).days
    return days_left


input_date = input("Input your birthday (format: YYYY-MM-DD): ")

try:
    birthday = datetime.datetime.strptime(input_date, "%Y-%m-%d").date()

    age_year, age_month, age_date = count_age(birthday)
    days_left = days_to_birthday(birthday)

    print(f"\n🗓️ Current Age: {age_year} years, {age_month} months, {age_date} days.")
    print(f"🎉 Your next birthday in {days_left} days.")

except ValueError:
    print("⚠️ Date format not valid. Use YYYY-MM-DD format.")