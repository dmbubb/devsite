# Triple Double
# find me at http://mbubb.devio.us/python_class/tripDoub.py
# run me at http://www.pythonide.org/run.html
# confused? check the docs at https://docs.python.org/2/
# or email
# michael.bubb@gmail.com
#
# lists
#Remember: in Python, 'lists' are ordered collections of elements
#
#
# index in parentheses - 
# [ GamesPlayed(0), Points(1), Rebounds(2), Assists(3), Steals(4), Blocks(5) ]
#  
RussellWestbrook = [ 8, 31.1, 8.3, 9.5, 1.4, 0.6 ]
AnthonyDavis = [ 8, 30.9, 11.4, 1.9, 1.9, 3 ]
JamesHarden = [ 8, 30.6, 7.8, 13, 1.3, 0 ]
KevinDurant = [ 8, 28.8, 7.6, 3.6, 1.9, 1.3 ]
KawhiLeonard = [ 8, 27.4, 5.6, 3.1, 2.3, 0.6 ]
StephenCurry = [ 8, 26.1, 3.3, 5.9, 1.1, 0.3 ]
LeBronJames = [ 7, 22.9, 8.9, 9.9, 1, 0.3 ]
CarmeloAnthony = [ 7, 22.7, 6.1, 2.7, 1, 0.3 ]
GiannisAntetokounmpo = [ 7, 21.1, 8.4, 6, 1.9, 1.9 ]
BrookLopez = [ 7, 20.6, 4.7, 0.9, 0.3, 1.1 ]
BlakeGriffin = [ 8, 19.6, 10.1, 4, 1.3, 0.5 ]
KristapsPorzingis = [ 7, 19.1, 6.7, 0.9, 0.6, 1.4 ]

# TASKS
#
# Print Blake Griffin's rebounds
#print(BlakeGriffin[])
#
#
# How many steals is Anthony David projected to have after 24 games?
#
#
# What is the following showing?
#if JamesHarden[1] > StephenCurry[1]:
#  print("James Harden has more points")
#else:
#  print("Steph has more points")

# A basketball player accomplishes a triple double by reaching double digits in 3 of the following:
# assists, rebounds, points, steals, and blocks.
# In most cases the 3 doubles are assists, rebounds, and points. 
#
def tripDubCheck(player):
    counter = 0
    for i in range(1,5):
        if player[i] >= 10:
            counter = counter + 1
    if counter == 3:
        print("TripleDouble!!!")
    else:
        print("KeepTrying")
        

#DavidNaumann = [ 7, 14.1, 12.7, 10.9, 0.6, 1.4 ]
#MichaelBubb = [ 7, 1.1, 2.7, 0.9, 0.6, 1.4 ]

#print("check DavidNaumann")
#tripDubCheck(DavidNaumann)
#print("check M Bubb")
#tripDubCheck(MichaelBubb)



# EXTRA TOPIC
# Lists of Lists?
# how do I index these?
myPlayers = [ GiannisAntetokounmpo, BrookLopez, BlakeGriffin, KristapsPorzingis ]
jennyPlayers = [ KawhiLeonard, StephenCurry, LeBronJames, CarmeloAnthony ]
williamsPlayers = [ RussellWestbrook, AnthonyDavis, JamesHarden, KevinDurant ]



