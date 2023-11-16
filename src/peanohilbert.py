def index(x, y, depth=4, xi=0, yi=0):
    if depth == 0:
        return 0
    else:
        mask = 1 << (depth - 1)
        bit_x = (x & mask) >> (depth - 1)
        bit_y = (y & mask) >> (depth - 1)

        sub_index = index(x & ~mask, y & ~mask, depth - 1, xi, yi)

        if bit_x == 0 and bit_y == 0:
            xi, yi = yi, xi

        if bit_x == 1 and bit_y == 0:
            xi = mask - 1 - xi
            yi = mask - 1 - yi

        return (bit_x | (bit_y << 1)) | ((xi | (yi << 1)) << (2 * depth - 2)) | (sub_index << (2 * depth))
