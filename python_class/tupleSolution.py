#n = int(input())
#s = str(input())
s = "35 30 18 16 12 33 33 25 22 3 29 6 12 17 26 57 57 -57 57"
ts = tuple(s)

def findbig(s):
  t = []
  for i in s.split():
    tnum = int(i)
    if tnum not in t:
      t.append(tnum)
  t.sort(reverse=True)
  #print(t)
  print(t[1])
  

findbig(s)
