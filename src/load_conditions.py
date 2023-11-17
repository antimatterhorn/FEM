from LinearAlgebra import *

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


if __name__ == "__main__":
    # Example Usage:
    loads = LoadConditions()
    loads.add_load_condition(node_id=1, load_vector=(100.0, 0.0))
    loads.add_load_condition(node_id=2, load_vector=(0.0, 50.0))

    print(loads)
