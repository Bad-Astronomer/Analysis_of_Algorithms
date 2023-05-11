# All pair shortest path

global inf
inf = float("inf")

graph = [
    [0, 50, 30, 10, inf, inf],
    [inf, 0, 10, 15, inf, inf],
    [inf, inf, 0, inf, 30, inf],
    [20, inf, inf, 0, 15, inf],
    [inf, 20, 35, inf, 0, inf],
    [inf, inf, inf, inf, 3, 0]
]

def apsp():
    n = len(graph) # since graph is a square matrix always
    cost = [[j for j in i] for i in graph] # init cost matrix

    path = [[f"{i+1}" for j in range(len(graph))] for i in range(len(graph))]
    for i in range(len(graph)):
            for j in range(len(graph)):
                if graph[i][j] < inf:
                    path[i][j] = f"{i+1} -> {j+1}"
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(cost[i][j] > cost[i][k] + cost[k][j]):
                    cost[i][j] = cost[i][k] + cost[k][j]
                    path[i][j] = f"{path[i][k]} -> {j+1}"

    print("Input")
    for i in graph:
        print(i)

    print("\nOutput")
    for i in cost:
        print(i)
        
    print("\nPath")
    for i in path:
        print(i)

apsp()

