from dataclasses import dataclass, field
from collections import defaultdict
from typing import Set, List, Dict, Optional

@dataclass
class DirectedGraph:
    size: int
    edges: Dict[int, Set[int]] = field(default_factory=lambda: defaultdict(set))
    
    def add_connection(self, source: int, target: int) -> None:
        """Add a directed edge if it doesn't exist."""
        if target not in self.edges[source]:
            self.edges[source].add(target)
    
    def get_neighbors(self, vertex: int) -> Set[int]:
        """Retrieve all neighbors of a vertex."""
        return self.edges[vertex]

class ComponentAnalyzer:
    def __init__(self, graph: DirectedGraph):
        self.graph = graph
        
    def _explore_component(self, start: int, visited: Set[int], 
                         graph_edges: Dict[int, Set[int]]) -> List[int]:
        """DFS exploration of a component."""
        component = []
        stack = [start]
        
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                component.append(current)
                stack.extend(v for v in graph_edges[current] if v not in visited)
        
        return component

class WeakComponents(ComponentAnalyzer):
    def find_components(self) -> List[List[int]]:
        """Find weakly connected components using undirected version of the graph."""

        undirected_edges = defaultdict(set)
        for source in range(self.graph.size):
            for target in self.graph.edges[source]:
                undirected_edges[source].add(target)
                undirected_edges[target].add(source)
        
        components = []
        visited = set()
        
        for vertex in range(self.graph.size):
            if vertex not in visited:
                component = self._explore_component(vertex, visited, undirected_edges)
                components.append(component)
        
        return components

class StrongComponents(ComponentAnalyzer):
    def _has_path(self, start: int, end: int) -> bool:
        """Check if there exists a path between two vertices."""
        visited = set()
        stack = [start]
        
        while stack:
            current = stack.pop()
            if current == end:
                return True
            if current not in visited:
                visited.add(current)
                stack.extend(self.graph.edges[current])
        
        return False
    
    def find_components(self) -> List[List[int]]:
        """Find strongly connected components using path existence checks."""
        components = []
        processed = set()
        
        for vertex in range(self.graph.size):
            if vertex not in processed:
                component = [vertex]
                for other in range(vertex + 1, self.graph.size):
                    if (other not in processed and 
                        self._has_path(vertex, other) and 
                        self._has_path(other, vertex)):
                        processed.add(other)
                        component.append(other)
                components.append(component)
        
        return components

def create_graph_from_matrix(matrix: List[List[int]]) -> DirectedGraph:
    """Convert adjacency matrix to DirectedGraph instance."""
    size = len(matrix)
    graph = DirectedGraph(size)
    
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 1:
                graph.add_connection(i, j)
    
    return graph


if __name__ == "__main__":
    test_matrix = [
        [0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    graph = create_graph_from_matrix(test_matrix)
    

    weak = WeakComponents(graph)
    weak_components = weak.find_components()
    print("Weakly Connected Components:")
    for idx, component in enumerate(weak_components, 1):
        print(f"Component {idx}: {component}")
    

    strong = StrongComponents(graph)
    strong_components = strong.find_components()
    print("\nStrongly Connected Components:")
    for idx, component in enumerate(strong_components, 1):
        print(f"Component {idx}: {[node + 1 for node in sorted(component)]}")