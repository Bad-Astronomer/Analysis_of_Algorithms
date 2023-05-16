def isSafe(graph, color):
    for i in range(size):
        for j in range(1, size+1):
            if (graph[i][j] and color[i] == color[j]):
                return False
    return True


def graph_coloring(graph, m, i, color):
    if (i == size):
        if isSafe(graph, color):
            print(color)
            return True
        return False
    
    for j in range(1, m+1):
        color[i] = j

        if graph_coloring(graph, m, i+1, color):
            return True
        color[i] = 0
    return False 

graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0],
]

m = max(sum(i) for i in graph)

color = [0 for i in graph]

size = len(graph)

if(not graph_coloring(graph, m, 0, color)):
    print("No solution")