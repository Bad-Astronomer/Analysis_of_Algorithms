from time import time
import matplotlib.pyplot as plt
from tqdm import tqdm
import copy

global timer_arr
timer_arr = []


def timer(func):
  global time_arr

  def timer(*args, **kwargs):
    t1 = time()
    result = func(*args, **kwargs)
    t2 = time()

    #print(f'{func.__name__}: {(t2-t1):.4f}s')
    timer_arr.append((t2-t1))
    return result
  return timer

@timer
def insertion_sort(arr):
  for j in range(1, len(arr)):
      while arr[j] < arr[j-1] and j!=0:
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j -= 1 

@timer
def selection_sort(arr):
  for i in range(len(arr)):
    min_index = i
    for j in range(i, len(arr)):
      if(arr[j] < arr[min_index]):
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]


start = 100 #starting size
samples = 50 #no. of samples
stride = 50

samples *= stride
samples += start
x_axis = [i for i in range(samples)]

for i in tqdm(range(start,samples,stride)):
  #arr = [random.randint(1,100) for j in range(i)]
  arr = [i-j for j in range(i)] #worst case
  selection_sort(arr)

selection_sort_timer_arr = copy.deepcopy(timer_arr)
timer_arr.clear()

for i in tqdm(range(start,samples,stride)):
  #arr = [random.randint(1,100) for j in range(i)]
  arr = [i-j for j in range(i)] #worst case
  insertion_sort(arr)


#for n^2 graph (insertion sort)
max_t = max(timer_arr)
max_index = timer_arr.index(max_t)
n_sq_arr = [(i**2/max_index**2)*max_t for i in range(max_index+1)]

plt.plot(timer_arr) #blue
plt.plot(n_sq_arr, linestyle = "dashed") #orange
plt.xlabel("No. of Samples")
plt.ylabel("Time (s)")
plt.show()

#for n^2 graph (selection sort)
max_t = max(selection_sort_timer_arr)
max_index = selection_sort_timer_arr.index(max_t)
n_sq_arr = [(i**2/max_index**2)*max_t for i in range(max_index+1)]

plt.plot(selection_sort_timer_arr) #blue
plt.plot(n_sq_arr, linestyle = "dashed") #orange
plt.xlabel("No. of Samples")
plt.ylabel("Time (s)")
plt.show()