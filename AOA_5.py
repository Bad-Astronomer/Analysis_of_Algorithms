# KnapSack

def knapSack(weights, profits, capacity):
    result_arr, max_profit = [0 for i in weights], 0
    pw_arr = sorted(zip(weights, profits), key = lambda x: -x[1]/x[0])
    print(f"P/W:\t\t {pw_arr}")
    print(f"P/W ratio:\t {[x[1]/x[0] for x in pw_arr]}")
    
    for pw in pw_arr:
        if(not capacity):
            break
        if(capacity >= pw[0]):
            capacity -= pw[0]
            max_profit += pw[1]
            result_arr[weights.index(pw[0])] = 1 # wont work for non-unique weights
            #temporary fix
            # if(weights.index(pw[0]) == profits.index(pw[1])):
            #     result_arr[weights.index(pw[0])] = 1 
        else:
            fraction = capacity/pw[0]
            capacity = 0
            max_profit += pw[1]*fraction
            result_arr[weights.index(pw[0])] = fraction 
    return result_arr, max_profit


weights = [4, 5, 2, 9, 1]
profits = [100, 150, 90, 200, 1]
capacity = 15

print(f"Input:\t\t {[i for i in zip(weights, profits)]}")


print(f"Output:\t\t{knapSack(weights, profits, capacity)}")

