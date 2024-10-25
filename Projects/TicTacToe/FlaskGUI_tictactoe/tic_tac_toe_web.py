'''This file will implement the web version using Flask and also import the game logic'''

import os
from flask import Flask, render_template, request, redirect, url_for
from tic_tac_toe import TicTacToe, Player

def get_board_size():
    if os.getenv("TEST_ENV"):
        return 3  # Default size for testing
    while True:
        try:
            size = int(input("Enter board size (between 3 and 10): "))
            if 3 <= size <= 10:
                return size
        except ValueError:
            print("Invalid input. Please enter a number between 3 and 10.")

game_size = get_board_size()
app = Flask(__name__)
game = TicTacToe(game_size)
current_player = Player.PLAYER1

@app.route("/")
def index():
    board = [["" for _ in range(game.size)] for _ in range(game.size)]
    for (i, j) in game.board:
        board[i][j] = "X" if game.scores[Player.PLAYER1][0][i] or game.scores[Player.PLAYER1][1][j] else "O"
    return render_template("index.html", board=board, current_player=current_player.name)

@app.route("/move", methods=["POST"])
def move():
    global current_player
    i, j = int(request.form["row"]), int(request.form["col"])
    result = game.move(current_player, i, j)
    if result == "Invalid move":
        return redirect(url_for("index"))

    if "wins" in result or result == "It's a draw!":
        return render_template("game_over.html", message=result)
    else:
        current_player = Player.PLAYER2 if current_player == Player.PLAYER1 else Player.PLAYER1
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)