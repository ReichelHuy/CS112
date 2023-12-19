from collections import defaultdict

def DFS(graph: defaultdict(list), start: int, visited=None) -> None:
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            DFS(graph, neighbor, visited)

def BFS(graph: defaultdict(list), start: int) -> None:
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        current = queue.pop(0)
        print(current, end=" ")

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    
T = int(input()) #number of test cases
while T:
    n = int(input()) #number of edges
    edge_list = []
    for _ in range(n):
        x, y = map(int, input().split())
        edge_list.append([x, y])
    graph = defaultdict(list) #edge adjacency list
    for edge in edge_list:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    start = int(input()) #node start
    print("DFS: ")
    DFS(graph, start)
    print()
    print("BFS: ")
    BFS(graph, start)
    print()
    T -= 1