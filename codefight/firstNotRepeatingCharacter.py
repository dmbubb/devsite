#! /usr/bin/env python3
#Note: Write a solution that only iterates over the string once and uses O(1) additional memory.

#Given a string s, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.



import random


def createStr(strLen):
    strResult = ""
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(strLen):
        strResult = strResult + alpha[random.randint(0,len(alpha)-3)]
    strResult = strResult + alpha[len(alpha)-2]
    strResult = strResult + alpha[len(alpha)-1]
    return strResult


def firstNotRepeatingCharacter(s):
    s_set = frozenset(s)
    res = ""
    #print(s)
    #print(s_set)
    non_dupes = {}
    non_dupes[len(s)+1] = "_"
    for entry in s_set:
        if s.count(entry) == 1:
            #print(s.index(entry))
            non_dupes[s.index(entry)] = entry

        #print(non_dupes)
        #print(min(non_dupes, key=non_dupes.get))
    res = non_dupes[min(non_dupes.keys())]
    return res



#s = "ababcababzababcababaabd"
#s = 'abcdefghijklmnopqrstuvwxyz'
#s = 'abcdefghijklmnopcqrstuvwxyz'
s = 'z'
#print(firstNotRepeatingCharacter(createStr(50)))
print(firstNotRepeatingCharacter(s))
