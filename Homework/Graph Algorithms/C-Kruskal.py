def kruskalMST(graph: list, n_vertices: int):
    '''
    Find the minimum spanning tree (MST) of a connected graph using Kruskal's algorithm
    
    Parameter:
        graph: list
            The graph represented as an edge list
        n_vertices: int
            The number of vertices in the graph
            
    Return:
        The total weight of the MST
    '''
    # This is the implementation of Disjoint set union data structure
    # It is used to quickly check if 2 vertices is in a single connected component
    # You can also write this part in a seperated class
    root = [i for i in range(n_vertices)] # The 'root' of a set (you can think of a set as a tree)
    rank = [1 for i in range(n_vertices)] # The 'rank' of a set (the height of the tree)
    
    # This function is used to find the set containing a vertex
    def find_set(vertex):
        nonlocal root
        # The vertex is the root
        if root[vertex] == vertex:
            return vertex
        # Store the root of a vertex as the root of its parent so that we can find it faster in the future
        root[vertex] = find_set(root[vertex])
        # Return the root
        return root[vertex]
    
    # This function is used to join 2 sets containing vertex_1 and vertex_2 respectively
    def join_sets(vertex_1, vertex_2):
        nonlocal root, rank
        set_v1 = find_set(vertex_1)
        set_v2 = find_set(vertex_2)
        # Two vertices are in the same set
        if set_v1 == set_v2:
            return
        # The set with lower rank should be moved under the other to minimize the rank of the resulting set
        # We only care about the rank of the root
        if rank[set_v1] < rank[set_v2]:
            root[set_v1] = set_v2
        elif rank[set_v2] < rank[set_v1]:
            root[set_v2] = set_v1
        else:
            # Two sets have the same rank
            # Moving one under another will result in a set whose rank is one greater
            root[set_v2] = set_v1
            rank[set_v1] += 1
    
    # This is the main implementation of Kruskal algorithm
    def kruskal_main():
        nonlocal graph, root, rank
        total_weight = 0
        n_edges_selected = 0
        graph.sort(key=lambda x: x[2])  # Sort the graph list in ascending order of weight

        for edge in graph:
            v1, v2, weight = edge
            if find_set(v1) == find_set(v2):
                continue
            total_weight += weight
            join_sets(v1, v2)
            n_edges_selected += 1
            if n_edges_selected == n_vertices - 1:
                return total_weight

    return kruskal_main()


graph = []
n_vertices = int(input())
vertex_1, vertex_2, weight = map(int, input().split())
while vertex_1 != -1:
    graph.append((min(vertex_1, vertex_2), max(vertex_1, vertex_2), weight))
    vertex_1, vertex_2, weight = map(int, input().split())
weight = kruskalMST(graph, n_vertices)
print(weight)