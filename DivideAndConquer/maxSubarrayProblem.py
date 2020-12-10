import sys
import math


def main():
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    low, high, sum = findMaxSubarray(A, 0, len(A) - 1)
    print("low: {} high: {} sum: {}".format(low, high, sum))


def findMaxCrossingSubarray(A, low, mid, high):
    leftSum = -sys.maxsize
    sum = 0
    for i in range(mid, low-1, -1):
        sum += A[i]
        if sum > leftSum:
            leftSum = sum
            maxLeft = i
        i -= 1

    rightSum = -sys.maxsize
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += A[j]
        if sum > rightSum:
            rightSum = sum
            maxRight = j
        j += 1
    return maxLeft, maxRight, leftSum + rightSum


def findMaxSubarray(A, low, high):
    if high == low:
        return low, high, A[low]
    else:
        mid = math.floor((low + high) / 2)
        leftLow, leftHigh, leftSum = findMaxSubarray(A, low, mid)
        rightLow, rightHigh, rightSum = findMaxSubarray(A, mid + 1, high)
        crossLow, crossHigh, crossSum = findMaxCrossingSubarray(A, low, mid, high)

        if leftSum >= rightSum and leftSum >= crossSum:
            return leftLow, leftHigh, leftSum
        elif rightSum >= leftSum and rightSum >= crossSum:
            return rightLow, rightHigh, rightSum
        else:
            return crossLow, crossHigh, crossSum


if __name__ == "__main__":
    main()
