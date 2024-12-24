import tkinter as tk

playerX = "X"
playerO = "O"
scoreX = 0
scoreO = 0
move = 0
i = 0 
game_over = False


curr_player = playerX
not_curr_player = playerO
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]


cream = "#fcd8a2"
hot_pink = "#ba0f30"
spearmint = "#f4e6d5"
rosewater = "#fbb000"


window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(True,True)
window.geometry("800x800")
window['bg'] = rosewater
frame = tk.Frame(window)
label_text = tk.Label(frame, text =(f"{curr_player}'s Turn"), font = ("comic sans MS",50), foreground="#ba0f30", background=rosewater)
label_score = tk.Label(frame, text = (f"score X = {scoreX}\nscore O = {scoreO}"), font = ("comic sans MS",50), foreground="#ba0f30", background=rosewater)
label_text.grid(row=0,column=0, columnspan=3, sticky="we")
label_score.grid(row=5,column=0, columnspan=3, sticky="we")
frame.pack()


def winner():
    global move, game_over, scoreX, scoreO
    move += 1


    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]) and board[row][0]["text"] != "":
            for column in range(3):
                board[row][column].config(background = spearmint)
            label_text.config(text = (f"{not_curr_player} is the winner"))
            if not_curr_player == playerX:
                scoreX += 1
            else:
                scoreO += 1
            label_score.config(text = (f"score X = {scoreX}\nscore O = {scoreO}"))
            game_over = True
            return 


    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]) and board[0][column]["text"] != "":
            for row in range(3):
                board[row][column].config(background = spearmint)
            label_text.config(text = (f"{not_curr_player} is the winner"))
            if not_curr_player == playerX:
                scoreX += 1
            else:
                scoreO += 1
            label_score.config(text = (f"score X = {scoreX}\nscore O = {scoreO}"))
            game_over = True
            return 


    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != '':
        board[0][0].config(background = spearmint)
        board[1][1].config(background = spearmint)
        board[2][2].config(background = spearmint)
        label_text.config(text = (f"{not_curr_player} is the winner"))
        if not_curr_player == playerX:
            scoreX += 1
        else:
            scoreO += 1
        label_score.config(text = (f"score X = {scoreX}\nscore O = {scoreO}"))
        game_over = True
        return 


    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[2][0]["text"] != '':
        board[0][2].config(background = spearmint)
        board[1][1].config(background = spearmint)
        board[2][0].config(background = spearmint)
        label_text.config(text = (f"{not_curr_player} is the winner"))
        if not_curr_player == playerX:
            scoreX += 1
        else:
            scoreO += 1
        label_score.config(text = (f"score X = {scoreX}\nscore O = {scoreO}"))
        game_over = True
        return
        

    if move == 9:
        label_text.config(text = (f"Draw"), foreground="Black")
        game_over = True
        return 


def set_tile(row,column):
    global curr_player, not_curr_player

    if game_over:
        return

    if board[row][column]["text"] != "":
        return
    
    if curr_player == playerO:
        board[row][column].config(text=playerO, foreground="white")
    else:
        board[row][column].config(text=playerX, foreground="black")

    if curr_player == playerO:
        curr_player = playerX
        not_curr_player = playerO
    else:
        curr_player = playerO
        not_curr_player = playerX


    
    label_text["text"] = (f"{curr_player}'s Turn")

    winner() 


def game_restart():
    global move, game_over

    move = 0
    game_over = False
    label_text.config(text =(f"{curr_player}'s Turn"))
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=hot_pink, background=cream)
    
for row in range(3):    
    for column in range(3):
        board[row][column] = tk.Button(frame, text="", font = ("comic sans MS",50),
                                    foreground=hot_pink, background=cream, width=4, height=1,
                                    command=lambda row=row,column=column: set_tile(row,column))
        board[row][column].grid(row=row+1, column=column)

label_restart = tk.Button(frame, text =(f"Restart"), font = ("comic sans MS",50),
                           foreground=hot_pink, background=cream, width=6, height=1,
                           command = game_restart)
label_restart.grid(row=4,column=0,columnspan=3, sticky="we") 

window.mainloop()
    