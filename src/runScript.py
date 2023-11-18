from fem import *
from material import *
from load_conditions import *

# Create the material
Mat = Material(properties=Materials.steel)
print(Mat)


# Example usage
file_path = "example.obj"
fem_grid = create_fem_grid_from_obj(file_path,mat=Mat)
fem_grid.sort_grid_peano()

#from ConnectivityMap import build_connectivity_map
#build_connectivity_map(fem_grid.ndoes,fem_grid.elements)
fem_grid.build_connectivity_map()

loads = LoadConditions()
loads.add_load_condition(node_id=1, load_vector=(100.0, 0.0))
loads.add_load_condition(node_id=2, load_vector=(0.0, 50.0))
#apply_load_conditions(loads,fem_grid)


from fileIO import *

export_to_vtk("example.vtk",fem_grid)