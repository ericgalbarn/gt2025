import heapq

def generate_weighted_adjacency_matrix():
    num_nodes = 9
    adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]
    edge_list = [
        (1, 2, 4), (1, 5, 1), (1, 7, 2),
        (2, 3, 7), (2, 6, 5),
        (3, 4, 1), (3, 6, 8),
        (4, 6, 6), (4, 7, 4), (4, 8, 3),
        (5, 6, 9), (5, 7, 10),
        (6, 9, 2),
        (7, 9, 8),
        (8, 9, 1),
        (9, 8, 7)
    ]
    for start, end, weight in edge_list:
        adjacency_matrix[start - 1][end - 1] = weight
        adjacency_matrix[end - 1][start - 1] = weight
    return adjacency_matrix

def display_adjacency_matrix(matrix):
    for line in matrix:
        print(" ".join(f"{value:2}" for value in line))

def prim_algorithm(adjacency_matrix, starting_node):
    node_count = len(adjacency_matrix)
    visited_nodes = [False] * node_count
    priority_queue = [(0, starting_node, -1)]
    mst_edges = []
    total_weight = 0
    
    while priority_queue:
        current_weight, current_node, parent_node = heapq.heappop(priority_queue)
        if visited_nodes[current_node]:
            continue
        visited_nodes[current_node] = True
        total_weight += current_weight
        if parent_node != -1:
            mst_edges.append((parent_node + 1, current_node + 1, current_weight))
        for neighbor in range(node_count):
            if not visited_nodes[neighbor] and adjacency_matrix[current_node][neighbor] > 0:
                heapq.heappush(priority_queue, (adjacency_matrix[current_node][neighbor], neighbor, current_node))
    return mst_edges, total_weight

def kruskal_algorithm(adjacency_matrix):
    node_count = len(adjacency_matrix)
    edge_list = []
    for i in range(node_count):
        for j in range(i + 1, node_count):
            if adjacency_matrix[i][j] > 0:
                edge_list.append((adjacency_matrix[i][j], i, j))
    edge_list.sort()
    parent = list(range(node_count))
    rank = [0] * node_count
    mst_edges = []
    total_weight = 0

    def find_root(node):
        if parent[node] != node:
            parent[node] = find_root(parent[node])
        return parent[node]

    def union_sets(node1, node2):
        root1 = find_root(node1)
        root2 = find_root(node2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

    for weight, u, v in edge_list:
        if find_root(u) != find_root(v):
            union_sets(u, v)
            mst_edges.append((u + 1, v + 1, weight))
            total_weight += weight
    return mst_edges, total_weight

if __name__ == "__main__":
    adjacency_matrix = generate_weighted_adjacency_matrix()
    display_adjacency_matrix(adjacency_matrix)
    root_node = int(input("\nEnter the root node (1-9): ")) - 1
    print("\nPrim's Algorithm:")
    prim_edges, prim_weight = prim_algorithm(adjacency_matrix, root_node)
    print("Edges in MST:", prim_edges)
    print("Total Weight of MST:", prim_weight)
    print("\nKruskal's Algorithm:")
    kruskal_edges, kruskal_weight = kruskal_algorithm(adjacency_matrix)
    print("Edges in MST:", kruskal_edges)
    print("Total Weight of MST:", kruskal_weight)