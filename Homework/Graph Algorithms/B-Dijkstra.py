import heapq

def dijkstra (graph, start):
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > shortest_distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return shortest_distances
    
graph = {}
n_vertices = int(input())
while True:
    input_list = input().split(" ")
    if "-1" in input_list:
        break
    x, y, w = map(int, input_list)
    if x not in graph: graph[x] = {y : w}
    else:
        graph[x][y] = w
    if y not in graph: graph[y] = {x : w}
    else:
        graph[y][x] = w 
start = int(input())
result = dijkstra(graph, start)
for i in range(n_vertices):
    print(f'{result[i]}\n')