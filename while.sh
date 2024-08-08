#!/bin/bash

#simple while loop to iterate and print a list of numbers to the screen

n=1
while [ $n -le 5 ]; do
  echo "Iteration number $n"
  ((n+=1))
done
