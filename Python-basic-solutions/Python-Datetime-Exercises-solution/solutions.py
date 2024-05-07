#Solutions

## TASK 1 

import datetime
print("Current date and time: ", datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))

## TASK 2

import datetime 
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print('Yesterday : ', yesterday)
print('Today : ', today)
print('Tomorrow : ', tomorrow)

## TASK 3

import datetime
x= datetime.datetime.now()
y = x + datetime.timedelta(0,5)
print("Current time:",x.time())
print("After adding 5 seconds:",y.time())

## TASK 4
from datetime import datetime , timedelta
today = datetime.today()
print(f"Today: {today}\nNext 5 days:")
for x in range(0, 5):
      print(today + timedelta(days=x+1))

## TASK 5

from datetime import datetime
today = datetime.now()
day_of_year = (today - datetime(today.year, 1, 1)).days + 1
print("Today: ",datetime.today(),"\nDay of the year: ",day_of_year)

## TASK 6
import datetime
today = datetime.date.today()
weekday = today.weekday()
first_monday = today - datetime.timedelta(days=weekday)
print("The first Monday of this week was:", first_monday)

##TASK 7
from datetime import datetime, timedelta, date
year = int(input("Input a year: "))
d = date(year, 1, 1)
d += timedelta(days=6 - d.weekday())  # First Sunday
while d.year == year:
    print(d)
    d += timedelta(days=7)


## TASK 8
from calendar import monthrange
month, year = (input("Enter Date(ex. 03/2023):").split("/"))

print(monthrange(int(year), int(month))[1])


#TASK 9- BONUS TASK
import calendar
print('Print a calendar for a year and month:')
month = int(input('Month (mm): '))
year = int(input('Year (yyyy): '))
print('\n')

calendar.setfirstweekday(calendar.SUNDAY)
cal = calendar.monthcalendar(year, month)

if len(str(month)) == 1:
    month = '0%s' % month

# Header
print('|++++++ %s-%s +++++|' % (month, year))
print('|Su Mo Tu We Th Fr Sa|')
print('|--------------------|')

# display calendar
border = '|'
for week in cal:
    line = border

    for day in week:
        if day == 0:
          # 3 spaces for blank days
            line += '   '
        elif len(str(day)) == 1:
            line += ' %d ' % day
        else:
            line += '%d ' % day
    # remove space in last column
    line = line[0:len(line) - 1]
    line += border
    print(line)

print('|--------------------|\n')
