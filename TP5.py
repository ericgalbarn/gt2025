import sys

def build_adjacency_matrix(edge_list):
    vertex_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L', 'M']
    num_vertices = len(vertex_labels)
    index_map = {label: idx for idx, label in enumerate(vertex_labels)}
    
    adjacency_matrix = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    
    for start, end, weight in edge_list:
        adjacency_matrix[index_map[start]][index_map[end]] = weight
        adjacency_matrix[index_map[end]][index_map[start]] = weight
    
    return adjacency_matrix, vertex_labels, index_map

def find_shortest_path(graph, start_vertex, end_vertex, vertex_labels):
    num_vertices = len(graph)
    distances = [float('inf')] * num_vertices
    previous = [None] * num_vertices
    visited = [False] * num_vertices
    
    distances[start_vertex] = 0
    
    for _ in range(num_vertices):
        min_distance = float('inf')
        current_vertex = -1
        for vertex in range(num_vertices):
            if not visited[vertex] and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                current_vertex = vertex
        
        if current_vertex == -1:
            break
            
        visited[current_vertex] = True
        
        for neighbor in range(num_vertices):
            if (not visited[neighbor] and 
                graph[current_vertex][neighbor] != float('inf') and 
                distances[current_vertex] + graph[current_vertex][neighbor] < distances[neighbor]):
                distances[neighbor] = distances[current_vertex] + graph[current_vertex][neighbor]
                previous[neighbor] = current_vertex
    
    path = []
    current = end_vertex
    while current is not None:
        path.append(vertex_labels[current])
        current = previous[current]
    path.reverse()
    
    return path, distances[end_vertex]

def run_program():
    edge_list = [
        ('A', 'C', 1), ('A', 'B', 4),
        ('B', 'F', 3),
        ('C', 'F', 7), ('C', 'D', 8),
        ('D', 'H', 5),
        ('E', 'F', 1), ('E', 'H', 2), ('E', 'L', 2),
        ('F', 'H', 1),
        ('H', 'G', 3), ('H', 'M', 7), ('H', 'L', 6),
        ('G', 'L', 4), ('G', 'M', 4),
        ('L', 'M', 1)
    ]
    
    adjacency_matrix, vertex_labels, index_map = build_adjacency_matrix(edge_list)
    
    while True:
        source_vertex = input("\nEnter source vertex (A-M): ").upper()
        target_vertex = input("Enter target vertex (A-M): ").upper()
        
        if source_vertex in index_map and target_vertex in index_map:
            break
        print("Invalid vertices! Please try again.")
    
    path, total_weight = find_shortest_path(adjacency_matrix, index_map[source_vertex], index_map[target_vertex], vertex_labels)
    
    print(f"\nShortest path from {source_vertex} to {target_vertex}:")
    print(" -> ".join(path))
    print(f"Total weight: {total_weight}")

if __name__ == "__main__":
    run_program()
