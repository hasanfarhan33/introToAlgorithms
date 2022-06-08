'''
PSEUDOCODE
for i = 1 to A.length - 1:
    for j = A.length downto i+1:
        if A[j] < A[j-1]
            exchange A[j] with A[j-1]
'''
from typing import List
arr = [3, 5, 9, 2, 10, 8, 7]

def bubbleSort(arr:List[int]):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
    return arr

print(bubbleSort(arr))