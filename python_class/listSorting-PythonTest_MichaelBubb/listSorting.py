#! /usr/bin/env python2
# I tested this on python3 as well and wasnt sure which to submit for
# This would only work Python2 - list_word.translate(None, string.punctuation)
# there is a simple way to make this work for Python 3 but I decided nto to use this way of
#stripping 'bad chars' below
import random
import string
import datetime
import sys
import os
# using the random library mostly for generating test data (genListStrings)
# this is not needed otherwise
# the string library has a number of useful methods for example:
#   string.ascii_letters
#   string.punctuation
#   string.digits
# datetime because for testing I wanted to have unique input and result files
# sys and os for commandline arguments and pwd (which I didnt end up using)
#
# VARS
# these 2 for generating test data
charpunc = string.punctuation+string.ascii_letters
numpunc = string.punctuation+string.digits
# sets are faster to check to see if something is an element
# below I decided to use the builtin 'isnum' instead though I could nto tell which was faster
bad_chars = set(string.punctuation)
nums = set(string.digits)
# the following are vars for the input and output files - different versions for testing
# for the final just used the sys args
workdir = os.getcwd()
tmstmp = datetime.datetime.now()
#file_inp = str("input_"+tmstmp.strftime("%Y%m%d_%H%M%S")+".txt")
#file_res = str("result_"+tmstmp.strftime("%Y%m%d_%H%M%S")+".txt")
#file_inp = "input.txt"
#file_res = "result.txt"
file_inp = sys.argv[1]
file_res = sys.argv[2]


# this function takes a number of words to generate a list and a file
# Over time I would collapse this into one loop
def genListStrings(num_of_words):
  str_list=[]
  for j in range(num_of_words):
    word_len=random.randint(3,100)
    list_word=""
    if word_len % 2 == 0:
      for i in range(word_len):
        list_word=list_word+charpunc[random.randint(0,len(charpunc)-1)]
    else:
      for i in range(word_len):
        list_word=str(random.randint(0,999999))

    str_list.append(list_word)
  #return(str_list)
  with open(file_inp, "w") as inp:
    for item in str_list:
      inp.write(item + ' ')


# this function strips the nonalphanumeric chars from the words and leaves them
# in the same order
def removeBadChars(input_file):
    with open(input_file, 'r') as infile:
        list_of_words = infile.read().split()
    clean_list=[]
    #print("orig list: " + str(list_of_words))
    for list_word in list_of_words:
        clean_word=""

        #print("orig word: " + list_word)
        if any((bc in bad_chars) for bc in list_word):
            for i in range(0,len(list_word)-1):
                if list_word[i] not in bad_chars:
                    clean_word=clean_word+list_word[i]
        else:
            clean_word=list_word
        ## the following is Python2 only
        #clean_word=list_word.translate(None, string.punctuation)
        clean_list.append(clean_word)
        #print("chars stripped: "+clean_word)
    #print("cleaned list: " + str(clean_list))
    return(clean_list)


# this function splits the fields into 2 lists and sorts them
# by turning the integer strings into real ints the sorting is correct
# there are better ways to do this - I thought about hash tables
def sortList(full_list):
    integer_list = []
    word_list = []
    new_sort_list = []
    for list_word in full_list:
        #print(list_word)
        if list_word.isdigit():
            integer_list.append(int(list_word))
        else:
            word_list.append(list_word)
    word_list.sort()
    integer_list.sort()
    #print(integer_list)
    word_list.reverse()
    integer_list.reverse()
    for list_word in full_list:
        if list_word.isdigit():
            new_sort_list.append(str(integer_list.pop()))
        else:
            new_sort_list.append(word_list.pop())
    #return(new_sort_list)
    with open(file_res, "w") as res:
        for item in new_sort_list:
            res.write(item + ' ')








#genListStrings(10000)
cln_lst=removeBadChars(file_inp)
sortList(cln_lst)
