import tkinter as tk
import random
import time
labels = []
turn = 'X'
computer = '0'
winner = ''


def comp_step():
    # stupid move
    global turn
    if computer == '1':
        empty_labels = []
        for i in range(0, 9):
            if labels[i]['text'] == '':
                empty_labels.append(labels[i])
        r = random.randint(0, len(empty_labels)-1)
        labels_unbind()
        empty_labels[r].after(500, lambda: freeze_game(empty_labels[r]))
        turn = 'X'
    # smart move
    if computer == '2':
        current_board = [[], [], []]
        for i in range(0, 9):
            current_board[i//3].append(labels[i]['text'])
        if turn == 'O':
            labels_unbind()
            minimax_index = minimax(current_board, True)[1]
            label = labels[minimax_index[0]*3 + minimax_index[1]]
            label.after(500, lambda: freeze_game(label))
            turn = 'X'


def minimax(board, min_max):
    win_tie = minimax_win_tie(board)
    if win_tie != 2:
        return win_tie, None
    empty = []
    x_o = 'O' if min_max is True else 'X'
    for row in range(3):
        for column in range(3):
            if board[row][column] == '':
                empty.append((row, column))
    maximum = -1
    minimum = 1
    best_index = (0, 0)
    for index in empty:
        new_board = [i.copy() for i in board]
        new_board[index[0]][index[1]] = x_o
        result = minimax(new_board, not min_max)[0]
        if min_max is True:
            if result == 1 or maximum == 1:
                return 1, index
            if maximum <= result:
                maximum = result
                best_index = index
        else:
            if result == -1 or minimum == -1:
                return -1, index
            if minimum >= result:
                minimum = result
                best_index = index
    if min_max is True:
        return maximum, best_index
    else:
        return minimum, best_index


def minimax_win_tie(board):
    # chek win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'O':
                return 1
            elif board[i][0] == 'X':
                return -1
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'O':
                return 1
            elif board[0][i] == 'X':
                return -1
        if (board[0][0] == board[1][1] == board[2][2]) or (board[2][0] == board[1][1] == board[0][2]):
            if board[1][1] == 'O':
                return 1
            elif board[1][1] == 'X':
                return -1
    # check tie
    if '' not in [board[i][j] for i in range(3) for j in range(3)]:
        return 0
    return 2


def freeze_game(label):
    label.config(text='O')
    labels_bind()
    check_win_tie()


def check_tie():
    for i in range(0, 9):
        if labels[i]['text'] == '':
            return False
    return True


def check_win():
    global winner
    # check rows:
    for i in range(0, 7, 3):
        if labels[i]['text'] == labels[i + 1]['text'] == labels[i + 2]['text'] != '':
            winner = labels[i]['text']
    # check columns:
    for i in range(3):
        if labels[i]['text'] == labels[i + 3]['text'] == labels[i + 6]['text'] != '':
            winner = labels[i]['text']
    # check diagonals:
    if labels[0]['text'] == labels[4]['text'] == labels[8]['text'] != '':
        winner = labels[0]['text']
    if labels[2]['text'] == labels[4]['text'] == labels[6]['text'] != '':
        winner = labels[2]['text']
    return winner


def check_win_tie():
    global winner
    global turn
    labels[9]['text'] = f'Turn {turn}'
    win_tie = False
    if winner == '':
        winner = check_win()
    if winner != '':
        labels[9]['text'] = f'The winner is {winner}'
        win_tie = True
    if check_tie() is True and winner == '':
        labels[9]['text'] = 'Tie'
        win_tie = True
    return win_tie


def player_step(label):
    global turn
    if label['text'] == '':
        if turn == 'X':
            label.config(text='X')
            turn = 'O'
        elif turn == 'O':
            label.config(text='O')
            turn = 'X'
        if check_win_tie() is False:
            comp_step()


def labels_bind():
    labels[0].bind("<Button-1>", func=lambda x: player_step(labels[0]))
    labels[1].bind("<Button-1>", func=lambda x: player_step(labels[1]))
    labels[2].bind("<Button-1>", func=lambda x: player_step(labels[2]))
    labels[3].bind("<Button-1>", func=lambda x: player_step(labels[3]))
    labels[4].bind("<Button-1>", func=lambda x: player_step(labels[4]))
    labels[5].bind("<Button-1>", func=lambda x: player_step(labels[5]))
    labels[6].bind("<Button-1>", func=lambda x: player_step(labels[6]))
    labels[7].bind("<Button-1>", func=lambda x: player_step(labels[7]))
    labels[8].bind("<Button-1>", func=lambda x: player_step(labels[8]))


def labels_unbind():
    for i in range(0, 9):
        labels[i].bind("<Button-1>", func=lambda x: x)


def labels_grid():
    labels[0].grid(row=0, column=0)
    labels[1].grid(row=0, column=1)
    labels[2].grid(row=0, column=2)
    labels[3].grid(row=1, column=0)
    labels[4].grid(row=1, column=1)
    labels[5].grid(row=1, column=2)
    labels[6].grid(row=2, column=0)
    labels[7].grid(row=2, column=1)
    labels[8].grid(row=2, column=2)
    labels[9].grid(row=0)
    labels[10].grid(row=1)


def new_game():
    global winner
    global turn
    global labels
    winner = ''
    turn = 'X'
    for i in range(0, 9):
        labels[i]['text'] = ''
    labels[9]['text'] = f'Turn {turn}'


def change_player(radio):
    global computer
    computer = radio.get()
    new_game()


def main():
    global labels
    root = tk.Tk()
    frame = tk.Frame(root)
    FONT = ('Arial', 70)
    FONT2 = ('Arial', 20)
    FONT3 = ('Arial', 16)
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
    player_vs_player.grid(row=0, pady=5, padx=5, sticky='W')
    player_vs_computer.grid(row=1, pady=5, padx=5, sticky='W')
    player_vs_smart_computer.grid(row=2, pady=5, padx=5, sticky='W')
    labels = [top_left, top_middle, top_right, middle_left, middle_middle, middle_right, bottom_left, bottom_middle,
              bottom_right, turn_label, restart, root]
    labels_grid()
    labels_bind()
    frame.pack()
    frame2.pack()
    frame3.pack(anchor='w')
    root.mainloop()


if __name__ == "__main__":
    main()
