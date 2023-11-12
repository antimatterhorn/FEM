class Node:
    def __init__(self, node_id, coordinates):
        self.id = node_id
        self.coordinates = coordinates

class Element:
    def __init__(self, element_id, nodes):
        self.id = element_id
        self.nodes = nodes

class FiniteElementGrid:
    def __init__(self):
        self.nodes = []
        self.elements = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_element(self, element):
        self.elements.append(element)

def create_fem_grid(file_path):
    from objReader import import_obj
    vertices, faces = import_obj(file_path)

    fem_grid = FiniteElementGrid()

    # Add nodes
    for node_id, coordinates in enumerate(vertices, start=1):
        node = Node(node_id, coordinates)
        fem_grid.add_node(node)

    # Add elements
    for element_id, face in enumerate(faces, start=1):
        element_nodes = [fem_grid.nodes[node_index] for node_index in face]
        element = Element(element_id, element_nodes)
        fem_grid.add_element(element)

    return fem_grid


