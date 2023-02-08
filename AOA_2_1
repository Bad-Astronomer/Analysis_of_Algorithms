import random
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt


global counter, counter_arr
counter, counter_arr = 0, []

def binarySearch(arr, key, low, high):
    global counter
    counter += 1 
    if low < high: #more than 1 element
        mid = (low + high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key: 
            return binarySearch(arr, key, mid+1, high) #search last half
        elif arr[mid] > key:
            return binarySearch(arr, key, low, mid-1) #search first half
    elif arr[low] == key: #1 element 
        return low
    else: #key not found
        print("Key Not Found")
        return -1



def iterativeBinarySearch(arr, key, low, high):
    global counter
    while low < high: 
        counter += 1 
        mid = (low+high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key: 
            low = mid + 1 #search last half
        elif arr[mid] > key:
            high = mid - 1 #search first half
    if arr[low] == key: #1 element 
        counter += 1
        return low
    else: #key not found
        print("Key Not Found")
        return -1
    

num = 10
arr = []

sizes = [1000*i for i in range(1,50)]

for size in tqdm(sizes):
    counter = 0
    for i in range(size):
        num += random.randint(1,5) #random sorted array
        arr.append(num)

    #ground_truth = random.randint(1, size)
    ground_truth = 1
    key = arr[ground_truth]                                                                                                                                                                                                                                                                                            
    ind = binarySearch(arr, key, 0, size)
    counter_arr.append(counter)


sizes = [10*i for i in sizes]
#counter_arr.append(0)
growth = np.log(sizes)
growth += counter_arr[0] - growth[0]

print(growth)
print(counter_arr)

plt.plot(counter_arr)
plt.plot(growth, linestyle = "dashed")
plt.xlabel("No. of Samples")
plt.ylabel("No. of comparisons")
plt.show()

