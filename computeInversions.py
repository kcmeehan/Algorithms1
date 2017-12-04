#!/usr/bin/python
'''
Programming assignment number 2
'''

import sys
import numpy as np

def sortAndCount(numArray, nInversions):
    """
    Computes the number of non-split inversions in an array
    """

    arraySize = numArray.size

    # Base case
    if arraySize == 1:
        return numArray, nInversions

    leftArray = numArray[0:arraySize/2]
    rightArray = numArray[arraySize/2:arraySize]

    leftArray, nInversions = sortAndCount(leftArray, nInversions)
    rightArray, nInversions = sortAndCount(rightArray, nInversions)

    i = 0
    j = 0
    for k in range(0,2*leftArray.size):
        if i == leftArray.size and j < rightArray.size:
            sortedArray[k] = rightArray[j]
            j+=1
        elif j == rightArray.size and i < leftArray.size:
            sortedArray[k] = leftArray[i]
            nInversions+=1
            i+=1
        elif leftArray[i] < rightArray[j]:
            sortedArray[k] = leftArray[i]
            i+=1
        else:
            sortedArray[k] = rightarray[j]
            nInversions+=1
            j+=1

    return sortedArray, nInversions

         
def main():
    """
    Computes the number of inversions in an array
    """

    if len(sys.argv) < 2:
        print "ERROR: No filename is passed to script. Aborting."
        return -1

    # Load file into array
    fileName = sys.argv[1]
    numArray = np.loadtxt(fileName,int)

    arraySize = numArray.size

    # Base case
    if arraySize == 1:
        return 0
    
    leftArray = numArray[0:arraySize/2] 
    rightArray = numArray[arraySize/2:arraySize]
    nLeftInversions = 0
    nRightInversions = 0
    leftSortedArray, nLeftInversions = sortAndCount(leftArray,nLeftInversions) # Count left inversions
    rightSortedArray, nRightInversions = sortAndCount(rightArray,nRightInversions) # Count right inversions
    # sortedNumArray, nSplitInversions = mergeAndCount(leftSortedArray, rightSortedArray)

    #return nLeftInversions+nRightInversions+nSplitInversions

if __name__ == "__main__": main()
