# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 16:07:47 2023

@author: dewitt
"""

#The function def readFloat(prompt) that displays the prompt string, followed by a space, 
#reads a floating-point number in, and returns it. Here is a typical usage:

##
#  Use a function to read a floating point value from the user.
#

def main() :
   salary = readFloat("please enter your salary:")
   percentageRaise = readFloat("What percentage raise would you like?")
   print("The salary is", salary)
   print("The raise percentage is", percentageRaise)

## Read a floating point number from the user.
#  @param prompt the promtp to display for the user
#  @return the number entered by the user as a floating point value
#
def readFloat(prompt) :
    poop = input(prompt)
    poop = float(poop)
    
    return poop
    
    

# Call the main function.
main()

