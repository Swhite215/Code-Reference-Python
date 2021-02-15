# Dates in Python
import datetime

x = datetime.datetime.now()
print(x)
print(x.month)
print(x.day)
print(x.year)

y = datetime.datetime(1993, 2, 15)
print(y)

print(x.strftime("%a")) # Weekday - Short
print(x.strftime("%A")) # Weekday - Full
print(x.strftime("%w")) # Weekday - Number
print(x.strftime("%d")) # Day of Month
print(x.strftime("%b")) # Month - Short
print(x.strftime("%B")) # Month - Full
print(x.strftime("%m")) # Month - Number
print(x.strftime("%y")) # Year - Short
print(x.strftime("%Y")) # Year - Full
print(x.strftime("%H")) # Hour - 24
print(x.strftime("%I")) # Hour - 12
print(x.strftime("%p")) # AM/PM
print(x.strftime("%M")) # Minute
print(x.strftime("%S")) # Second
print(x.strftime("%f")) # Microsecond
print(x.strftime("%z")) # UTC Offset
print(x.strftime("%Z")) # Timezone
print(x.strftime("%j")) # Day of Year 1 - 365
print(x.strftime("%U")) # Week of Year - Sunday
print(x.strftime("%W")) # Week of Year - Monday
print(x.strftime("%c")) # Local Date and Time
print(x.strftime("%x")) # Local Date
print(x.strftime("%X")) # Local Time
