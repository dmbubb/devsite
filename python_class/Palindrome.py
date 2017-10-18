stringIn = str(input("String to check for anagram: "))

def checkAna(myString):
  myStr = myString.lower()
  if myStr == myStr[::-1]:
        print("Yes, it is an anagram")
  else:
        print("Not an anagram")
     
checkAna(stringIn)
