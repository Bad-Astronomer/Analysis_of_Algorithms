import matplotlib.pyplot as plt
from tqdm import tqdm
from math import log2


global counter
counter_arr = []

def mergeSort(arr, s, e):
    global counter 
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
            counter += 1
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
            counter += 1
            arr[e], arr[s] = arr[s], arr[e]

    return arr[s:e+1]


sizes = [10*i for i in range(1,500)]

for size in tqdm(sizes):
    counter = 0
    arr = [size-i for i in range(size)]
    arr = mergeSort(arr, 0, len(arr)-1)
    counter_arr.append(counter)


growth = [(counter_arr[-1]*i*log2(i))/(len(sizes)*log2(len(sizes))) for i in range(1, len(sizes)+1)]
plt.plot(counter_arr)
plt.plot(growth, linestyle = "dashed")
plt.xlabel("No. of samples")
plt.ylabel("No. of comparisons")
plt.show()

for i, n in enumerate(sizes):
    print(f"{n}\t {counter_arr[i]}\t{growth[i]}")
