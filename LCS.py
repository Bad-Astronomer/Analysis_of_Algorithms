# Longest Common Subsequence

# Iterative lcs function
def calc_lcs(a,b):
    cost = [[0]*(len(b) + 1)]*(len(a) + 1)

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                cost[i][j] = cost[i - 1][j - 1] + 1
            else:
                cost[i][j] = max(cost[i-1][j], cost[i][j - 1])
    return cost

# Iterative path finding function
def get_path(a, b, cost, i, j): 
    seq = ""
    while(i != 0 and j != 0): 
        # go diagonal and add to subseq
        if a[i-1] == b[j-1]:
            i-=1
            j-=1
            seq += a[i]
        # go up or left based on arrow (bigger value)
        else:
            if cost[i-1][j] > cost[i][j-1]:
                i-=1
            else:
                j-=1
    # invert and return string
    return seq[::-1]

a = "QueSeraSera"
b = "CoursEra"
cost = calc_lcs(a,b)
lcs_str = get_path(a, b, cost, len(a), len(b))
print(f"Longest common subsequence: {lcs_str}\n")\

for row in cost:
    print(row)
 
