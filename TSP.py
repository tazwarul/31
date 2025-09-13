from itertools import permutations
def tsp(graph):
    n = len(graph)
    best_cost, best_path = float('inf'), None
    
    for perm in permutations(range(1, n)):
        path = (0,) + perm + (0,)
        cost = sum(graph[path[i]][path[i+1]] for i in range(n))
        if cost < best_cost:
            best_cost, best_path = cost, path
    return best_path, best_cost

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
path, cost = tsp(graph)
print("Optimal Path:", [p+1 for p in path])
print("Minimum Cost:", cost)