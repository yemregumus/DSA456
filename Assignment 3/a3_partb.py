# Main Author: Dev Jigishkumar Shah
# Main Reviewer: Yunus Emre Gumus, Lorenzo Ramos

# This function duplicates and returns the board. You may find this useful

from a3_parta import evaluate_board, has_winning_config, overflow


def copy_board(board):
    current_board = []
    height = len(board)
    for i in range(height):
        current_board.append(board[i].copy())
    return current_board


class GameTree:
    class Node:
        def __init__(self, board, depth, player, tree_height, move=None):
            self.board = board
            self.depth = depth
            self.player = player
            self.tree_height = tree_height
            self.children = []
            self.move = move
            self.score = None

    def __init__(self, board, player, tree_height=4):
        self.player = player
        self.board = copy_board(board)
        self.root = self.Node(board, 0, player, tree_height)
        self.build_tree(self.root)

    def build_tree(self, node):
        # Base case: Check if the node is at the maximum depth or the board is in a terminal state
        if (
            node.depth == node.tree_height - 1
            or has_winning_config(node.board, 1)
            or has_winning_config(node.board, -1)
        ):
            # Evaluate the board and set the score attribute of the node
            node.score = evaluate_board(node.board, node.player)
            return

        # Check if node.board is a list before attempting to access its elements
        if not isinstance(node.board, list):
            return

        # For each valid move, create a child node and recursively call build_tree
        for col in range(len(node.board[0])):
            if not overflow(node.board, col):
                new_board = [row[:] for row in node.board]  # create a copy of the board
                new_board = overflow(
                    new_board, col
                )  # update the new board with the result of overflow
                child_node = self.Node(
                    new_board,
                    node.depth + 1,
                    -node.player,
                    node.tree_height,
                    move=(node.depth, col),
                )
                node.children.append(child_node)
                self.build_tree(child_node)

        # After all children are created, score the current node using the minimax algorithm
        if node.children:
            child_scores = [child.score for child in node.children]
            if all(score is None for score in child_scores):
                # If all child scores are None, set the node score to None
                node.score = None
            else:
                if node.depth % 2 == 0:
                    # Maximize for even-depth nodes
                    node.score = max(
                        score for score in child_scores if score is not None
                    )
                else:
                    # Minimize for odd-depth nodes
                    node.score = min(
                        score for score in child_scores if score is not None
                    )

    def get_move(self):
        if not self.root.children:
            return (0, 1)  # Return a placeholder move when there is no valid move

        # Filter out nodes with None scores or None moves
        valid_children = [
            child
            for child in self.root.children
            if child.score is not None and child.move is not None
        ]

        if not valid_children:
            return (0, 1)  # Return a placeholder move when there is no valid move

        # Get the best child based on the score
        best_child = max(valid_children, key=lambda x: x.score, default=None)

        # Check if the best_child has a valid move
        if best_child.move is not None:
            return best_child.move
        else:
            return (0, 1)  # Return a placeholder move when there is no valid move

    def clear_tree(self):
        self.root.children = []
