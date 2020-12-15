import sys


def main():
    v = [1, 6, 18, 22, 28]
    w = [1, 2, 5, 6, 7]
    c = 11
    m = zeorOneKnapsackDP(c, v, w)

    for i in m:
        print(i)


def zeorOneKnapsackDP(c, v, w):
    '''
    c: capacity of knapsack
    v: value list of items
    w: weight list of items
    '''
    n = len(v)

    m = [[0 for i in range(c + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, c + 1):
            m[i][j] = m[i-1][j]
            if j >= w[i-1] and m[i][j] < m[i - 1][j - w[i - 1]] + v[i - 1]:
                m[i][j] = m[i - 1][j - w[i - 1]] + v[i - 1]

    return m


if __name__ == "__main__":
    main()
