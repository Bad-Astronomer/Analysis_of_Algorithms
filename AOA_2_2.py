# MinMax Algorithm

import numpy as np
import matplotlib.pyplot as plt
from time import time
import random


global counter_arr
counter_arr = []
global count

def minMax(arr, s, e):
    global count
    if s > e:
        print("invalid index")
        return

    elif s < e:
        if not (e - s - 1): #2 elements
            count += 1
            if(arr[s] > arr[e]):
                return e, s
            else:
                return s, e

        else: #more than 2 elements
            count += 1
            #divide
            mid = (s+e)//2 
            min1, max1 = minMax(arr, s, mid) 
            min2, max2 = minMax(arr, mid+1, e)
            #combine
            if arr[max1] < arr[max2]:
                max1 = max2
            if arr[min1] > arr[min2]:
                min1 = min2
            return min1, max1

    #1 element
    return s, s


sizes = [10*i for i in range(100,1100,100)]

for size in sizes:
    count = 0
    arr_unsorted = [random.randint(1,100) for i in range(size)]
    min, max = minMax(arr_unsorted, 0, (size)-1)
    counter_arr.append(count)

plt.plot(counter_arr)
plt.plot(sizes, linestyle = "dashed")
plt.xlabel("No. of Samples")
plt.ylabel("No. of comparisons")
plt.show()
