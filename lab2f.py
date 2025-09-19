#!/usr/bin/env python3

import sys

'''
 lab2e: while loops
'''
#Author: Agnestra Mahat
#Author ID: 128939238
#Date Created: 2025-09-16

#The count value is the first argument provided while running the script
count = int(sys.argv[1])



#This is our while loop
while count != 0:
    print(count)
    count = count - 1

print('blast off!')