d1 = 10
m1 = 2
y1 = 2014

d2 = 10
m2 = 3
y2 = 2015

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    return month_days[month - 1]

def total_days(day, month, year):
    days = day
    for y in range(1, year):
        days += 366 if is_leap(y) else 365
    for m in range(1, month):
        days += days_in_month(m, year)
    return days

def days_between_dates(d1, m1, y1, d2, m2, y2):
    return abs(total_days(d1, m1, y1) - total_days(d2, m2, y2))

# Example Usage:
day1, month1, year1 = 10, 3, 2024
day2, month2, year2 = 28, 3, 2025

print("Number of days between the dates:", days_between_dates(day1, month1, year1, day2, month2, year2))
