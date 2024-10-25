### Pytest File for Testing ###
import pytest
from tic_tac_toe import TicTacToe, Player

def test_player_1_row_win():
    game = TicTacToe(4)
    assert game.move(Player.PLAYER1, 0, 0) == "Next move"
    assert game.move(Player.PLAYER2, 0, 1) == "Next move"
    assert game.move(Player.PLAYER1, 1, 0) == "Next move"
    assert game.move(Player.PLAYER2, 0, 2) == "Next move"
    assert game.move(Player.PLAYER1, 2, 0) == "Next move"
    assert game.move(Player.PLAYER1, 3, 0) == "PLAYER1 wins the game!"

def test_player_2_row_win():
    game = TicTacToe(3)
    assert game.move(Player.PLAYER1, 2, 2) == "Next move"
    assert game.move(Player.PLAYER2, 0, 1) == "Next move"
    assert game.move(Player.PLAYER1, 1, 0) == "Next move"
    assert game.move(Player.PLAYER2, 0, 2) == "Next move"
    assert game.move(Player.PLAYER1, 2, 0) == "Next move"
    assert game.move(Player.PLAYER2, 0, 0) == "PLAYER2 wins the game!"

def test_player_1_column_win():
    game = TicTacToe(3)
    assert game.move(Player.PLAYER1, 0, 0) == "Next move"
    assert game.move(Player.PLAYER2, 1, 1) == "Next move"
    assert game.move(Player.PLAYER1, 0, 1) == "Next move"
    assert game.move(Player.PLAYER2, 2, 2) == "Next move"
    assert game.move(Player.PLAYER1, 0, 2) == "PLAYER1 wins the game!"

def test_player_2_column_win():
    game = TicTacToe(3)
    assert game.move(Player.PLAYER1, 1, 0) == "Next move"
    assert game.move(Player.PLAYER2, 0, 2) == "Next move"
    assert game.move(Player.PLAYER1, 1, 1) == "Next move"
    assert game.move(Player.PLAYER2, 0, 1) == "Next move"
    assert game.move(Player.PLAYER1, 2, 2) == "Next move"
    assert game.move(Player.PLAYER2, 0, 0) == "PLAYER2 wins the game!"

def test_player_1_negative_diagonal_win():
    game = TicTacToe(3)
    assert game.move(Player.PLAYER1, 0, 0) == "Next move"
    assert game.move(Player.PLAYER2, 0, 1) == "Next move"
    assert game.move(Player.PLAYER1, 1, 1) == "Next move"
    assert game.move(Player.PLAYER2, 0, 2) == "Next move"
    assert game.move(Player.PLAYER1, 2, 2) == "PLAYER1 wins the game!"

def test_player_1_positive_diagonal_win():
    game = TicTacToe(3)
    assert game.move(Player.PLAYER1, 0, 2) == "Next move"
    assert game.move(Player.PLAYER2, 0, 1) == "Next move"
    assert game.move(Player.PLAYER1, 1, 1) == "Next move"
    assert game.move(Player.PLAYER2, 0, 0) == "Next move"
    assert game.move(Player.PLAYER1, 2, 0) == "PLAYER1 wins the game!"

def test_draw():
    game = TicTacToe(3)
    assert game.move(Player.PLAYER1, 1, 1) == "Next move"
    assert game.move(Player.PLAYER2, 0, 0) == "Next move"
    assert game.move(Player.PLAYER1, 1, 0) == "Next move"
    assert game.move(Player.PLAYER2, 1, 2) == "Next move"
    assert game.move(Player.PLAYER1, 2, 2) == "Next move"
    assert game.move(Player.PLAYER2, 2, 0) == "Next move"
    assert game.move(Player.PLAYER1, 2, 1) == "Next move"
    assert game.move(Player.PLAYER2, 0, 1) == "Next move"
    assert game.move(Player.PLAYER1, 0, 2) == "It's a draw!"

def test_invalid_move():
    game = TicTacToe(3)
    assert game.move(Player.PLAYER1, 1, 0) == "Next move"
    assert game.move(Player.PLAYER2, 1, 0) == "Invalid move"

if __name__ == "__main__":
    pytest.main()
