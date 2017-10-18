#! /usr/bin/env python3
teststr = "wwejfpwejfpweaaaaamvdmVirknafnbbbbbaSpfjpsfjienfdfidcfjfbnsdjfcCccccd"


word_list.sort()
if blahblah:
  word_list.pop(0)

word_list.sort()
word_list.reverse()
if blahblah:
  word_list.pop()

word_list.sort().reverse()
if blahblah:
  word_list.pop()

word_list.sort(reversed=True)
if blahblah:
  word_list.pop()

#a = []
def firstDuplicate(a):
    check_arr = {}
    res = -1
    for entry in a:
        if entry in check_arr:
            res = entry
            break
        else:
            check_arr[entry] = True
            #check_arr.append(entry)
    return res




firstDuplicate(teststr)
