import sys
print("Leap Years exercise")
# The following statement will take in a year and will put it in the variable N
#N = int(input("Please enter a year > 399: ").strip())
N = int(input("Please enter a year > 399: ").strip())
#################
# Step1
#################
# create 2 variables one for the string 'Leap Year!' - the other for 'Common Year'
LY="Leap Year!"
CY="Common Year"
#################
# Step2
#################
# Commonly we think of a leap year as divisible by 4
# Check to see if the year is divisible by 4 and print the appropriate variable if it is  orisnt
#if (N % 4 == 0):
#  print(N," is a ",LY)
#else:
#  print(N," is a ",CY)
#################
# Step3
#################
# But this is not *exactly* correct. Lets look at Wikipedia
# https://en.wikipedia.org/wiki/Leap_year#Algorithm
# How can we turn this into a correct algorithm?
#
# wikipedia shows us:
# if (year is not divisible by 4) then (it is a common year)
# else if (year is not divisible by 100) then (it is a leap year)
# else if (year is not divisible by 400) then (it is a common year)
# else (it is a leap year)
#
if (N % 4 != 0 ):
    #LeapYear is False
    print(N," is a ",CY)
elif (N % 100 != 0 ):
    #LeapYear is True
    print(N," is a ",LY)
elif (N % 400 != 0 ):
    #LeapYear is False
    print(N," is a ",CY)
else:
    #LeapYear is True
    print(N," is a ",LY)
#
#################
# EXTRA1  redo the above with one print statement (hint use a new var to hold Year)
#################
yearType=""
#
if (N % 4 != 0 ):
    #LeapYear is False
    yearType=CY
elif (N % 100 != 0 ):
    #LeapYear is True
    yearType=LY
elif (N % 400 != 0 ):
    #LeapYear is False
    yearType=CY
else:
    #LeapYear is True
    yearType=LY

print(N," is a ",yearType," Extra1")
#################
# EXTRA2  redo the above with Boolean variables
#################
LeapYear=True
yearType=""
#
if (N % 4 != 0 ):
    LeapYear=False
elif (N % 100 != 0 ):
    LeapYear=True
elif (N % 400 != 0 ):
    LeapYear=False
else:
    LeapYear=True

if LeapYear == False:
    yearType=CY
elif LeapYear == True:
    yearType=LY
else:
    print("program error check your code or input")
    exit

print(N," is a ",yearType," Extra2")
