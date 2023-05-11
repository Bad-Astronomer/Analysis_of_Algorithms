def MCM(p, i, j):
    if i == j:
        return 0
    min = float("infinity")
     
    for k in range(i, j):
        count = (MCM(p, i, k) + MCM(p, k + 1, j) + p[i-1] * p[k] * p[j])
        min = -1*max(-1*min, -1*count) # converting max function into min

    return min

# Driver program to test above function
arr = [1, 2, 3, 4, 3]
print(f"Min no. of multiplications: {MCM(arr, 1, len(arr)-1)}")
