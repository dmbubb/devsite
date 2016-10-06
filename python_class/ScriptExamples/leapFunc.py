def is_leap(year):
    leap = False

    if (year % 4 != 0 ):
        leap = False
    elif (year% 100 != 0 ):
        leap = True
    elif (year % 400 != 0 ):
        leap = False
    else:
        leap = True

    if leap == False:
        yearType="common year"
    else:
        yearType="leap year"

    return leap

year = int(input())

if is_leap(year) == False:
    yearType="common year"
else:
    yearType="leap year"

print(year," is a ",yearType )
