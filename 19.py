# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

dayList = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
dayIndex = 2

sundays = 0

for year in range(1901, 2001):
    for month in range(1, 13):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            days = 31
        elif month in [4, 6, 9, 11]:
            days = 30
        
        # Febuary
        if month == 2:
            # Leap year
            if year % 4 == 0:
                # Not on a century
                if year % 100 == 0:
                    # unless divisible by 400
                    if year % 400 == 0:
                        days = 29
                    else:
                        days = 28
                # if regular leap year
                else:
                    days = 29
            # if not leap year
            else:
                days = 28

        if dayIndex == 0:
            sundays += 1
        dayIndex = (dayIndex + days) % 7

        
print(f"There were {sundays} Sundays on the first of the month during the twentieth century.")