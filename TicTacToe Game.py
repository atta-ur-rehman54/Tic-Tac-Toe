# Importing Libraries

import tkinter as tk
import random



# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")


                    #Setting Up the Board
# Initialize the board, it's a list of 9 empty spots
board = [""] * 9
player = "X"  # The human player is "X"
ai_player = "O"  # The AI player is "O"



                    #Checking for a Winner
# Function to check if anyone has won
def check_winner():
    # List of winning combinations (rows, columns, diagonals)
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    
    for combination in win_combinations:
        # If all three spots in a combination are filled by the same player, return that player as the winner
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != "":
            return board[combination[0]]
    return None

                #Checking if the Board is Full
# Function to check if the board is full (no more empty spots)
def check_full():
    return "" not in board
    
                    #AI's Move Logic
# Function to handle AI's move
def ai_move():
    # Try to find an empty spot where the AI can win or block the player
    for i in range(9):
        if board[i] == "":
            # Try the move for AI (O)
            board[i] = ai_player
            if check_winner() == ai_player:  # Check if AI wins
                buttons[i].config(text=ai_player, bg="lightcoral")
                return
            board[i] = ""  # Undo the move if it doesn't win
    
    # If AI can't win, block the player from winning
    for i in range(9):
        if board[i] == "":
            board[i] = player
            if check_winner() == player:  # Check if the player wins
                board[i] = ai_player
                buttons[i].config(text=ai_player, bg="lightcoral")
                return
            board[i] = ""  # Undo the move if it doesn't block the player
    
    # If no one is winning, pick a random empty spot
    empty_spots = [i for i in range(9) if board[i] == ""]
    move = random.choice(empty_spots)
    board[move] = ai_player
    buttons[move].config(text=ai_player, bg="lightcoral")

    
                        #Handling Player's Move
# Function to handle a click on the button (where player makes a move)
def button_click(i):
    global player
    if board[i] == "" and not check_winner():  # Ensure the square is empty and no one has won
        board[i] = player
        buttons[i].config(text=player, bg="lightblue")
        
        # Check if the player won
        if check_winner() == player:
            result_label.config(text=f"Player {player} wins!", fg="green")
        elif check_full():
            result_label.config(text="It's a tie!", fg="red")
        else:
            # If no one won, switch turns to the AI's turn
            player = ai_player
            ai_move()  # AI makes its move
            # After AI move, check for winner
            if check_winner() == ai_player:
                result_label.config(text=f"Player {ai_player} wins!", fg="red")
            elif check_full():
                result_label.config(text="It's a tie!", fg="red")
            else:
                player = "X"  # Switch back to Player X's turn


                
                        #Creating the Grid (Buttons)
# Create buttons for the Tic Tac Toe grid
buttons = []
for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 24), width=5, height=2, command=lambda i=i: button_click(i), bg="lightgray")
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)
    
                            #Displaying the Game Result
# Label to show the game result
result_label = tk.Label(root, text="Player X's turn", font=("Arial", 16), fg="black")
result_label.grid(row=3, column=0, columnspan=3)


                            # Resetting the Game
# Reset button to restart the game
def reset_game():
    global board, player
    board = [""] * 9  # Reset the board
    player = "X"  # Player X starts
    result_label.config(text="Player X's turn", fg="black")  # Reset the result label
    for button in buttons:
        button.config(text="", bg="lightgray")  # Reset the button texts and colors

        
                        #Creating the Reset Button
# Create the reset button
reset_button = tk.Button(root, text="Restart Game", font=("Arial", 16), command=reset_game, bg="lightgreen")
reset_button.grid(row=4, column=0, columnspan=3)

                        #Running the Game Loop
# Run the main loop (to keep the window open)
root.mainloop()
