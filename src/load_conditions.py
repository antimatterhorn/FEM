from LinearAlgebra import *
import numpy as np
from scipy.sparse import lil_matrix

class LoadCondition:
    def __init__(self, node_id, load_vector):
        self.node_id = node_id
        self.load_vector = Vector2d(*load_vector)

    def __repr__(self):
        return f"LoadCondition(node_id={self.node_id}, load_vector={self.load_vector})"

class LoadConditions:
    def __init__(self):
        self.conditions = []

    def add_load_condition(self, node_id, load_vector):
        condition = LoadCondition(node_id, load_vector)
        self.conditions.append(condition)

    def __repr__(self):
        return f"LoadConditions(conditions={self.conditions})"

def apply_load_conditions(loads, fem_grid):
    num_nodes = len(fem_grid.nodes)

    for element in fem_grid.elements:
        for load in loads.conditions:
            if load.node_id == element.id:
                element.loads.append(load)

    K_global = lil_matrix((2 * num_nodes, 2 * num_nodes))
    F_global = np.zeros(2 * num_nodes)
    # Loop through each element
    for element in fem_grid.elements:
        # Assuming element stiffness matrix is calculated using your method
        K_element = element.stiffness

        # Assuming you have the element load vector
        F_element = element.calculate_load_vector()

        # Assemble stiffness matrix into global matrix
        for i, ni in enumerate(element.node_ids):
            for j, nj in enumerate(element.node_ids):
                K_global[2 * ni:2 * (ni + 1), 2 * nj:2 * (nj + 1)] += K_element[i * 2:(i + 1) * 2, j * 2:(j + 1) * 2]

        # Assemble load vector into global vector
        for i, ni in enumerate(element.node_ids):
            F_global[2 * ni:2 * (ni + 1)] += F_element[i * 2:(i + 1) * 2]

    # Apply external loads
    for load_condition in loads.conditions:
        node_id = load_condition.node_id
        F_global[2 * node_id:2 * (node_id + 1)] += load_condition.load_vector.values


if __name__ == "__main__":
    # Example Usage:
    loads = LoadConditions()
    loads.add_load_condition(node_id=1, load_vector=(100.0, 0.0))
    loads.add_load_condition(node_id=2, load_vector=(0.0, 50.0))

    print(loads)
