class BoundaryConditions:
    def __init__(self, conditions=None):
        self.conditions = conditions or {}

    def set_conditions(self, node_id, constraint_type, constraint_value):
        self.conditions[node_id] = {
            "constraint_type": constraint_type,
            "constraint_value": constraint_value
        }

    def get_conditions(self, node_id):
        return self.conditions.get(node_id, {})


if __name__ == "__main__":
    # Example usage:
    boundary_conditions = BoundaryConditions()

    # Set conditions for a specific node
    node_id = 1
    constraint_type = "fixed"
    constraint_value = 0.0
    boundary_conditions.set_conditions(node_id, constraint_type, constraint_value)

    # Get conditions for the same node
    conditions = boundary_conditions.get_conditions(node_id)
    print(f"Boundary Conditions for Node {node_id}: {conditions}")
