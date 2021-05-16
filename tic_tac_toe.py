import tkinter as tk
# import random
labels = []
turn = 'X'
winner = ''


def comp_step():
    """ ######## stupid computer move #########
    global turn
    empty_labels = []
    for label in labels:
        if label['text'] == '':
            empty_labels.append(label)
    r = random.randint(0,len(empty_labels)-1)
    empty_labels[r]['text'] = 'O'
    turn = 'X'
    check_win_tie()
    """

def check_tie():
    for label in labels:
        if label['text'] == '':
            return False
    return True


def check_win():
    global winner
    #check rows:
    for i in range(0,7,3):
        if labels[i]['text'] == labels[i + 1]['text'] == labels[i + 2]['text'] != '':
            winner = labels[i]['text']
    #check columns:
    for i in range(3):
        if labels[i]['text'] == labels[i + 3]['text'] == labels[i + 6]['text'] != '':
            winner = labels[i]['text']
    #check diagonals:
    if labels[0]['text'] == labels[4]['text'] == labels[8]['text'] != '':
        winner = labels[0]['text']
    if labels[2]['text'] == labels[4]['text'] == labels[6]['text'] != '':
        winner = labels[2]['text']
    return winner


def check_win_tie():
    global winner
    global turn
    labels[9]['text'] = f'turn {turn}'
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
    labels[9].pack()


def main():
    global labels
    root = tk.Tk()
    frame = tk.Frame(root)
    FONT = ('Arial',70)
    top_left = tk.Label(frame,text='', font=FONT, width=2, height=1, relief='solid')
    top_middle = tk.Label(frame, text='', font=FONT, width=2, height=1, relief='solid')
    top_right = tk.Label(frame, text='', font=FONT, width=2, height=1, relief='solid')
    middle_left = tk.Label(frame, text='', font=FONT, width=2, height=1, relief='solid')
    middle_middle = tk.Label(frame, text='', font=FONT, width=2, height=1, relief='solid')
    middle_right = tk.Label(frame, text='', font=FONT, width=2, height=1, relief='solid')
    bottom_left = tk.Label(frame, text='', font=FONT, width=2, height=1, relief='solid')
    bottom_middle = tk.Label(frame, text='', font=FONT, width=2, height=1, relief='solid')
    bottom_right = tk.Label(frame, text='', font=FONT, width=2, height=1, relief='solid')
    frame2 = tk.Frame(root)
    turn_label = tk.Label(frame2, text='turn X', font=('Arial',20))
    labels = [top_left, top_middle, top_right, middle_left, middle_middle, middle_right, bottom_left, bottom_middle, bottom_right, turn_label]
    labels_grid()
    labels_bind()
    frame.pack()
    frame2.pack()
    root.mainloop()


if __name__ == "__main__":
    main()