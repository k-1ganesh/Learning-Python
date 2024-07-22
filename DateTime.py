import datetime 

# Creating date using date.
# date(year,month,day)

dt = datetime.date(2024,5,12)
print(dt)
print(type(dt))
print(dt.year)
print(dt.month)
print(dt.day)

dtoday = datetime.date.today()
print(dtoday)

# Timedelta. Its gap between dates in terms of days.

tdelta = datetime.timedelta(days = 10)

# Time.
# time(hour,minute,second)
time = datetime.time(10,14,10)
print(time)
print(time.hour)
print(time.minute)
print(time.second)

# We can add date and time at the same time using datetime.

dtime = datetime.datetime(2024,4,12,10,15,12)
print(dtime)
print(dtime.date())
print(dtime.time())
print(dtime.year)


# Convert string to datetime.

date = '2024-12-15'
ddate = '2024-Nov-15'
dtime = datetime.datetime.strptime(date,'%Y-%m-%d')
ddtime = datetime.datetime.strptime(ddate,'%Y-%b-%d')
print(dtime)
print(ddtime)
print(type(dtime))

