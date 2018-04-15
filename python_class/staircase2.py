#!/bin/python3

import os
import sys

#
# Complete the staircase function below.
#
def staircase(n):
  for i in range(n):
      stair="#"
      for j in range(i):
          stair=stair+"#"
      print(stair.rjust(n))

if __name__ == '__main__':
    n = int(input())

    staircase(n)
