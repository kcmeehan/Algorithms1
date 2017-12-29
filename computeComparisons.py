#!/usr/bin/python
'''
Programming assignment number 3 -- Part 1
'''

import sys
import numpy as np

def partition(subArray, leftIndex, rightIndex, nCompareCount):
    '''
    Compares elements in subArray to pivot and partitions accordingly
    '''

    # Base case: if array has only one entry then it is already sorted
    # and no comparisons are necessary (total comparisons = 0)
    if rightIndex - leftIndex == 1:
       # print "(Sub)array is of unit size; no comparisons are necessary"
        return nCompareCount

    # Increment number of comparisons by array length - 1
    nCompareCount += rightIndex - leftIndex - 1

    # Choose first array element as pivot
    pivot = subArray[leftIndex]

    # Intitialize i (the first element in the subarray of elements larger than the pivot)
    i = leftIndex + 1

    # Do the partitioning
    for j in range(leftIndex + 1, rightIndex):
        if subArray[j] < pivot:
            if j != i:
                subArray[j], subArray[i] = subArray[i], subArray[j]
            i += 1

    # Put pivot in its proper place
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
    print numArray

if __name__ == "__main__":
    main()
