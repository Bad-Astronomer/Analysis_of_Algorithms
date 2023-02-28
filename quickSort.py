import time 
import random
import matplotlib.pyplot as plt
from tqdm import tqdm
import sys
from math import log2

sys.setrecursionlimit(1001)

def quickSort(arr, pivot, e):
    i, j = pivot+1, e
    #1 element
    if pivot > e:
        return
    #2 elements
    if pivot +1 == e:
        if arr[pivot] > arr[e]:
            arr[pivot], arr[e] = arr[e], arr[pivot]
        return
    #general case
    while True:
        while i < e and arr[i] < arr[pivot]:
            i += 1
        while arr[j] > arr[pivot]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            arr[j], arr[pivot] = arr[pivot], arr[j]
            quickSort(arr, pivot, j-1)
            quickSort(arr, j+1, e)
            return arr



sizes = [10*i for i in range(1,100 +1)]
timer_arr, timer_arr2 = [], []

for size in tqdm(sizes):
    
    # avg case
    i, arr = 0, []
    while(i < size): 
        rand = random.randint(1, size)
        if rand in arr:
            continue
        i += 1
        arr.append(rand)
    
    # if(sorted(arr) != quickSort(arr, 0, len(arr)-1)):
    #     print("STOP")
    #     break

    time1 = time.perf_counter()
    arr = quickSort(arr, 0, len(arr)-1)
    time2 = time.perf_counter()
    timer_arr.append((time2 - time1)*1000)


    # worst case
    arr = [size-i for i in range(size)]
    
    time1 = time.perf_counter()
    arr = quickSort(arr, 0, len(arr)-1)
    time2 = time.perf_counter()
    timer_arr2.append((time2 - time1)*1000)


avg_growth = [(size*log2(size)) for size in sizes]
avg_growth = [(growth_element/ avg_growth[-1])*timer_arr[-1] for growth_element in avg_growth]


plt.plot(timer_arr)
plt.plot(avg_growth, linestyle = "dashed")
plt.show()

worst_growth = [(size**2) for size in sizes]
worst_growth = [(worst_growth_element/ worst_growth[-1])*timer_arr2[-1] for worst_growth_element in worst_growth]


plt.plot(timer_arr2)
plt.plot(worst_growth, linestyle = "dashed")
plt.show()
