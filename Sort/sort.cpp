// #include "sort.h"
#include <bits/stdc++.h>
using namespace std;

template <typename T>
void insertionSort(vector<T> &A);
template <typename T>
void bubbleSort(vector<T> &A);
template <typename T>
void mergeSort(vector<T> &A, int p, int r);
template <typename T>
void merge(vector<T> &A, int p, int q, int r);
template <typename T>
void quickSort(vector<T> &A, int p, int r);
template <typename T>
int partition(vector<T> &A, int p, int r);

int main()
{
    vector<int> arr = {9, 8, 7, 6, 5, 4, 3, 2, 1};

    for (auto i : arr)
        cout << i << "\t";
    cout << endl;

    mergeSort(arr, 0, arr.size() - 1);

    for (auto i : arr)
        cout << i << "\t";
    cout << endl;

    return 0;
}

template <typename T>
void quickSort(vector<T> &A, int p, int r)
{
    int q;
    if (p < r)
    {
        q = partition(A, p, r);
        quickSort(A, p, q - 1);
        quickSort(A, q + 1, r);
    }
}

template <typename T>
int partition(vector<T> &A, int p, int r)
{
    T x = A[r];
    int i = p - 1;
    for (int j = p; j < r; j++)
    {
        if (A[j] <= x)
        {
            i++;
            T temp = A[i];
            A[i] = A[j];
            A[j] = temp;
        }
    }
    T temp = A[i + 1];
    A[i + 1] = A[r];
    A[r] = temp;
    return i + 1;
}

template <typename T>
void mergeSort(vector<T> &A, int p, int r)
{
    int q;
    if (p < r)
    {
        q = (p + r) / 2;
        mergeSort(A, p, q);
        mergeSort(A, q + 1, r);
        merge(A, p, q, r);
    }
}

template <typename T>
void merge(vector<T> &A, int p, int q, int r)
{
    vector<T> B = A;

    int i = p;
    int j = q + 1;
    int k = i;

    while (i <= q && j <= r)
    {
        if (B[i] <= B[j])
            A[k] = B[i++];
        else
            A[k] = B[j++];
        k++;
    }

    while (i <= q)
        A[k++] = B[i++];
    while (j <= r)
        A[k++] = B[j++];
}

template <typename T>
void insertionSort(vector<T> &A)
{
    T key;
    for (int j = 1; j < A.size(); j++)
    {
        key = A[j];
        int i = j - 1;
        while (i >= 0 && A[i] > key)
        {
            A[i + 1] = A[i];
            i--;
        }
        A[i + 1] = key;
    }
}

template <typename T>
void bubbleSort(vector<T> &A)
{
    for (int i = 0; i < A.size() - 1; i++)
    {
        for (int j = 0; j < A.size() - 1 - i; j++)
        {
            if (A[j] > A[j + 1])
            {
                T temp = A[j];
                A[j] = A[j + 1];
                A[j + 1] = temp;
            }
        }
    }
}