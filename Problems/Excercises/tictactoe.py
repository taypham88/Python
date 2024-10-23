'''Excercise to build a tic toc toe game back end'''

'''Should intialize the game, allow moves input, execute win condition'''
from enum import Enum

class Player(Enum):
    PLAYER1 = 1
    PLAYER2 = 2

class TicTacToe:

    def __init__(self, n):
        if not (3 <= n <= 10):
            raise ValueError("Board size must be between 3 and 10")
        self.size = n
        self.reset_game()

    def reset_game(self):
        """Resets the game state."""
        self.scores = {
            Player.PLAYER1: [[0] * self.size, [0] * self.size, [0], [0]],
            Player.PLAYER2: [[0] * self.size, [0] * self.size, [0], [0]]
        }
        self.board = set()

    def move(self, player, i, j):
        """Makes a move and returns the game status."""
        if not self._is_valid_move(i, j):
            return "Invalid move"

        # Register the move
        self.board.add((i, j))
        self._update_scores(player, i, j)

        # Check for a win or draw
        if self._winGame(player):
            return f"{player.name} wins the game!"
        if self._checkDraw():
            return "It's a draw!"
        return "Next move"

    def _is_valid_move(self, i, j):
        """Checks if the move is valid."""
        return 0 <= i < self.size and 0 <= j < self.size and (i, j) not in self.board

    def _update_scores(self, player, i, j):
        """Updates the player's score for the given move."""
        self.scores[player][0][i] += 1  # Row count
        self.scores[player][1][j] += 1  # Column count
        if i + j == self.size - 1:  # Negative diagonal
            self.scores[player][2][0] += 1
        if i == j:  # Positive diagonal
            self.scores[player][3][0] += 1

    def _winGame(self, player):
        """Checks if the player has won."""
        return (
            self.size in (self.scores[player][2][0], self.scores[player][3][0])
            or any(row == self.size for row in self.scores[player][0])
            or any(col == self.size for col in self.scores[player][1])
        )

    def _checkDraw(self):
        """Checks if the game is a draw."""
        return len(self.board) == self.size * self.size


if __name__ == '__main__':
    # Test player 1 row win
    game = TicTacToe(4)
    print(game.move(Player.PLAYER1, 0, 0))
    print(game.move(Player.PLAYER2, 0, 1))
    print(game.move(Player.PLAYER1, 1, 0))
    print(game.move(Player.PLAYER2, 0, 2))
    print(game.move(Player.PLAYER1, 2, 0))
    print(game.move(Player.PLAYER1, 3, 0))

    # Test player 2 row win
    game = TicTacToe(3)
    print(game.move(Player.PLAYER1, 2, 2))
    print(game.move(Player.PLAYER2, 0, 1))
    print(game.move(Player.PLAYER1, 1, 0))
    print(game.move(Player.PLAYER2, 0, 2))
    print(game.move(Player.PLAYER1, 2, 0))
    print(game.move(Player.PLAYER2, 0, 0))

    # Test player 1 col win
    game = TicTacToe(3)
    print(game.move(Player.PLAYER1, 0, 0))
    print(game.move(Player.PLAYER2, 1, 1))
    print(game.move(Player.PLAYER1, 0, 1))
    print(game.move(Player.PLAYER2, 2, 2))
    print(game.move(Player.PLAYER1, 0, 2))

    # Test player 2 col win
    game = TicTacToe(3)
    print(game.move(Player.PLAYER1, 1, 0))
    print(game.move(Player.PLAYER2, 0, 2))
    print(game.move(Player.PLAYER1, 1, 1))
    print(game.move(Player.PLAYER2, 0, 1))
    print(game.move(Player.PLAYER1, 2, 2))
    print(game.move(Player.PLAYER2, 0, 0))

    # Test player 1 negDiag win
    game = TicTacToe(3)
    print(game.move(Player.PLAYER1, 0, 0))
    print(game.move(Player.PLAYER2, 0, 1))
    print(game.move(Player.PLAYER1, 1, 1))
    print(game.move(Player.PLAYER2, 0, 2))
    print(game.move(Player.PLAYER1, 2, 2))


    # Test player 1 posDiag win
    game = TicTacToe(3)
    print(game.move(Player.PLAYER1, 0, 2))
    print(game.move(Player.PLAYER2, 0, 1))
    print(game.move(Player.PLAYER1, 1, 1))
    print(game.move(Player.PLAYER2, 0, 0))
    print(game.move(Player.PLAYER1, 2, 0))

    # Test Draw
    game = TicTacToe(3)
    print(game.move(Player.PLAYER1, 1, 1))
    print(game.move(Player.PLAYER2, 0, 0))
    print(game.move(Player.PLAYER1, 1, 0))
    print(game.move(Player.PLAYER2, 1, 2))
    print(game.move(Player.PLAYER1, 2, 2))
    print(game.move(Player.PLAYER2, 2, 0))
    print(game.move(Player.PLAYER1, 2, 1))
    print(game.move(Player.PLAYER2, 0, 1))
    print(game.move(Player.PLAYER1, 0, 2))

    # Test invalid move
    game = TicTacToe(3)
    print(game.move(Player.PLAYER1, 1, 0))
    print(game.move(Player.PLAYER2, 1, 0))

