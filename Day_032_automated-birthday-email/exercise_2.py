import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()

print(type(year))
print(type(now))

date_of_birth =dt.datetime(year=1987, month=1, day=1)
print(date_of_birth)