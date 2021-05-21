import tkinter as tk
import random
widgets = []
turn = 'X'
radio_button = '0'
winner = ''


def comp_step():
    # random step
    global turn
    current_board = get_matrix_board()
    if radio_button == '1':
        labels_unbind()
        # delay between player step and computer step
        widgets[11].after(500, lambda: freeze_game(random.choice(empty_cells(current_board))))
    # smart step (minimax algorithm)
    if radio_button == '2':
        # checks if it's the computer's turn
        if turn == 'O':
            labels_unbind()
            # gets the optimal index for computer step
            index = minimax(current_board, True)[1]
            # delay between player step and computer step
            widgets[11].after(500, lambda: freeze_game(index))


def get_matrix_board():
    board = [[], [], []]
    for i in range(9):
        # converts the visual board to a matrix
        board[i // 3].append(widgets[i]['text'])
    return board


def empty_cells(board):
    # returns a indexes list of the empty cells
    return [(row, column) for row in range(3) for column in range(3) if board[row][column] == '']


# Computes all possible ways to proceed from the current state and selects the optimal way
def minimax(board, min_max):
    result = win_draw(board)
    if result != 2:
        return result, None
    maximum = -1
    minimum = 1
    best_index = (0, 0)
    for index in empty_cells(board):
        new_board = [i.copy() for i in board]
        # puts in the board X or O according the turn
        new_board[index[0]][index[1]] = 'O' if min_max is True else 'X'
        # the recursive step
        result = minimax(new_board, not min_max)[0]
        # computer turn
        if min_max is True:
            # improvement of the algorithm for saving unnecessary steps
            if result == 1:
                return 1, index
            # Finds the maximum result out of the possible ways and its index (one step from the current board)
            if maximum <= result:
                maximum = result
                best_index = index
        # player turn
        else:
            # improvement of the algorithm for saving unnecessary steps
            if result == -1:
                return -1, index
            # Finds the minimum result out of the possible ways and its index (one step from the current board)
            if minimum >= result:
                minimum = result
                best_index = index
    # returns the result and the optimal index
    return (maximum, best_index) if min_max is True else (minimum, best_index)


def win_draw(board):
    # checks win
    for i in range(3):
        # checks rows
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] != '':
                return 1 if board[i][0] == 'O' else -1 if board[i][0] == 'X' else 2
        # checks columns
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] != '':
                return 1 if board[0][i] == 'O' else -1 if board[0][i] == 'X' else 2
        # checks diagonals
        if (board[0][0] == board[1][1] == board[2][2]) or (board[2][0] == board[1][1] == board[0][2]):
            if board[1][1] != '':
                return 1 if board[1][1] == 'O' else -1 if board[1][1] == 'X' else 2
    # checks draw
    return 0 if '' not in [board[i][j] for i in range(3) for j in range(3)] else 2


def freeze_game(index):
    # changes the pressed label to 'O'
    widgets[index[0] * 3 + index[1]].config(text='O')
    labels_bind()
    check_win_draw()


def check_win_draw():
    global winner
    global turn
    if winner == '':
        current_board = get_matrix_board()
        result = win_draw(current_board)
        if result in [1, -1]:
            winner = turn
            widgets[9]['text'] = f'The winner is {winner}'
            labels_unbind()
        if result == 0:
            widgets[9]['text'] = 'Draw'
        if result == 2:
            turn = 'O' if turn == 'X' else 'X'
            widgets[9]['text'] = f'Turn {turn}'
        return result


def player_step(label):
    if label['text'] == '':
        label.config(text=turn)
        # Checks if you are playing against the computer and checks if there is no winner or draw
        if check_win_draw() == 2 and radio_button != '0':
            comp_step()


def labels_bind():
    widgets[0].bind("<Button-1>", func=lambda x: player_step(widgets[0]))
    widgets[1].bind("<Button-1>", func=lambda x: player_step(widgets[1]))
    widgets[2].bind("<Button-1>", func=lambda x: player_step(widgets[2]))
    widgets[3].bind("<Button-1>", func=lambda x: player_step(widgets[3]))
    widgets[4].bind("<Button-1>", func=lambda x: player_step(widgets[4]))
    widgets[5].bind("<Button-1>", func=lambda x: player_step(widgets[5]))
    widgets[6].bind("<Button-1>", func=lambda x: player_step(widgets[6]))
    widgets[7].bind("<Button-1>", func=lambda x: player_step(widgets[7]))
    widgets[8].bind("<Button-1>", func=lambda x: player_step(widgets[8]))


def labels_unbind():
    for i in range(9):
        widgets[i].bind("<Button-1>", func=lambda x: x)


def grid_all():
    for i in range(9):
        # labels grid
        widgets[i].grid(row=(i // 3), column=(i % 3))
    widgets[9].grid(row=0)
    widgets[10].grid(row=1)
    for i in range(12, 15):
        # radio buttons grid
        widgets[i].grid(row=(i - 12), pady=5, padx=5, sticky='W')


def new_game():
    # reset all labels and global variables
    global winner
    global turn
    global widgets
    winner = ''
    turn = 'X'
    labels_bind()
    for i in range(9):
        widgets[i]['text'] = ''
    widgets[9]['text'] = f'Turn {turn}'


def change_player(radio):
    global radio_button
    radio_button = radio.get()
    new_game()


def main():
    global widgets
    root = tk.Tk()
    root.wm_title('Tic Tac Toe')
    frame = tk.Frame(root)
    FONT, FONT2, FONT3 = ('Arial', 70), ('Arial', 20), ('Arial', 16)
    top_left = tk.Label(frame, text='', font=FONT, width=2, height=1, relief='solid')
    top_middle = tk.Label(frame, text='', font=FONT, width=2, height=1, relief='solid')
    top_right = tk.Label(frame, text='', font=FONT, width=2, height=1, relief='solid')
    middle_left = tk.Label(frame, text='', font=FONT, width=2, height=1, relief='solid')
    middle_middle = tk.Label(frame, text='', font=FONT, width=2, height=1, relief='solid')
    middle_right = tk.Label(frame, text='', font=FONT, width=2, height=1, relief='solid')
    bottom_left = tk.Label(frame, text='', font=FONT, width=2, height=1, relief='solid')
    bottom_middle = tk.Label(frame, text='', font=FONT, width=2, height=1, relief='solid')
    bottom_right = tk.Label(frame, text='', font=FONT, width=2, height=1, relief='solid')
    frame2 = tk.Frame(root)
    turn_label = tk.Label(frame2, text=f'Turn {turn}', font=FONT2)
    restart = tk.Button(frame2, text='New game', command=lambda: new_game(), font=FONT3)
    radio = tk.StringVar()
    radio.set(0)
    frame3 = tk.Frame(root)
    player_vs_player = tk.Radiobutton(frame3, text='Player vs Player', command=(lambda: change_player(radio)),
                                      variable=radio, value=0)
    player_vs_computer = tk.Radiobutton(frame3, text='Player vs Computer', command=(lambda: change_player(radio)),
                                        variable=radio, value=1)
    player_vs_smart_computer = tk.Radiobutton(frame3, text='Player vs Smart Computer',
                                              command=(lambda: change_player(radio)), variable=radio, value=2)
    widgets = [top_left, top_middle, top_right, middle_left, middle_middle, middle_right, bottom_left, bottom_middle,
               bottom_right, turn_label, restart, root, player_vs_player, player_vs_computer, player_vs_smart_computer]
    grid_all()
    labels_bind()
    frame.pack()
    frame2.pack()
    frame3.pack(anchor='w')
    root.mainloop()


if __name__ == "__main__":
    main()
