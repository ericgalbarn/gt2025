def create_adjacency_matrix(vertices_list, edges_list):
    size = len(vertices_list)
    matrix = [[0] * size for _ in range(size)]
    index_map = {vertex: idx for idx, vertex in enumerate(vertices_list)}

    for start, end in edges_list:
        matrix[index_map[start]][index_map[end]] = 1

    return matrix

def generate_tree_from_edges(edges_list):
    """
    Constructs a binary tree-like structure from the edges.
    Assumes edges describe a tree.
    """
    class Node:
        def __init__(self, key):
            self.key = key
            self.left_child = None
            self.right_child = None

    node_dict = {}


    for start, end in edges_list:
        if start not in node_dict:
            node_dict[start] = Node(start)
        if end not in node_dict:
            node_dict[end] = Node(end)


        if node_dict[start].left_child is None:
            node_dict[start].left_child = node_dict[end]
        else:
            node_dict[start].right_child = node_dict[end]

    return node_dict

def inorder_traverse(node):
    if node is None:
        return []


    return inorder_traverse(node.left_child) + [node.key] + inorder_traverse(node.right_child)


if __name__ == '__main__':
    vertices = [1, 2, 3, 4, 5, 6, 7, 8]
    edges = [(1, 2), (1, 3), (2, 5), (2, 6), (3, 4), (4, 8), (5, 7)]


    adjacency_matrix = create_adjacency_matrix(vertices, edges)
    print("Adjacency Matrix:")
    for row in adjacency_matrix:
        print(row)

    tree_nodes = generate_tree_from_edges(edges)

    while True:
        try:
            start_node = int(input("Enter the starting node for Inorder traversal: "))
            if start_node not in tree_nodes:
                print("Invalid node label. Please enter a valid node label.")
                continue

            root_node = tree_nodes[start_node]
            inorder_result = inorder_traverse(root_node)
            print("\nInorder Traversal Result starting from node {}:".format(start_node))
            print(" ".join(map(str, inorder_result)))
            break
        except ValueError:
            print("Please enter a valid integer.")