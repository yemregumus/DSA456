from a1_partc import Queue


def get_overflow_list(grid):
    def count_neighbors(row, col, rows, cols):
        count = 0
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols:
                count += 1
        return count

    rows, cols = len(grid), len(grid[0])
    overflow_list = []

    for row in range(rows):
        for col in range(cols):
            neighbors = count_neighbors(row, col, rows, cols)
            if abs(grid[row][col]) >= neighbors:
                overflow_list.append((row, col))

    if not overflow_list:
        return None
    return overflow_list


def overflow(grid, a_queue):
    def is_valid_cell(row, col, rows, cols):
        return 0 <= row < rows and 0 <= col < cols

    def process_overflow(row, col, rows, cols):
        if is_valid_cell(row, col, rows, cols) and grid[row][col] != 0:
            value = grid[row][col]
            grid[row][col] = 0
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r, c = row + dr, col + dc
                if is_valid_cell(r, c, rows, cols):
                    if grid[r][c] * value > 0:
                        grid[r][c] += value
                    elif grid[r][c] == 0:
                        grid[r][c] = value
            return True
        return False

    rows, cols = len(grid), len(grid[0])
    overflow_count = 0

    while True:
        overflow_cells = get_overflow_list(grid)
        if not overflow_cells:
            break

        for row, col in overflow_cells:
            if process_overflow(row, col, rows, cols):
                overflow_count += 1

    a_queue.enqueue([row[:] for row in grid])
    return overflow_count
