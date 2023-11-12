from fem import *

# Example usage
file_path = "untitled.obj"
fem_grid = create_fem_grid(file_path)

print(len(fem_grid.nodes))
print(len(fem_grid.elements))