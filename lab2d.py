#!/usr/bin/env python3

''' 
Lab2d: Prints usage messages if not exactly two arguments are present 
'''

#Calls the sys module so that we can use sys.argv
import sys 

#Prints a usage message if zero arguments provided
if len(sys.argv) == 1:
    print('Usage: ' + sys.argv[0] + ' name age')
    sys.exit()

#Prints a usage message if not exactly two arguments provided
if len(sys.argv) != 3:
    print('Usage: ' + sys.argv[0] + ' name age')
    sys.exit()
 
# Uses the first argument as name and the second argument as age 
name = sys.argv[1]
age = sys.argv[2]

#Gives you the required output after you run the script with exactly two arguments
print('Hi ' + name + ', you are ' + str(age) + ' years old.') 
