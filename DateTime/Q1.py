# 20. Questions:------

import datetime

# 1. Write a Python script to display the various Date Time formats.
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week

today = datetime.date.today()
print("Current date: ", today)
print("Current time: ", today.ctime())
print("Current year: ", today.year)
print("Current month: ", today.month)
print("Week number of the year: ", today.strftime("%W"))
print("Weekday of the week: ", today.weekday())
print("Day of year: ", today.strftime("%j"))
print("Day of the month: ", today.day)
print("Day of Week: ", today.strftime("%A"))


# 2. Write a Python program to determine whether a given year is a leap year.
def LeepYear(yr):
    if yr % 4 or yr % 400 == 0:
        print("{} is Leep Year.".format(yr))
    else:
        print("{} is not Leep Year.".format(yr))

LeepYear(2020)
LeepYear(2000)
LeepYear(2021)
LeepYear(2032)
LeepYear(2035)
LeepYear(1900)


# 3. Write a Python program to convert a string to datetime.
from datetime import datetime
date_object = datetime.strptime('Jul 1 2014 2:43PM', '%b %d %Y %I:%M%p')
print(date_object)


# 4. Write a Python program to get the current time in Python.
print("Current Time: ", datetime.datetime.now().time())


# 5. Write a Python program to subtract five days from current date.
def Subtract(day):
    tdel = datetime.timedelta(days=day)
    cdate = datetime.date.today()
    print("5 day before: {}".format(cdate - tdel))
Subtract(5)


# 6. Write a Python program to convert unix timestamp string to readable date.
def Timestamp(n):
    ddt = datetime.datetime.fromtimestamp(n).strftime('%Y-%m-%d %H:%M:%S')
    print("Unix Timestamp: ", ddt)
Timestamp(1284105682)


# 7. Write a Python program to print yesterday, today, tomorrow.
def Print(n):
    today = datetime.datetime.today()
    tdelta = datetime.timedelta(days=n)

    print(f"Today: {today.date()}")
    print(f"Yesterday: {(today - tdelta).date()}")
    print(f"Tomorrow: {(today + tdelta).date()}")
Print(1)


# 8. Write a Python program to convert the date to datetime (midnight of the date) in Python.
from datetime import date
from datetime import datetime
dt = date.today()
print(datetime.combine(dt, datetime.min.time()))


# 9. Write a Python program to print next 5 days starting from today.
def Next(n):
    today = datetime.datetime.today()
    for i in range(n):
        print(f"Day{i} date: {(today + (datetime.timedelta(days=i))).date()}")

Next(5)


# 10. Write a Python program to add 5 seconds with the current time.
x= datetime.datetime.now()
y = x + datetime.timedelta(0,5)
print(x.time())
print(y.time())


# 11. Write a Python program to get week number.
def WeekNumber(yr, mn, dy):
    print("Week number is: ", datetime.date(yr, mn, dy).isocalendar()[1])
WeekNumber(2015, 6, 16)
WeekNumber(2021, 1, 20)


# 12. Write a Python program to select all the Sundays of a specified year. 
def Select_Sundays(yr):
    dt = datetime.date(yr, 1, 1)
    dt += datetime.timedelta(days= 6 - dt.weekday())
    while dt.year == yr:
        yield dt
        dt += datetime.timedelta(days = 7)
        
for s in Select_Sundays(2021):
    print(s)


# 13. Write a Python program to drop microseconds from datetime.
print(datetime.datetime.today().replace(microsecond=0))


# 14. Write a Python program to get days between two dates.
a = datetime.date(2000, 2, 28)
b = datetime.date(2001, 2, 28)
print("Days: ", b - a)


# 15. Write a Python program to get the date of the last Tuesday.
today = datetime.date.today()
offset = (today.weekday() - 1) % 7
last_tuesday = today - datetime.timedelta(days=offset)
print("Last Tuesday: ", last_tuesday)


# 16. Write a Python program to test the third Tuesday of a month.
def is_third_Tuesday(yr, mn, dy):
    dt = datetime.date(yr, mn, dy)
    if dt.weekday() == 1 and 14 < dt.day < 22:
        print("True")
    else:
        print("False")

is_third_Tuesday(2021, 1, 2)
is_third_Tuesday(2021, 1, 19)
is_third_Tuesday(2021, 1, 28)
is_third_Tuesday(2021, 2, 12)


# 17. Write a Python program to get the last day of a specified year and month.
def Lastday(yr, mn):
    import calendar
    print(calendar.monthrange(yr, mn)[1])

Lastday(2021, 1)
Lastday(2021, 2)
Lastday(2021, 3)


# 18. Write a Python program to get the number of days of a given month and year.
def CurrentDays(yr, mn):
    from calendar import monthrange
    print(monthrange(yr, mn))

    import calendar
    print(calendar.monthrange(yr, mn)[1])

CurrentDays(2021, 2)


# 19.  Write a Python program to add a month with a specified date.
from datetime import date, timedelta
import calendar
start_date = date(2014, 12, 25)
days_in_month = calendar.monthrange(start_date.year, start_date.month)[1]
print(start_date + timedelta(days=days_in_month))


# 20. Write a Python program to count the number of Monday of the 1st day 
#     of the month from 2015 to 2016.
from datetime import datetime
monday1 = 0
months = range(1,13)
for year in range(2020, 2021):
    for month in months:
        if datetime(year, month, 1).weekday() == 0:
            monday1 += 1
print(monday1)
