#    Main Author(s): Lorenzo Ramos
#    Main Reviewer(s): Dev Jigishkumar Shah, Yunus Gumus

from a1_partc import Queue


def get_overflow_list(grid):
    # Define a helper function to count the number of neighboring cells
    def count_neighbors(row, col):
        neighbors = 0
        if row > 0:
            neighbors += 1
        if row < len(grid) - 1:
            neighbors += 1
        if col > 0:
            neighbors += 1
        if col < len(grid[0]) - 1:
            neighbors += 1
        return neighbors

    # Define a function to check if a cell overflows based on its value and neighbors
    def is_overflow(row, col):
        value = grid[row][col]
        neighbors = count_neighbors(row, col)
        return abs(value) >= neighbors

    # Initialize an empty list to store overflow cell coordinates
    overflow_list = []

    # Iterate though the grid and find overflow cells
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if is_overflow(row, col):
                overflow_list.append((row, col))

    # return the list of overflow cells or None if there are no overflows
    return overflow_list if overflow_list else None


def overflow(grid, a_queue):
    # get the number of rows and columns in the grid
    num_rows = len(grid)
    num_cols = len(grid[0])

    # Check if every value in the grid has the same sign
    all_positive = all(all(cell >= 0 for cell in row) for row in grid)
    all_negative = all(all(cell <= 0 for cell in row) for row in grid)

    # If either all values are non-negative or all values are non-positive, add to the queue and return 0
    if all_positive or all_negative:
        a_queue.enqueue([row[:] for row in grid])
        return 0

    # Initialize flags and counter
    is_overflow = False
    count = 0

    # Find cells that are part of an overflow
    overflow_cells = get_overflow_list(grid)
    if not overflow_cells:
        return count

    for row, col in overflow_cells:
        # determine the sign of the cells value
        sign = 1 if grid[row][col] > 0 else -1

        # mark that an overflow event has occurred
        is_overflow = True

        # store the absolute current cell value
        current_cell_value = abs(grid[row][col])

        grid[row][col] = 0

        if col < num_cols - 1:
            # check the value of next cell
            next_cell_value = abs(grid[row][col + 1])
            if (
                current_cell_value == next_cell_value
                and (row, col + 1) in overflow_cells
            ):
                grid[row][col] = sign
                grid[row][col + 1] = sign
                if col + 2 < num_cols - 1:
                    grid[row][col + 2] = (abs(grid[row][col + 2]) + 1) * sign
                    if row + 1 < num_rows:
                        grid[row + 1][col + 1] = (
                            abs(grid[row + 1][col + 1]) + 1
                        ) * sign
                overflow_cells.remove((row, col))
            else:
                grid[row][col + 1] = (abs(grid[row][col + 1]) + 1) * sign
        if col > 0:
            grid[row][col - 1] = (abs(grid[row][col - 1]) + 1) * sign
        if row > 0:
            grid[row - 1][col] = (abs(grid[row - 1][col]) + 1) * sign
        if row < num_rows - 1:
            grid[row + 1][col] = (abs(grid[row + 1][col]) + 1) * sign

    a_queue.enqueue([row[:] for row in grid])

    if not is_overflow:
        return count

    count += overflow(grid, a_queue) + 1
    return count
