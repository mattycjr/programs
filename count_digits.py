#!/usr/bin/env python3

"""This solves an old math brain teaser/challenge from when I was in college.
The point is to count every digit you would pass from
1 - 1,000,000. I have adopted the code to count to whatever you
like.  Anything past 1M will take quite some time.
Majority of code credit goes to Adam Watters.  My
version worked, but was clunky and took way too long.

Program originally written in Java which has my version of getting the correct answer.
"""

#intialize some variables for the program
#only doing 0s, 1s, and 2s. 2-9s should be the same.
onesW = 0
zeroesW =  0
twosW = 0

#get number to count to
gotonum = int(input("Give me the count number! "))
numLen = 0

#iterate through the number to count each digit

for i in range(1,gotonum+1):
  numLen = len(str(i))
  place = 10
  r = 0

  for j in range(1,numLen+1):
    if j == 1:
      r = i % 10

    else:
      r = (i//place) % 10
      place *= 10


    if r == 0:
      zeroesW += 1
    elif r == 1:
        onesW += 1
    elif r == 2:
        twosW += 1

print("Count Digits from 1 to " + str(gotonum))
print("0 = " + str(zeroesW))
print("1 = " + str(onesW))
print("2-9 = " + str(twosW))
