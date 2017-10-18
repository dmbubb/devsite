#from random import *
import random
#N = int(input("Please enter a year > 399: ").strip())

# wikipedia shows us algorithm for leap year:
# if (year is not divisible by 4) OR
# if (year is not divisible by 100) but (year is not divisible by 400)
# then it is a common year
# else it is a leap year



for i in range(45):
    year_type = ""
    yr = (random.randint(4,24) * 100)
    
    if (yr % 100 == 0 ):
        if (yr % 400 == 0 ):
            year_type = "leap"
        else:
            year_type = "common"
    elif (yr % 4 == 0 ):
        year_type = "leap"
    else:
        year_type = "common"
        
    print( str(yr) + " " + year_type)
