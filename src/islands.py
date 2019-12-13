# Coding interview problem from Anthem.AI: Find the sizes of the islands
# of 1s in a binary matrix.

# No islands
islands_empty = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

# Only land
islands_full = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]

# 2 islands of sizes 16, 4
islands_u = [
    [0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 1],
]

# 4 islands of sizes 28, 5, 3, 2
islands_donut = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0],
]

# 10 islands of size 1
islands_pts = [
    [0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0],
]

# Half land, randomly determined.  5 islands of sizes 1, 3, 3, 5, 6.
islands_rand = [
    [1, 0, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 1, 0],
    [1, 0, 0, 1, 0, 0],
]


def find_islands(matrix, empty_value=0):
    # Find the size of the matrix
    n_rows = len(matrix)
    if n_rows < 1:
        raise ValueError(f'Matrix has no rows: {matrix}')
    n_cols = len(matrix[0])
    if n_cols < 1:
        raise ValueError(f'Matrix has no columns: {matrix}')
    # Mapping of matrix coordinates to island IDs
    coord2id = {}
    # Scan the matrix
    for row_idx in range(n_rows):
        for col_idx in range(n_cols):
            # Skip any zero entries
            if matrix[row_idx][col_idx] == empty_value:
                continue
            # Look at the neighbors
            adjacent_ids = set()
            for neighbor_offset in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                neighbor_coord = (row_idx + neighbor_offset[0],
                                  col_idx + neighbor_offset[1])
                # Skip any neighbors that fall outside the matrix
                if not (0 <= neighbor_coord[0] < n_rows and
                        0 <= neighbor_coord[1] < n_cols):
                    continue
                if (matrix[neighbor_coord[0]][neighbor_coord[1]]
                        != empty_value and neighbor_coord in coord2id):
                    adjacent_ids.add(coord2id[neighbor_coord])
            # Label this coordinate based on its neighbors
            if len(adjacent_ids) == 0:
                # Add this coordinate to its own new island
                coord2id[row_idx, col_idx] = len(coord2id)
            elif len(adjacent_ids) == 1:
                # Add this coordinate its only adjacent island
                coord2id[row_idx, col_idx] = min(adjacent_ids)
            else:
                # Add this coordinate the first of its adjacent islands
                coord2id[row_idx, col_idx] = min(adjacent_ids)
                # Combine islands
                combine_ids(coord2id, adjacent_ids)
    return coord2id


def combine_ids(coord2id, ids):
    ids = set(ids)
    new_id = min(ids)
    for coord, id in coord2id.items():
        if id in ids and id != new_id:
            coord2id[coord] = new_id


def island_sizes(coord2id):
    counter = {}
    for coord, id in coord2id.items():
        count = counter.get(id, 0)
        counter[id] = count + 1
    return counter
