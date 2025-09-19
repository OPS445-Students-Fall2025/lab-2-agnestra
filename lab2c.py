#!/usr/bin/env python3

#This calls the sys module so that we can use sys.argv
import sys 

# This uses the first argument as name and the second argument as age 
name = sys.argv[1]
age = sys.argv[2]

#This gives you the required output after you run the script with arguments
print('Hi ' + name + ', you are ' + str(age) + ' years old.') 

