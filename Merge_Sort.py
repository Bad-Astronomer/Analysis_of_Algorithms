from time import time
import matplotlib.pyplot as plt
from tqdm import tqdm
from math import log2


def mergeSort(arr, s, e):
    if s > e: 
        print("Invalid")
        return
    
    elif e > s+1: #general case
        #divide
        mid = (s+e)//2
        arr1 = mergeSort(arr, s, mid)
        arr2 = mergeSort(arr, mid+1,e)
        #combine
        i, j, arr3 = 0, 0, []

        while(i < len(arr1) and j < len(arr2)):
            if(arr1[i] < arr2[j]):
                arr3.append(arr1[i])
                i += 1
            else:
                arr3.append(arr2[j])
                j += 1

        if not i < len(arr1):
            arr3.extend(arr2[j:])
        else:
            arr3.extend(arr1[i:]) 
        return arr3
    
    elif not e-s-1:
        if arr[e] < arr[s]:
            arr[e], arr[s] = arr[s], arr[e]

    return arr[s:e+1]


sizes = [1000*i for i in range(1,300)]
timer_arr = []

for size in tqdm(sizes):
    arr = [size-i for i in range(size)]
    tic = time()
    arr = mergeSort(arr, 0, len(arr)-1)
    toc = time()
    timer_arr.append(toc - tic)

# print(timer_arr)
growth = [(timer_arr[-1]*i*log2(i))/(len(sizes)*log2(len(sizes))) for i in range(1, len(sizes))]
linear_growth = [(timer_arr[-1]*i)/len(sizes) for i in range(len(sizes))]

plt.plot(timer_arr)
plt.plot(growth, linestyle = "dashed")
plt.plot(linear_growth, linestyle = "dashed")
plt.show()
