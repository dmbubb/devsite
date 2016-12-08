# Mad lib game.  Learning about 'while' loops.

from random import *

###  find me at http://mbubb.devio.us/python_class/rando.py

# STEP 0:
# Review this function that you worked on before.
def randElt(L):
    '''Assuming L is a list, return a random element of the list.'''
    index = randint(0, len(L)-1)
    return L[index]

# STEP 1:
# Read this code, then try running it.  What does it do?
def getNouns():
    nouns = ["turtle"]
    word = "attention"
    while word != "q" :
        nouns = nouns + [word]
        word = input("Enter a noun, or 'q' to quit: ")
    return nouns
        

# STEP 2:
# Can you figure out what this does, without running it?
def madnoun():
    n1 = getNouns()
    print("How about some more?")
    n2 = getNouns()
    
    print("the", randElt(n1), "likes", "the", randElt(n2))
    print("the", randElt(n1), "likes", "the", randElt(n2))


# STEP 3:
# Finish these functions so that madlib makes fun sentences.
def getVerbs():
    pass

def getAdverbs():
    pass

def madlib():
    pass

