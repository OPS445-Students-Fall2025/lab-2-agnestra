#!/usr/bin/env python3

import sys

#Author: Agnestra Mahat
#Author ID: 128939238
#Date Created: 2025-09-16


# Checks if no argumnents is provided 
if len(sys.argv) == 1:
    #Default value for timer if no arguments present
    timer = 3

    while timer != 0:
        print(timer)
        timer = timer - 1

#If an argument is present replaces the timer value.
if len(sys.argv) == 2:
    timer = int(sys.argv[1])
    while timer != 0:
        print(timer)
        timer = timer - 1
print('blast off!')

