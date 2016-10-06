import sys
print("Leap Years exercise")
# The following statement will take in a year and will put it in the variable N
N = int(input("Please enter a year > 399: ").strip())
# Step1 create 2 variables one for the string 'Leap Year!' - the other for 'Not a Leap Year'
#
## LY="Leap Year!"
## NLY="Not a Leap Year"
# Commonly we think of a leap year as divisible by 4
# Check to see if the year is divisible by 4 and print the appropriate variable if it is  orisnt
##if (N % 4 == 0):
##  print(LY)
##else:
##  print(NLY)
# But this is not *exactly* correct. Lets look at Wikipedia
# https://en.wikipedia.org/wiki/Leap_year#Algorithm
# How can we turn this into a correct algorithm?
#
## if (N % 4 != 0 ):
##  print(NLY)
## elif (N % 100 != 0 ):
##  print(NLY)
## elif (N % 400 != 0 ):
##  print(NLY)
## else:
##  print(LY)
