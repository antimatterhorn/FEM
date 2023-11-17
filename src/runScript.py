from fem import *

# Example usage
file_path = "example.obj"
fem_grid = create_fem_grid_from_obj(file_path)
fem_grid.sort_grid_peano()

#from ConnectivityMap import build_connectivity_map
#build_connectivity_map(fem_grid.ndoes,fem_grid.elements)
fem_grid.build_connectivity_map()




from fileIO import *

export_to_vtk("example.vtk",fem_grid)