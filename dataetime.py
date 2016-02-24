import datetime

# date

t = datetime.date.today()
print(t)
print("day-",t.day)
print("month-",t.month)
print("year-",t.year)
print("today-",t)
print("ctime-",t.ctime())
print("timetuple-",t.timetuple())
print("now-",datetime.datetime.now())
print("\n")

# date arithmetic

tt = datetime.date.today()
print("tomorrow-",tt+datetime.timedelta(days=1))
print("yesterday-",tt-datetime.timedelta(days=1))
print("one week forward-",tt+datetime.timedelta(days=7))
print("one week before-",tt-datetime.timedelta(days=7))
print("\n")

# time

t = datetime.time(datetime.datetime.now().hour%12,datetime.datetime.now().minute,datetime.datetime.now().second)   # hh:mm:ss.ssssss 24 hour clock
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)
print("\n")
