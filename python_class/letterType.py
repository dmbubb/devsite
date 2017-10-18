import string

stringIn = str(input("String to extract letters: "))
loCase = string.ascii_lowercase
def extractLetter(myString):
  myStr = myString.lower()
  myVowels = ["a", "e", "i", "o", "u"]
  vowArray = []
  conArray = []
  for i in myStr:
    if i in loCase:
      if i in myVowels:
        # print(i," is a vowel")
        vowArray.append(i)
      else:
        #print(i," is a consonant")
        conArray.append(i)
  print("Vowels: ",vowArray)
  print("Cons: ",conArray)
  
extractLetter(stringIn)
