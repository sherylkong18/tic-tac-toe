# v5
import tkinter as tk
from tkinter import ttk
from tkinter import *

options = ["O", "X"]
dc = 0
startfirst = 0
colour = ["pale violet red", "steelblue1"]
restartbuttoncolour = "slateblue1"
turn = 0
winningcombo = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2]]


def play():
    window = tk.Toplevel(startpage)
    window.title("tic tac toe")
    window.geometry("500x500")

    def swapturns():
        global turn
        if turn == 0:
            turn = 1
        else:
            turn = 0

    def restart():
        global dc
        global turn
        global startfirst
        # Restart button
        if restartbutton['text'] == "Restart":
            labelscore1['text'] = 0
            labelscore2['text'] = 0
            turn = 0
            startfirst = 0
            label1.config(text=entry1.get() + "'s turn", fg=colour[0])
        else:
            if (startfirst == 0):
                turn = 1
                startfirst = 1
                label1.config(text=entry2.get() + "'s turn", fg=colour[1])
            else:
                turn = 0
                startfirst = 0
                label1.config(text=entry1.get() + "'s turn", fg=colour[0])
            restartbutton.config(text="Restart", fg=restartbuttoncolour)
        for b in buttons:
            b['state'] = tk.NORMAL
            b['text'] = " "
        for labels in winlabels:
            labels.grid_remove()
        dc = 0

    def win(number):
        if number == 0:
            label1.config(text=entry1.get() + " wins!", fg=colour[0])
            labelscore1['text'] += 1
        else:
            label1.config(text=entry2.get() + " wins!", fg=colour[1])
            labelscore2['text'] += 1

        for b in buttons:
            b['state'] = DISABLED
        endgame()

    def endgame():
        global turn
        restartbutton.config(text="Play again", fg=restartbuttoncolour)
        turn = 0

    def checkwin():
        global options
        global turn
        for combo in winningcombo:
            first = buttons[combo[0]]
            second = buttons[combo[1]]
            third = buttons[combo[2]]
            symbol = options[turn]
            if first['text'] == symbol and second['text'] == symbol and third['text'] == symbol:
                i = 0
                for button in [first, second, third]:
                    r = button.grid_info()['row']
                    c = button.grid_info()['column']
                    winlabels[i].config(text=options[turn], fg=colour[turn])
                    winlabels[i].grid(row=r, column=c)
                    i += 1
                return win(turn)
        else:  # check draw
            if dc == 9:
                label1.config(text="Draw!", fg=restartbuttoncolour)
                endgame()

    def changelabel1():
        if label1['text'] == entry1.get() + "'s turn":
            label1.config(text=entry2.get() + "'s turn", fg=colour[1])
        else:
            label1.config(text=entry1.get() + "'s turn", fg=colour[0])
        return

    def placesymbol(number):
        global dc
        global turn
        dc += 1
        buttons[number].config(text=options[turn], fg=colour[turn], disabledforeground=colour[turn])
        buttons[number]['state'] = tk.DISABLED
        buttons[number]['cursor'] = ''
        changelabel1()
        checkwin()
        swapturns()

    buttons = []

    # making buttons
    for i in range(9):
        i = i
        b = tk.Button(window, text=" ", font="Calibri 18", cursor='hand1', height=6, width=11, command=lambda i=i:
        placesymbol(i))
        buttons.append(b)

    # placing buttons onto grid
    i = 0
    for j in range(3):
        for k in range(3):
            buttons[i].grid(row=j, column=k)
            i += 1

    restartbutton = tk.Button(window, text='Restart', font=('calibri, 18'), cursor='hand1', height=2, width=10,
                              fg=restartbuttoncolour, relief="raised", command=restart)
    restartbutton.grid(row=5, column=1)

    label0 = tk.Label(window, text=entry1.get() + "'s score", font=('calibri 15 underline'), fg=colour[0])
    label0.grid(row=4, column=0)
    labelscore1 = tk.Label(window, text=0, font=('calibri, 25 '), fg=colour[0])
    labelscore1.grid(row=5, column=0)

    label1 = tk.Label(window, text=entry1.get() + "'s turn", font=('calibri 15 bold '), fg=colour[0])
    label1.grid(row=4, column=1)

    label2 = tk.Label(window, text=entry2.get() + "'s score", font=('calibri 15 underline'), fg=colour[1])
    label2.grid(row=4, column=2)
    labelscore2 = tk.Label(window, text=0, font=('calibri, 25'), fg=colour[1])
    labelscore2.grid(row=5, column=2)

    winlabels = []
    for i in range(3):
        winlabels.append(tk.Label(window, text=' ', font=('calibri, 30')))

    window.mainloop()


startpage = tk.Tk()
startpage.title("start page")
startpage.geometry("400x400")

b = ttk.Button(startpage, text="PLAY", width=20, command=play)
b.grid(row=11, column=1, padx=3, pady=3)
style = ttk.Style()

# user input 1

userinput1 = ttk.Label(startpage, text="Player 1: ", font=("Courier 22 bold"))
userinput1.grid(row=2, column=1)

frame1 = tk.Frame()
frame1.grid(row=4, column=1)
entry1 = ttk.Entry(startpage, width=40)
entry1.focus_set()
entry1.grid(row=3, column=1)


def entername1():
    global entry1
    if entry1.get() == '':
        entry1.insert(0, "Player 1")
        userinput1.config(text="Player 1")
    else:
        userinput1.config(text="Player 1: " + entry1.get())
    entry2.focus_set()


enterbutton = ttk.Button(frame1, text="Enter", width=10, command=entername1)
enterbutton.grid(row=4, column=1)


def clear1():
    userinput1.config(text="Player 1: ")
    entry1.delete(0, END)


clearbutton = ttk.Button(frame1, text="Clear", width=10, command=clear1)
clearbutton.grid(row=4, column=2)

# user input 2

userinput2 = ttk.Label(startpage, text="Player 2: ", font=("Courier 22 bold"))
userinput2.grid(row=5, column=1, pady=1)

frame2 = ttk.Frame()
frame2.grid(row=7, column=1)
entry2 = ttk.Entry(startpage, width=40)
entry2.grid(row=6, column=1)


def entername2():
    global entry2
    if entry2.get() == '':
        entry2.insert(0, "Player 2")
        userinput2.config(text="Player 2")
    else:
        userinput2.config(text="Player 2: " + entry2.get())


enterbutton = ttk.Button(frame2, text="Enter", width=10, command=entername2)
enterbutton.grid(row=7, column=1)


def clear2():
    userinput2.config(text="Player 2: ")
    entry2.delete(0, END)


clearbutton = ttk.Button(frame2, text="Clear", width=10, command=clear2)
clearbutton.grid(row=7, column=2)

startpage.mainloop()
