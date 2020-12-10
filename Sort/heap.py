import math


def main():
    # A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    heapSort(A)
    print(A)


def parent(i):
    return math.floor((i - 1) / 2)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def maxHeapify(A, i, heapsize):
    l = left(i)
    r = right(i)
    # Find largest i, l or r
    if l < heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heapsize and A[r] > A[largest]:
        largest = r

    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        # Max heapify sub-tree
        maxHeapify(A, largest, heapsize)


def buildMaxHeap(A, heapsize):
    for i in range(math.floor((len(A) - 1) / 2), -1, -1):
        maxHeapify(A, i, heapsize)


def heapSort(A):
    heapsize = len(A)
    buildMaxHeap(A, heapsize)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapsize -= 1
        maxHeapify(A, 0, heapsize)


if __name__ == "__main__":
    main()
