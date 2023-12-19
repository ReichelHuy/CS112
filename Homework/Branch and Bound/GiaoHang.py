import sys
from itertools import permutations

def calculate_bound(graph, path):
    # Tinh gioi han tren dua tren duong di da chon
    bound = 0 
    n = len(graph)
    for i in range(n - 1):
        u = path[i]
        v = path[i + 1]
        bound += graph[u][v]
    return bound

def branch_and_bound(graph):
    n = len(graph)
    min_time = sys.maxsize
    cities = list(range(1, n))
    permutations_cities = permutations(cities)

    for perm in permutations_cities:
        path = [0] + list(perm) + [0]
        bound = calculate_bound(graph, path)
        if bound < min_time:
            visited = [False] * n
            visited[0] = True
            time = backtrack(graph, visited, path, 1, 0, bound)
            if time < min_time:
                min_time = time

    if min_time == sys.maxsize:
        return -1
    return min_time

def backtrack(graph, visited, path, count, total, min_time):
    n = len(graph)
    if count == n:
        # Da di qua tat ca cac thanh pho
        return total + graph[path[-1]][0]

    curr_city = path[-1]
    for next_city in range(n):
        if not visited[next_city]:
            visited[next_city] = True
            path.append(next_city)
            bound = calculate_bound(graph, path)
            if bound < min_time:
                time = backtrack(graph, visited, path, count + 1, total + graph[curr_city][next_city], min_time)
                if time < min_time:
                    min_time = time
            path.pop()
            visited[next_city] = False

    return min_time

# Input 
n, m = map(int, input().split())
graph = [[sys.maxsize] * n for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u - 1][v - 1] = w
    graph[v - 1][u - 1] = w

# Result
result = branch_and_bound(graph)
print(result)