import string

string1 = str(input("First string: "))
string2 = str(input("String to check for anagram: "))
loCase = string.ascii_lowercase

def checkAna(myString1,myString2):
  myStr1 = myString1.lower()
  myStr2 = myString2.lower()
  if myStr1 != myStr2 and myStr1.len() == myStr2.len() :
    print("not identical")
    for i in myStr1:
      if i in loCase:
        print(i)
        

     
checkAna(string1,string2)
