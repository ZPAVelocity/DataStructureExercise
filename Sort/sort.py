import math
import sys
import random


def main():
    A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(A)
    insertionSort(A, 0, len(A) - 1)
    print(A)


def merge(A, p, q, r):
    '''
    A: A list needs to be sorted. 
    p: First index
    q: Middle index
    r: Last index
    '''
    L = A[p:q + 1]
    R = A[q + 1:r + 1]

    L.append(sys.maxsize)
    R.append(sys.maxsize)

    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def mergeSort(A, p, r):
    '''
    A: A list needs to be sorted. 
    p: First index
    r: Last index
    '''
    if p < r:
        # divide
        q = math.floor((p + r) / 2)
        # conquer
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        # combine
        merge(A, p, q, r)


def partition(A, p, r):
    '''
    Froom p to r
    Select A[r] as pivot. 
    Separate A with larger than r and smaller than r. 
    '''
    privot = A[r]
    i = p - 1
    # i: Less than privot
    # j: Greater than privot
    for j in range(p, r):
        if A[j] <= privot:
            i += 1
            A[i], A[j] = A[j], A[i]

    # Switch privot to the middle.
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quickSort(A, p, r):
    '''
    A: A list needs to be sorted. 
    p: First index
    r: Last index
    '''
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)


def quickSort2(A):
    if len(A) < 2:
        # base case, arrays with 0 or 1 element are already "sorted"
        return A
    else:
        # recursive case
        pivot = A[0]
        # sub-array of all the elements less than the pivot
        less = [i for i in A[1:] if i <= pivot]
        # sub-array of all the elements greater than the pivot
        greater = [i for i in A[1:] if i > pivot]
        return quickSort2(less) + [pivot] + quickSort2(greater)


def randomizedPartition(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)


def randomizedQuickSort(A, p, r):
    if p < r:
        q = randomizedPartition(A, p, r)
        randomizedQuickSort(A, p, q - 1)
        randomizedQuickSort(A, q + 1, r)


def insertionSort(A, p, r):
    '''
    A: A list needs to be sorted. 
    p: First index
    r: Last index
    '''
    for j in range(p + 1, r + 1):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


def bubbleSort(A, p, r):
    '''
    A: A list needs to be sorted. 
    p: First index
    r: Last index
    '''
    for i in range(p, r + 1):
        for j in range(r, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]


if __name__ == "__main__":
    main()
