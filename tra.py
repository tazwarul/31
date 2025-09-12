from itertools import combinations

def tsp(graph):
    n = len(graph)
    # dp[mask][i] = minimum cost to reach subset 'mask' ending at city 'i'
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Start at city 0

    for mask in range(1 << n):
        for u in range(n):
            if not (mask & (1 << u)): 
                continue
            for v in range(n):
                if mask & (1 << v): 
                    continue
                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + graph[u][v])

    # Return to start (city 0)
    return min(dp[(1 << n) - 1][i] + graph[i][0] for i in range(n))

# Example graph (adjacency matrix)
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print("Minimum traveling cost:", tsp(graph))
