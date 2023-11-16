from fem import *

# Example usage
file_path = "example.obj"
fem_grid = create_fem_grid_from_obj(file_path)
fem_grid.build_connectivity_map()
sgrid = fem_grid.sort_elements_connected()

# fem_grid.sort_elements_connected()
# fem_grid.reindex()


from fileIO import *

export_to_vtk("example.vtk",fem_grid)