#!/usr/bin/python

from math import pow

import sys

icount = 0

#Defining function that multiplies two numbers via Karatsuba Algorithm
def Karatsuba(x,y):

    global icount 
    icount = icount + 1
    #if icount > 5: sys.exit()

    xstr = str(x);
    ystr = str(y);

    n = len(xstr)

    # base case
    if n == 1 or x == 0 or y == 0:
       return x*y

    nby2 = n/2  

    a = int(xstr[:nby2])
    b = x - pow(10,nby2)*a
    c = int(ystr[:nby2])
    d = y - pow(10,nby2)*c

    ac = Karatsuba(a,c);

    bd = Karatsuba(b,d);

    ad = Karatsuba(a,d);

    bc = Karatsuba(b,c);

    sum = pow(10,nby2)*ac + pow(10,nby2)*(ad+bc) + bd

    return sum

#***********************************************************************************************************   
#----------------------------------------------------------------------------------------------------------    
# Starting Program that accepts two numbers and returns their product calculated via the Karatsuba algorithm
#----------------------------------------------------------------------------------------------------------    
#***********************************************************************************************************   

if len(sys.argv) != 3:
    print "ERROR: Incorrect number of arguments! Please pass two numbers. Try again."

else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    product = Karatsuba(num1, num2)

    if product >= 0: print str(num1)+" * "+str(num2)+" = "+str(product)


