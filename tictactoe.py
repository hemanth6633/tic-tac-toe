import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.player1_name = tk.StringVar()
        self.player2_name = tk.StringVar()

        self.player1_label = tk.Label(root, text="Player 1 Name:")
        self.player1_label.grid(row=0, column=0, padx=10, pady=10)
        self.player1_entry = tk.Entry(root, textvariable=self.player1_name)
        self.player1_entry.grid(row=0, column=1, padx=10, pady=10)

        self.player2_label = tk.Label(root, text="Player 2 Name:")
        self.player2_label.grid(row=1, column=0, padx=10, pady=10)
        self.player2_entry = tk.Entry(root, textvariable=self.player2_name)
        self.player2_entry.grid(row=1, column=1, padx=10, pady=10)

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def start_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j] is None:
                    self.buttons[i][j] = tk.Button(self.root, text="", font='Helvetica 20', height=3, width=6,
                                                   command=lambda row=i, col=j: self.button_click(row, col))
                    self.buttons[i][j].grid(row=i+3, column=j)

    def button_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                self.show_winner()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != "":
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def show_winner(self):
        winner = self.player1_name.get() if self.current_player == "X" else self.player2_name.get()
        messagebox.showinfo("Game Over", f"Congratulations! {winner} wins!")
        self.start_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
