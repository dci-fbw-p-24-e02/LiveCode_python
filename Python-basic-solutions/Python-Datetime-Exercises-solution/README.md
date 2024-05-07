# Python-Datetime-Exercises

## Description
- How to create a date object and manipulate it.
- How to format a date and time and the different formats.
- Add time.
- Difference between two dates.
- timedelta.
- How to work with calendars.

##

## Tasks
###
**Note: The output of the following Tasks can change according to when the program will be executed.**

###

### Task 1
Write a Python script to display the various Date Time formats.
- Current date and time
- Current year
- Month of year
- Week number of the year
- Weekday of the week
- Day of year
- Day of the month
- Day of week
###
- Your result could look like this :

```
Current date and time:  2023-03-13 17:24:28.526015
Current year:  2023
Month of year:  March
Week number of the year:  11
Weekday of the week:  1
Day of year:  72
Day of the month :  13
Day of week:  Monday
```

### Task 2
Write a Python program to print yesterday, today, tomorrow. 

- Your result could look like this :

```
Yesterday :  2023-03-11
Today :  2023-03-12
Tomorrow :  2023-03-13
```
### Task 3 
Write a Python program to add 5 seconds to the current time.
###
**Hint:** you can use `timedelta` to solve the task.

- Your result could look like this :

```
Current time: 12:37:43.350241                                                                                               
After adding 5 seconds: 12:37:48.350241 
```
### Task 4
Write a Python program to print the next 5 days starting today. 
###
**Hint:** you can use `timedelta` and `for` loop to solve the task.

- Your result could look like this :

```
Today: 2023-03-13 17:30:24.199855
Next 5 days:
2023-03-14 17:30:24.199855
2023-03-15 17:30:24.199855
2023-03-16 17:30:24.199855
2023-03-17 17:30:24.199855
2023-03-18 17:30:24.199855
```
### Task 5
Write a Python program to convert Year/Month/Day to Day of Year using datetime module.

- Your result could look like this :

```
Today: 2023-03-12 19:53:25.690478
Day of the year: 71
```

### Task 6
Write a Python program to find the date of the first Monday of a given week.

- Your result could look like this :

```
The first Monday of this week was: 2023-03-13
```

### Task 7
Write a Python program to select all the Sundays in a specified year.
###
**Hint:** Think about using a loop

- Your result could look like this :

```
Input a year: 2023
Output:
2023-01-01
2023-01-08
2023-01-15
----------
2023-12-17
2023-12-24
2023-12-31
```

### Task 8
Write a Python program to get the number of days in a given month and year.
###
**Hint:** you can use `from calendar import monthrange`

- Your result could look like this :

```
Input: 03/2023
Output: 31
```

### TASK 9-BONUS TASK
Write a Python program to display a simple, formatted calendar of a given year and month.
###
**Hint:** Use the `calendar` module to generate the calendar.

- Your result could look like this :

```
Print a calendar for a year and month:
Month (mm): 4   
Year (yyyy): 2023


|++++++ 04-2023 +++++|
|Su Mo Tu We Th Fr Sa|
|--------------------|
|                   1|
| 2  3  4  5  6  7  8|
| 9 10 11 12 13 14 15|
|16 17 18 19 20 21 22|
|23 24 25 26 27 28 29|
|30                  |
|--------------------|
```
