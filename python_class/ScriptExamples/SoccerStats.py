print("Soccer Stats")
totalgames=20
pname=input("what is the player name? ")
pgames=float(input("how many games played? "))
pgamepercent=(pgames/totalgames*100)
print("The season has ",totalgames," games.")
print(pname," played in ",pgames," games.")
ptype=input("Is player a goalie? Yes or No? ")
ans=(ptype.lower())
if ans == "yes":
  psaves=float(input("how many saves? "))
  savespergame=psaves/pgames
  print(pname, " had ", savespergame, " saves per game")
elif ans == "no":
  pgoals=float(input("how many goals scored? "))
  passists=float(input("how many assists? "))
  pyellows=float(input("how many yellows? "))
  ppoints=(pgoals*2+passists)
  pyelfreq=(pyellows/pgames)
  print(pname, " had ", ppoints, " points and ", pyelfreq, " yellow cards per game")
else:
  print("Please try again")
#
