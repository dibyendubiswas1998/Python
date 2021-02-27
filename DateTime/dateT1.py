import datetime


dt = datetime.date(2017, 7, 20)
print(dt)


# Today Year, day, weekday, ctime:--------
today = datetime.date.today()
print(today)
print(today.year)
print(today.day)
print(today.weekday())
print(today.isoweekday())
print(today.ctime())


# Get the date after/ before 10 days:------
tdelt = datetime.timedelta(days=10)
print("after 10 days: {}".format(today + tdelt))
print("before 10 days: {}".format(today - tdelt))


# how many day's/ second left from today:---
bday = datetime.date(2021, 3, 12)
print("Day's Left: {}".format(bday - today))
print("Day's Left: {} days".format((bday - today).days))
print("Seccond's Left: {} sec".format((bday - today).total_seconds()))


# Custom Time:---
tt = datetime.time(8, 30, 40, 100)
print("Time: {}".format(tt))
print("Hour: {}".format(tt.hour))
print("Minute: {}".format(tt.minute))
print("Seconds: {}".format(tt.second))
print("Micro Seconds: {}".format(tt.microsecond))


# User Input:--
def CustomTime(hr, mins, sec=0, microsec=0):
    tt = datetime.time(hr, mins, sec, microsec)
    print("Time: {}".format(tt))
    print("Hour: {}".format(tt.hour))
    print("Minute: {}".format(tt.minute))
    print("Seconds: {}".format(tt.second))
    print("Micro Seconds: {}".format(tt.microsecond))

CustomTime(8, 30, 40, 100)
CustomTime(8, 30)


def CustomeDate(yr, mn, dtt):
    dt = datetime.date(yr, mn, dtt)
    print("Date: {}".format(dt))
CustomeDate(2021, 1, 19)


# DateTime.DateTime:-----
def CustomeDateTime(yr, mn, day, hr, mins, sec=0, mms=0):
    ddt = datetime.datetime(yr, mn, day, hr, mins, sec, mms)
    print("DateTime: {}".format(ddt))
    print("Date: {}".format(ddt.date()))
    print("Time: {}".format(ddt.time()))

CustomeDateTime(2021, 1, 19, 9, 19, 5, 450)
CustomeDateTime(2021, 1, 19, 9, 19)


def CustomeDateTime(yr, mn, day, hr, mins, sec=0, mms=0):
    dd = datetime.datetime(yr, mn, day, hr, mins, sec, mms)
    tdel = datetime.timedelta(days=10)
    ddt = dd + tdel
    print("DateTime: {}".format(ddt))
    print("Date: {}".format(ddt.date()))
    print("Time: {}".format(ddt.time()))

CustomeDateTime(2021, 1, 19, 9, 19, 5, 450)
CustomeDateTime(2021, 1, 19, 9, 19)


def CustomeDateTime(yr, mn, day, hr, mins, sec=0, mms=0):
    dd = datetime.datetime(yr, mn, day, hr, mins, sec, mms)
    tdel = datetime.timedelta(days=10, hours=10, seconds=20)
    ddt = dd + tdel
    print("DateTime: {}".format(ddt))
    print("Date: {}".format(ddt.date()))
    print("Time: {}".format(ddt.time()))

CustomeDateTime(2021, 1, 19, 9, 19, 5, 450)
CustomeDateTime(2021, 1, 19, 9, 19)


# TimeZone():-------
def TimeZone():
    import pytz
    dt = datetime.datetime.now()
    ddt = pytz.timezone("Asia/Kolkata")
    print(ddt.localize(dt))
TimeZone()

