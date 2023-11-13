from fem import *

# Example usage
file_path = "example.obj"
fem_grid = create_fem_grid_from_obj(file_path)

print(len(fem_grid.nodes))
print(len(fem_grid.elements))

for i in range(15):
    print(fem_grid.nodes[i].coordinates)

from fileIO import *

export_to_vtk("example.vtk",fem_grid)