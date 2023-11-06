# fem_interface.py (Python interface for FEM namespace using cppyy)

import cppyy
from vector_math_interface import VectorMathWrapper

# Load the fem.cpp file as a Python module using cppyy
cppyy.include("fem.cpp")

# Import the FEM namespace
FEM = cppyy.gbl.FEM

class NodeWrapper:
    def __init__(self, nodeId, coordinates):
        vector = VectorMathWrapper.create_vector(*coordinates)
        self.node = FEM.Node(nodeId, vector)

class ElementWrapper:
    def __init__(self, elementId, nodes):
        node_list = [node.node for node in nodes]
        self.element = FEM.Element(elementId, node_list)

class FiniteElementGridWrapper:
    def __init__(self):
        self.grid = FEM.FiniteElementGrid()

    def add_node(self, coordinates):
        vector = VectorMathWrapper.create_vector(*coordinates)
        self.grid.addNode(vector)

    def add_element(self, nodes):
        self.grid.addElement([node.node for node in nodes])

# Example usage
if __name__ == "__main__":
    node1 = NodeWrapper(1, [0.0, 0.0, 0.0])
    node2 = NodeWrapper(2, [1.0, 0.0, 0.0])
    node3 = NodeWrapper(3, [1.0, 1.0, 0.0])

    element1 = ElementWrapper(1, [node1, node2, node3])

    fem_grid = FiniteElementGridWrapper()
    fem_grid.add_node([0.0, 0.0, 0.0])
    fem_grid.add_node([1.0, 0.0, 0.0])
    fem_grid.add_node([1.0, 1.0, 0.0])

    fem_grid.add_element([node1, node2, node3])
