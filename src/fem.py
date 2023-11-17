from LinearAlgebra import *
import peanohilbert
import numpy as np

class Node:
    def __init__(self, node_id, coordinates):
        self.id             = node_id
        self.coordinates    = coordinates

class Element:
    def __init__(self, element_id, nodes, mat=None):
        self.id         = element_id
        self.nodes      = nodes
        self.area       = self.compute_area()
        self.centroid   = self.compute_centroid()
        self.connected_elements = set()
        self.material   = mat
        self.stiffness  = None

    def compute_area(self):
        vecs = []
        for node in self.nodes:
            vecs.append(Vector2d(*node.coordinates))
        return quadArea(*vecs)

    def compute_centroid(self):
        vecs = []
        for node in self.nodes:
            vecs.append(Vector2d(*node.coordinates))
        return quadCentroid(*vecs)

    def shared_nodes(self,element2):
        return set(self.nodes).intersection(set(element2.nodes))

    def shares_nodes(self,element2):
        return len(self.shared_nodes(element2)) > 0

    def calculate_xi_eta(self,xi, eta):
        # Given nodes: (x1, y1), (x2, y2), (x3, y3), (x4, y4)
        x1, y1 = self.nodes[0].coordinates
        x2, y2 = self.nodes[1].coordinates
        x3, y3 = self.nodes[2].coordinates
        x4, y4 = self.nodes[3].coordinates

        # Calculate lengths of edges in xi and eta directions
        h_xi = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        h_eta = ((x4 - x1)**2 + (y4 - y1)**2)**0.5

        # Calculate global coordinates (x, y) using xi and eta
        x = 0.25 * ((1 - xi)*(1 - eta)*x1 + (1 + xi)*(1 - eta)*x2 + (1 + xi)*(1 + eta)*x3 + (1 - xi)*(1 + eta)*x4)
        y = 0.25 * ((1 - xi)*(1 - eta)*y1 + (1 + xi)*(1 - eta)*y2 + (1 + xi)*(1 + eta)*y3 + (1 - xi)*(1 + eta)*y4)

        # Calculate local coordinates xi and eta
        local_xi = 2 * (x - x1) / h_xi - 1
        local_eta = 2 * (y - y1) / h_eta - 1

        return local_xi, local_eta

    def calculate_stiffness_matrix(self):
        nodes = self.nodes
        # Calculate lengths of edges in xi and eta directions
        h_xi = ((nodes[1].coordinates[0] - nodes[0].coordinates[0])**2 + (nodes[1].coordinates[1] - nodes[0].coordinates[1])**2)**0.5
        h_eta = ((nodes[3].coordinates[0] - nodes[0].coordinates[0])**2 + (nodes[3].coordinates[1] - nodes[0].coordinates[1])**2)**0.5

        # Calculate local coordinates xi and eta for the four nodes
        xi1, eta1 = self.calculate_xi_eta(-1, -1)
        xi2, eta2 = self.calculate_xi_eta(1, -1)
        xi3, eta3 = self.calculate_xi_eta(1, 1)
        xi4, eta4 = self.calculate_xi_eta(-1, 1)

        # Calculate derivatives of shape functions with respect to xi and eta
        dN1_dxi = 0.25 * (eta1 - eta3)
        dN1_deta = 0.25 * (xi1 - xi3)
        dN2_dxi = 0.25 * (eta2 - eta4)
        dN2_deta = 0.25 * (xi2 - xi4)
        dN3_dxi = 0.25 * (eta3 - eta1)
        dN3_deta = 0.25 * (xi3 - xi1)
        dN4_dxi = 0.25 * (eta4 - eta2)
        dN4_deta = 0.25 * (xi4 - xi2)

        # Assemble the B matrix
        B = np.array([
            [dN1_dxi, 0, dN2_dxi, 0, dN3_dxi, 0, dN4_dxi, 0],
            [0, dN1_deta, 0, dN2_deta, 0, dN3_deta, 0, dN4_deta],
            [dN1_deta, dN1_dxi, dN2_deta, dN2_dxi, dN3_deta, dN3_dxi, dN4_deta, dN4_dxi]
        ])

        # Calculate the Jacobian matrix
        J = np.array([
            [h_xi / 2, 0],
            [0, h_eta / 2]
        ])

        # Calculate the determinant of the Jacobian matrix
        detJ = np.linalg.det(J)

        # Calculate the stiffness matrix
        E = self.material.youngs_modulus
        #t = self.material.thickness right now just use 1.0
        t = 1

        factor = E * t * detJ / (h_xi * h_eta)

        stiffness_matrix = factor * np.dot(B.T, B)

        self.stiffness = stiffness_matrix

class FiniteElementGrid:
    def __init__(self):
        self.nodes      = []
        self.elements   = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_element(self, element):
        if element.material is not None:
            element.calculate_stiffness_matrix()
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

def create_fem_grid_from_obj(file_path, mat=None):
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
        element = Element(element_id, element_nodes, mat)
        fem_grid.add_element(element)

    print("Created FEM grid with %d nodes and %d elements."%(len(fem_grid.nodes),len(fem_grid.elements)))
    return fem_grid

def on_import():
    from art import tprint
    tprint("eleForge",font="larry3d")
    print("~~~ v0.0.1 ~~~\n\n")

on_import()  
