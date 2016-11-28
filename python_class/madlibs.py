from random import *

''' Random Numbers
  find me at http://mbubb.devio.us/python_class/rando.py
  michael.bubb@gmail.com
'''



''' 
 Function to give out random numbers
 
print(randint(a, z))
'''


num = 10
a = 3
z = 10000

def rand_nums(howmany,startnum,endnum):
    for _ in range(howmany):
        return(randint(startnum, endnum))

rand_nums(num,a,z)

def rand_list_element(mylist):
    return(mylist[randint(0,len(mylist)-1)])
    
### Use the color list to print random colors
###

noun_list = []
adj_list = []
verb_list = []
adv_list = []
color_list = ["blue", "green", "yellow", "orange", "red", "purple", "gray", "brown"]
