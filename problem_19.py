import datetime

years = range(1901, 2000+1)
months = range(1, 12+1)

num_sundays = 0
for year in years:
    for month in months:
        weekday = datetime.date(year, month, 1).weekday()
        num_sundays += 1 if weekday == 6 else 0

print(num_sundays)