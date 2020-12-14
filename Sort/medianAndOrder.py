import sys
import math
from sort import randomizedPartition


def main():

    A = [2, 7, 5, 6, 9, 8, 1, 3, 4, 0]
    print(A)
    for i in range(1, len(A)+1):
        print(randomizedSelect(A, 0, len(A) - 1, i))


def minimum(A):
    min = A[0]
    for i in range(1, len(A)):
        if min > A[i]:
            min = A[i]
    return min


def maximum(A):
    max = A[0]
    for i in range(1, len(A)):
        if max < A[i]:
            max = A[i]
    return max


def minmax(A):
    min = A[0]
    max = A[0]
    for i in range(1, len(A)):
        if min > A[i]:
            min = A[i]
        if max < A[i]:
            max = A[i]
    return min, max


def randomizedSelect(A, p, r, i):
    if p == r:
        return A[p]
    q = randomizedPartition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomizedSelect(A, p, q-1, i)
    else:
        return randomizedSelect(A, q + 1, r, i - k)


if __name__ == "__main__":
    main()
