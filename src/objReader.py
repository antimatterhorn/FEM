def import_obj(file_path):
    vertices, faces = [], []

    with open(file_path, 'r') as file:
        for line in file:
            tokens = line.strip().split()

            if not tokens:
                continue  # Skip empty lines

            if tokens[0] == 'v':
                # Take only x and z for 2D (ignoring y)
                vertex = list(map(float, tokens[1:3]))
                vertices.append(vertex)
            elif tokens[0] == 'f':
                face = [int(index.split('/')[0]) - 1 for index in tokens[1:]]
                faces.append(face)

    return vertices, faces