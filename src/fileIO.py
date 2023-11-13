def import_obj(file_path, axes="(x,z)"):
    assert axes in ["(x,y)","(x,z)","(y,z)"]
    
    vertices = []
    faces = []

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()

            if not parts:
                continue

            if parts[0] == 'v':
                # Extract x, y, z coordinates
                x, y, z = map(float, parts[1:4])
                if axes == "(x,z)":
                    vertices.append((x, z))  # Use x and z coordinates
                elif axes == "(x,y)":
                    vertices.append((x, y))
                else:
                    vertices.append((y, z))
            elif parts[0] == 'f':
                # Extract vertex indices of a face
                face = [int(index.split('/')[0]) for index in parts[1:]]
                faces.append(face)

    return vertices, faces
    

def export_to_vtk(file_path, fem_grid):
    with open(file_path, 'w') as file:
        file.write("# vtk DataFile Version 3.0\n")
        file.write("FEM Grid Exported for VisIt\n")
        file.write("ASCII\n")
        file.write("DATASET UNSTRUCTURED_GRID\n")

        # Write node coordinates
        file.write(f"POINTS {len(fem_grid.nodes)} double\n")
        for node in fem_grid.nodes:
            file.write(f"{node.coordinates[0]} 0.0 {node.coordinates[1]}\n")

        # Write element connectivity
        total_nodes = sum(len(element.nodes) for element in fem_grid.elements)
        file.write(f"CELLS {len(fem_grid.elements)} {len(fem_grid.elements) + total_nodes}\n")
        for element in fem_grid.elements:
            node_ids = [node.id - 1 for node in element.nodes]
            file.write(f"{len(element.nodes)} {' '.join(map(str, node_ids))}\n")

        file.write(f"CELL_TYPES {len(fem_grid.elements)}\n")
        for element in fem_grid.elements:
            if len(element.nodes) == 3:
                file.write("5 ")  # VTK_TRIANGLE
            elif len(element.nodes) == 4:
                file.write("9 ")  # VTK_QUAD
            # Add more cases for different element types as needed

        file.write("\n")

        # Write nodal values (MESH variable)
        file.write("POINT_DATA " + str(len(fem_grid.nodes)) + "\n")
        file.write("SCALARS MESH double 1\n")
        file.write("LOOKUP_TABLE default\n")
        for node in fem_grid.nodes:
            # You can replace this with your actual nodal values for the "MESH" variable
            file.write(f"{node.coordinates[0]}\n")