#!/usr/bin/python

from math import pow

import sys

icount = 0

#Defining function that multiplies two numbers via Karatsuba Algorithm
def Karatsuba(x,y):

    global icount 
    icount = icount + 1
    #if icount > 5: sys.exit()

    xstr = str(x)
    ystr = str(y)

    n = len(xstr)

    # base case
    if x < 10 or y < 10:
       return x*y

    # Adding protection against cases that will currently crash program
    if len(xstr) != len(ystr):
        print "ERROR: Numbers must have the same number of digits. Please try again."
        #return -1

    if n % 2 != 0:
        print "ERROR: Numbers must have an even number of digits. Please try again."
        return -1

    nby2 = n/2  

    a = int(xstr[:nby2])
    b = int(x - pow(10,nby2)*a)
    c = int(ystr[:nby2])
    d = int(y - pow(10,nby2)*c)

    ac = Karatsuba(a,c)

    bd = Karatsuba(b,d)

    ad = Karatsuba(a,d)

    bc = Karatsuba(b,c)

    sum = pow(10,n)*ac + pow(10,nby2)*(ad+bc) + bd

    print "Sum is: " + str(sum)

    return sum

#***********************************************************************************************************   
#-----------------------------------------------------------------------------------------------------------    
# Starting Program that accepts two numbers and returns their product calculated via the Karatsuba algorithm
#-----------------------------------------------------------------------------------------------------------    
#***********************************************************************************************************   

if len(sys.argv) != 3:
    print "ERROR: Incorrect number of arguments! Please pass two numbers. Try again."

else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    product = Karatsuba(num1, num2)

    if product >= 0: print str(num1)+" * "+str(num2)+" = "+str(product)


