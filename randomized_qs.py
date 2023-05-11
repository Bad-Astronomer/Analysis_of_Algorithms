import random

def partition(arr, lo, hi):
    pivot = arr[lo]
    i = lo + 1
    j = hi

    while i < j:
        while arr[j] > pivot:
            j -= 1
        while i <= j and arr[i] <= pivot:
            i += 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[lo], arr[j] = arr[j], arr[lo]
    print(arr)
    return j

def partition_r(arr, lo, hi):
    r = random.randint(lo, hi)
    arr[r], arr[hi] = arr[hi], arr[r]
    return partition(arr, lo, hi)

def quickSort(arr, lo, hi):
    if lo < hi:
        p = partition_r(arr, lo, hi)
        quickSort(arr, lo, p-1)
        quickSort(arr, p+1, hi)

arr = input("Enter array input: ")
arr = list(map(int, arr.split(" ")))
quickSort(arr, 0, len(arr)-1)