from typing import List
'''
PSEUDOCODE
for j = 2 to A.length
    key = A[j]
    //insert A[j] into the sorted sequence
    i = j - 1
    while i>0 and A[i]>key
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = key
'''

A = [5, 2, 4, 6, 1, 3]

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertionSort(A))