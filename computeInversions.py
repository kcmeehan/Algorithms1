#!/usr/bin/python
'''
Programming assignment number 2
'''

import sys
import math
import numpy as np

def sortAndCount(numArray, nInversions):
    """
    Sorts each half of an array and computes the number of non-split inversions in an array
    """

    numArraySize = numArray.size

    # Base case
    if numArraySize == 1:
        return numArray, nInversions

    # Recursively divide into subproblems
    leftArray = numArray[0:math.ceil(numArraySize/2.)]
    rightArray = numArray[math.ceil(numArraySize/2.):numArraySize]
    leftArray, nInversions = sortAndCount(leftArray, nInversions)
    rightArray, nInversions = sortAndCount(rightArray, nInversions)

    i = 0 # index for left array
    j = 0 # index for right array
    sortedArray = np.empty((leftArray.size+rightArray.size, 1)) # container for merged array

    # Looping over merged array size
    for k in range(0, sortedArray.size):

        # End cases
        if i == leftArray.size and j < rightArray.size:
            sortedArray[k] = rightArray[j]
            j += 1
        elif j == rightArray.size and i < leftArray.size:
            sortedArray[k] = leftArray[i]
            nInversions += j
            i += 1

        # Normal cases
        elif leftArray[i] < rightArray[j]:
            sortedArray[k] = leftArray[i]
            nInversions += j
            i += 1
        else:
            sortedArray[k] = rightArray[j]
            j += 1

    return sortedArray, nInversions

def mergeAndCount(sortedLeftArray, sortedRightArray):
    """
    Computes the total number of split inversions in an array
    """
    # Create container for merged array
    sortedArray = np.empty((sortedLeftArray.size+sortedRightArray.size, 1))
    sortedArraySize = sortedArray.size

    i = 0 # index for sorted left array
    j = 0 # index for sorted right array
    nInversions = 0 # counter for split inversions

    # Looping over merged array
    for k in range(0, sortedArraySize):

        # End cases
        if i == sortedLeftArray.size and j < sortedRightArray.size:
            #print "end case left"
            sortedArray[k] = sortedRightArray[j]
            j += 1
        elif j == sortedRightArray.size and i < sortedLeftArray.size:
            #print "end case right"
            sortedArray[k] = sortedLeftArray[i]
            i += 1

        # Normal cases
        elif sortedLeftArray[i] < sortedRightArray[j]:
            #print "case big right"
            sortedArray[k] = sortedLeftArray[i]
            i += 1
        elif sortedRightArray[j] < sortedLeftArray[i]:
            #print "case big left"
            sortedArray[k] = sortedRightArray[j]
            j += 1
            nInversions += sortedLeftArray.size - i

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
    numArray = np.loadtxt(fileName, int)

    arraySize = numArray.size

    # Base case
    if arraySize == 1:
        return 0

    leftArray = numArray[0:arraySize/2]
    rightArray = numArray[arraySize/2:arraySize]
    nLeftInversions = 0
    nRightInversions = 0
    # Count left inversions
    sortedLeftArray, nLeftInversions = sortAndCount(leftArray, nLeftInversions)
    # Count right inversions
    sortedRightArray, nRightInversions = sortAndCount(rightArray, nRightInversions)

    #print "The left sortedArray is given here: " + str(sortedLeftArray) + " with " \
#+ str(nLeftInversions) + " inversions"
#    print "The right sortedArray is given here: " + str(sortedRightArray) + " with " \
#+ str(nRightInversions) + " inversions"
    sortedNumArray, nSplitInversions = mergeAndCount(sortedLeftArray, sortedRightArray)

#    print "The FINAL array is given here: " + str(sortedNumArray)
    print "TOTAL INVERSIONS: " + str(nLeftInversions+nRightInversions+nSplitInversions)

    return nLeftInversions+nRightInversions+nSplitInversions

if __name__ == "__main__":
    main()
