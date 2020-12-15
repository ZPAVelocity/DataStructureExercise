import sys
import numpy as np


def main():
    p = [30, 35, 15, 5, 10, 20, 25]
    m, s = matrixChainOrder(p)
    
    print('m')
    for i in m:
        print(i)
    print('s')
    for i in s:
        print(i)


def matrixMultiply(A, B):
    if A.shape[1] != B.shape[0]:
        print('incompatible dimensions')
        return np.array([[]])
    C = np.array([[0 for i in range(A.shape[0])] for i in range(B.shape[1])])
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            C[i][j] = 0
            for k in range(A.shape[1]):
                C[i][j] += + A[i][k] * B[k][j]
    return C


def matrixChainOrder(p):
    n = len(p) - 1
    m = [[0 for i in range(n)] for j in range(n)]
    s = [[0 for i in range(n)] for j in range(n)]

    for i in range(0, n):
        m[i][i] = 0

    for l in range(2, n + 1):  # l is the chain length
        for i in range(0, n - l + 1):
            j = i + l - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k + 1
    return m, s


if __name__ == "__main__":
    main()
