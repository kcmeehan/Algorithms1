#!/usr/bin/python
'''
Programming assignment number 2
'''

import sys
import numpy as np

def sortAndCount(numArray):
    """
    Computes the number of inversions in a text file
    """

    # Base case
    if arraySize == 1:
        return numArray, 0

    leftArray = numArray[0:arraySize/2]
    rightArray = numArray[arraySize/2:arraySize]

    #leftArray, nLeftInversions =


def main():
    """
    Main
    """

    if len(sys.argv) < 2:
        print "ERROR: No filename is passed to script. Aborting."
        return -1

    # Load file into array
    fileName = sys.argv[1]
    numArray = np.loadtxt(fileName,int)

    
    arraySize = numArray.size
    leftArray = numArray[0:arraySize/2] 
    rightArray = numArray[arraySize/2:arraySize]
    leftSortedArray, nLeftInversions = sortAndCount(leftArray) # Count left inversions
    rightSortedArray, nRightInversions = sortAndCount(rightArray) # Count right inversions
    # sortedNumArray, nSplitInversions = mergeAndCount()

if __name__ == "__main__": main()
