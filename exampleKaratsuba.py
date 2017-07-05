#!/usr/bin/python

# This example is from https://pythonandr.com/2015/10/13/karatsuba-multiplication-algorithm-python-code/

import sys

def exampleKaratsuba(x,y):

	"""Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		n = max(len(str(x)),len(str(y)))
		nby2 = n / 2
		
		a = x / 10**(nby2)
		b = x % 10**(nby2)
		c = y / 10**(nby2)
		d = y % 10**(nby2)
		
		ac = exampleKaratsuba(a,c)
		bd = exampleKaratsuba(b,d)
		ad_plus_bc = exampleKaratsuba(a+b,c+d) - ac - bd
        
        	# this little trick, writing n as 2*nby2 takes care of both even and odd n
		prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd

                return prod

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
    product = exampleKaratsuba(num1, num2)

    if product >= 0: print str(num1)+" * "+str(num2)+" = "+str(product)

