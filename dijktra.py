exemple = [
    [0, 4, 1, -1],
    [4, 0, 2, 1],
    [1, 2, 0, -1],
    [-1, 1, -1, 0]
]


def explore(x, dist, graphe, vus):
    n = len(graphe)
    if i == n-1:
        return dist
    if not vus[x]:
        vus[x] = True
        for i in range(n):
            
