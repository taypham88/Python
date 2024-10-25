'''This file will implement the GUI version and import the game logic'''

import tkinter as tk
from tkinter import messagebox, simpledialog
from tic_tac_toe import TicTacToe, Player

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.size = self.get_board_size()
        self.game = TicTacToe(self.size)
        self.current_player = Player.PLAYER1
        self.buttons = [[None for _ in range(self.size)] for _ in range(self.size)]
        self._build_grid()

    def get_board_size(self):
        while True:
            try:
                size = simpledialog.askinteger("Board Size", "Enter board size (between 3 and 10):", minvalue=3, maxvalue=10, parent=self.root)
                if size is not None:
                    return size
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid number between 3 and 10.")

    def _build_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                button = tk.Button(self.root, text="", width=10, height=3,
                                  command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def make_move(self, i, j):
        result = self.game.move(self.current_player, i, j)
        if result == "Invalid move":
            messagebox.showerror("Invalid Move", "This move is not allowed.")
            return

        self.buttons[i][j].config(text="X" if self.current_player == Player.PLAYER1 else "O")

        if "wins" in result:
            messagebox.showinfo("Game Over", result)
            self.reset_game()
        elif result == "It's a draw!":
            messagebox.showinfo("Game Over", result)
            self.reset_game()
        else:
            self.current_player = Player.PLAYER2 if self.current_player == Player.PLAYER1 else Player.PLAYER1

    def reset_game(self):
        self.game.reset_game()
        self.current_player = Player.PLAYER1
        for i in range(self.size):
            for j in range(self.size):
                self.buttons[i][j].config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tic Tac Toe")
    app = TicTacToeGUI(root)
    root.mainloop()