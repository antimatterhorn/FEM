from LinearAlgebra import *
import peanohilbert

class Node:
    def __init__(self, node_id, coordinates):
        self.id             = node_id
        self.coordinates    = coordinates

class Element:
    def __init__(self, element_id, nodes):
        self.id         = element_id
        self.nodes      = nodes
        self.area       = self.computeArea()
        self.centroid   = self.computeCentroid()
        self.connected_elements = set()

    def computeArea(self):
        vecs = []
        for node in self.nodes:
            vecs.append(Vector2d(*node.coordinates))
        return quadArea(*vecs)

    def computeCentroid(self):
        vecs = []
        for node in self.nodes:
            vecs.append(Vector2d(*node.coordinates))
        return quadCentroid(*vecs)

    def shared_nodes(self,element2):
        return set(self.nodes).intersection(set(element2.nodes))

    def shares_nodes(self,element2):
        return len(self.shared_nodes(element2)) > 0

class FiniteElementGrid:
    def __init__(self):
        self.nodes      = []
        self.elements   = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_element(self, element):
        self.elements.append(element)

    def sort_grid_peano(self):
        print("Sorting by space-filling curve...")
        # Calculate Peano-Hilbert index for each element based on its centroid
        element_indices = [(i, peanohilbert.index(int(element.centroid.x), int(element.centroid.y)), element)
                        for i, element in enumerate(self.elements)]

        # Sort elements based on Peano-Hilbert index and original order
        sorted_elements = [element for _, _, element in sorted(element_indices, key=lambda x: (x[1], x[0]))]
        self.elements = sorted_elements
        self.reindex()

    def reindex(self):
        for i in range(len(self.elements)):
            self.elements[i].id = i

    def build_connectivity_map(self):
        print("Building connectivity map...")
        connectivity_map = {element.id: [] for element in self.elements}

        for element1 in self.elements:
            for element2 in self.elements:
                if element1 != element2 and element1.shared_nodes(element2):
                    connectivity_map[element1.id].append(element2.id)

        self.connectivity_map = connectivity_map
        for element_id, connected_element_ids in connectivity_map.items():
            element = self.elements[element_id - 1]
            element.connected_elements.update(connected_element_ids)
        print("Connectivity built.")

def create_fem_grid_from_obj(file_path):
    print("Importing %s"%file_path)
    from fileIO import import_obj
    vertices, faces = import_obj(file_path)

    fem_grid = FiniteElementGrid()

    # Add nodes
    for node_id, coordinates in enumerate(vertices, start=1):
        node = Node(node_id, coordinates)
        fem_grid.add_node(node)

    # Add elements
    for element_id, face in enumerate(faces, start=1):
        element_nodes = [fem_grid.nodes[node_index-1] for node_index in face]
        element = Element(element_id, element_nodes)
        fem_grid.add_element(element)

    print("Created FEM grid with %d nodes and %d elements."%(len(fem_grid.nodes),len(fem_grid.elements)))
    return fem_grid

def on_import():
    from art import tprint
    tprint("eleForge",font="larry3d")
    print("~~~ v0.0.1 ~~~\n\n")

on_import()  
