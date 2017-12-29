#!/usr/bin/python
'''
Programming assignment number 3 -- Part 3
'''

import sys
import math
import numpy as np

def partition(subArray, leftIndex, rightIndex, nCompareCount):
    '''
    Compares elements in subArray to pivot and partitions accordingly
    '''

    # Base case: if array has only one entry then it is already sorted
    # and no comparisons are necessary (total comparisons = 0)
    if rightIndex - leftIndex == 1:
        return nCompareCount

    # Choose pivot
    pivot = -999
    pivotIndex = -999

    # If subArray only has size 2, choose first element to be pivot
    if rightIndex - leftIndex == 2:
        pivot = subArray[leftIndex]
        pivotIndex = leftIndex

    # Else choose the "median of three" as the pivot
    else:
        if (rightIndex - leftIndex) % 2 == 0:
            middleIndex = (rightIndex - leftIndex - 1) / 2 + leftIndex
        else:
            middleIndex = (rightIndex - leftIndex) / 2 + leftIndex
        pivotList = [subArray[leftIndex], subArray[middleIndex], subArray[rightIndex - 1]]
        for ipivot in pivotList:
            if ipivot != min(pivotList) and ipivot != max(pivotList):
                pivot = ipivot
                if pivotList.index(ipivot) == 0:
                    pivotIndex = leftIndex
                elif pivotList.index(ipivot) == 1:
                    pivotIndex = middleIndex
                elif pivotList.index(ipivot) == 2:
                    pivotIndex = rightIndex - 1

    if pivot == -999:
        print "ERROR: INVALID PIVOT"
        return -1

    # Swap the pivot and first element, so pivot will be at the front of array 
    subArray[pivotIndex], subArray[leftIndex] = subArray[leftIndex], subArray[pivotIndex]

    # Increment number of comparisons by array length - 1
    nCompareCount += rightIndex - leftIndex - 1

    # Do the partitioning

    # Intitialize i (the first element in the subarray of elements larger than the pivot)
    i = leftIndex + 1
    for j in range(leftIndex + 1, rightIndex):
        if subArray[j] < pivot:
            if j != i:
                subArray[j], subArray[i] = subArray[i], subArray[j]
            i += 1

    # Put pivot in its proper place and execute recursive calls
    if i-1 != leftIndex:
        subArray[leftIndex], subArray[i-1] = subArray[i-1], subArray[leftIndex]
        nCompareCount = partition(subArray, leftIndex, i-1, nCompareCount)

    if i != rightIndex:
        nCompareCount = partition(subArray, i, rightIndex, nCompareCount)

    return nCompareCount

def main():
    """
    Computes the number of comparisons used to sort the input array by QuickSort
    """

    if len(sys.argv) < 2:
        print "ERROR: No filename is passed to script. Aborting."
        return -1

    # Load file into array
    filename = sys.argv[1]
    numArray = np.loadtxt(filename, int)

    arraySize = numArray.size

    nComparisons = 0
    nComparisons = partition(numArray, 0, arraySize, nComparisons)
    print nComparisons
    #print numArray

if __name__ == "__main__":
    main()
