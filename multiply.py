#!/usr/bin/python
'''
Programming assignment number 1
'''

def multiply(num1, num2):
    """
    Multiplies two numbers using the Karatsuba algorithm
    """

    #base case
    xstr = str(num1)
    ystr = str(num2)
    print str(len(xstr))
    print str(len(ystr))
   
    if len(xstr) == 0 or len(ystr) == 0:
        print "Error: One or more of the inputs is null."
        return -1

    if len(xstr) == 1:
        return num1*num2

    if len(xstr) < len(ystr):
        print "Warning: numbers have different numbers of digits."
        while len(xstr) < len(ystr):
            xstr = str(0)+xstr

    elif len(ystr) < len(xstr):
        print "Warning: numbers have different numbers of digits."
        while len(ystr) < len(xstr):
            ystr = str(0)+ystr

    ndigits = len(xstr)
    nby2 = len(xstr)/2

    anum = int(xstr[:nby2])
    bnum = num1 - anum * 10**nby2
    cnum = int(ystr[:nby2])
    dnum = num2 - cnum * 10**nby2

    acprod = multiply(anum, cnum)
    adprod = multiply(anum, dnum)
    bcprod = multiply(bnum, cnum)
    bdprod = multiply(bnum, dnum)

    print "acprod: " + str(acprod)

    return acprod*10**ndigits + (adprod + bcprod) * 10**nby2 + bdprod


    #recursive calls

    #end steps

def main():
    """
    Function to test if Karatsuba algorithm is working correctly
    """
    ans = multiply(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627)
    #ans = multiply(31415999, 76270090)
    print "The product is: " + str(ans)

if __name__ == "__main__":
    main()
