from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)
    
    def add_edge(self, source, destination):
        self.adjacency_list[source].append(destination)
    
    def path_exists(self, start_node, end_node):
        visited_nodes = set()
        return self._depth_first_search(start_node, end_node, visited_nodes)
    
    def _depth_first_search(self, current_node, target_node, visited_nodes):
        if current_node == target_node:
            return True
        visited_nodes.add(current_node)
        for neighbor in self.adjacency_list[current_node]:
            if neighbor not in visited_nodes:
                if self._depth_first_search(neighbor, target_node, visited_nodes):
                    return True
        return False

def run_graph():
    graph_instance = Graph()
    
    edge_list = [
        (1, 2), (2, 5), (3, 6), 
        (4, 6), (4, 7), (6, 7)
    ]
    
    for source, destination in edge_list:
        graph_instance.add_edge(source, destination)
    
    try:
        start_node = int(input("Please enter the start node: "))
        end_node = int(input("Please enter the end node: "))
        
        if graph_instance.path_exists(start_node, end_node):
            print(f"True: A path exists between node {start_node} and node {end_node}.")
        else:
            print(f"False: No path exists between node {start_node} and node {end_node}.")
    except ValueError:
        print("Invalid input. Please enter integers for the nodes.")

if __name__ == "__main__":
    run_graph()