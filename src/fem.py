import vector_math_interface as VectorMath

class Node:
    def __init__(self, node_id, coordinates):
        self.id = node_id
        self.coordinates = VectorMath.Vector(*coordinates)

class Element:
    def __init__(self, element_id, nodes):
        self.id = element_id
        self.nodes = nodes

class FiniteElementGrid:
    def __init__(self, dimension):
        self.dimension = dimension
        self.nodes = []
        self.elements = []

    def add_node(self, coordinates):
        if len(coordinates) != self.dimension:
            raise ValueError("Invalid number of coordinates for the given dimension")
        node_id = len(self.nodes)
        node = Node(node_id, coordinates)
        self.nodes.append(node)

    def add_element(self, node_ids):
        if len(node_ids) != self.dimension + 1:
            raise ValueError(f"Invalid number of nodes for {self.dimension}D element")
        nodes = [self.nodes[node_id] for node_id in node_ids]
        element_id = len(self.elements)
        element = Element(element_id, nodes)
        self.elements.append(element)

# Example usage
if __name__ == "__main__":
    # Create a 3D finite element grid
    grid = FiniteElementGrid(dimension=3)

    # Add nodes
    grid.add_node((1.0, 2.0, 3.0))
    grid.add_node((4.0, 5.0, 6.0))
    grid.add_node((7.0, 8.0, 9.0))
    grid.add_node((10.0, 11.0, 12.0))

    # Add elements using node IDs
    grid.add_element([0, 1, 2, 3])
    
    # Print node and element information
    for node in grid.nodes:
        print(f"Node ID: {node.id}, Coordinates: {node.coordinates}")
    for element in grid.elements:
        print(f"Element ID: {element.id}, Node IDs: {[node.id for node in element.nodes]}")
