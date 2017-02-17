#!/usr/bin/env python3
from math import *
from random import *
from glob import *
import datetime

ulys="/Users/mbubb/git/devsite/python_class/udemy/ulysses.txt"
sampdir="/tmp/Sample-Files/*"
fileses=glob(sampdir)
tmstmp=datetime.datetime.now()
filen=str("mylog_"+tmstmp.strftime("%Y%m%d_%H%M%S_%f")+".txt")


with open(filen,"w+") as wFile:
    for i in fileses:
        with open(i,"r+") as rFile:
            rFile.seek(0)
            for i in rFile.readlines():
                wFile.write(i+"\n")

with open(filen,"r+") as endFile:
    print(endFile.readlines())


def hundred_ulysses():
    with open(ulys,"r+") as uly:
        uly.seek(0)
        uly_contents=uly.readlines()
        for i in range(100):
            print(uly_contents[randint(0,len(uly_contents)-1)])


hundred_ulysses()
