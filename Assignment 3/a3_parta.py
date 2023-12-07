# Main Author: Yunus Emre Gumus
# Main Reviewer: Dev Jigishkumar Shah, Lorenzo Ramos
from a1_partc import Queue
from a1_partd import overflow


# this function is your evaluation function for the board
def evaluate_board(board, player):
    # Check if given player has winning configuration
    if has_winning_config(board, player):
        return 100

    # Check if given player has losing configuration
    if has_losing_config(board, -player):
        return -100

    # Otherwise, calculate heuristic score
    return calculate_heuristic(board, player)


def has_winning_config(board, player):
    if not isinstance(board, list) or not all(isinstance(row, list) for row in board):
        # Handle the case where an integer or non-list object is passed
        return False

    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(len(board[0])):
        if all(board[row][col] == player for row in range(len(board))):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(min(len(board), len(board[0])))) or all(
        board[i][len(board[0]) - i - 1] == player
        for i in range(min(len(board), len(board[0])))
    ):
        return True

    return False


def has_losing_config(board, player):
    # Check if the opponent has a winning configuration
    return has_winning_config(board, player)


def calculate_heuristic(board, player):
    # Calculate heuristic score based on the number of pieces, positions, etc.
    score = 0

    # Evaluate rows
    for row in board:
        score += evaluate_line(row, player)

    # Evaluate columns
    for col in range(len(board[0])):
        column = [board[row][col] for row in range(len(board))]
        score += evaluate_line(column, player)

    # Evaluate diagonals
    diagonal1 = [board[i][i] for i in range(min(len(board), len(board[0])))]
    diagonal2 = [
        board[i][len(board[0]) - i - 1] for i in range(min(len(board), len(board[0])))
    ]

    score += evaluate_line(diagonal1, player)
    score += evaluate_line(diagonal2, player)

    return score


def evaluate_line(line, player):
    # Evaluate a line (row, column, or diagonal) and return the score
    player_count = line.count(player)
    opponent_count = line.count(-player)

    # Reward for having more pieces
    score = player_count - opponent_count

    return score
