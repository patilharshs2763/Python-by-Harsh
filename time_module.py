import time
import datetime as dt
t=time.strftime('%H:%M:%S')
print(t)
t=time.strftime('%H')
print(t)
t=time.strftime('%M')
print(t)
t=time.strftime('%S')
print(t)

today = dt.date.today()  # Current date
print("Today's date:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
print("-----------------------------\n")
current_time = dt.datetime.now().time()  # Current time
print("Current time:", current_time)
print("Hour:", current_time.hour)
print("Minute:", current_time.minute)
print("Second:", current_time.second)
print("-----------------------------\n")
delta = dt.timedelta(days=5, hours=3)
future_date = dt.datetime.now() + delta
print("Future date:", future_date)
print("-----------------------------\n")
now = dt.datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted:", formatted)

parsed = dt.datetime.strptime("2023-08-18 14:30:00", "%Y-%m-%d %H:%M:%S")
print("Parsed:", parsed)