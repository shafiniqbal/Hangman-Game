###### TEST FURTHER restart
# GUI version
import csv
import random
from string import ascii_lowercase
from tkinter import *
from tkinter import messagebox as mb


root = Tk()
root.title('Hangman')
root.iconbitmap(r'pikachu_icon-icons.com_67535.ico')
root.geometry("700x450")
root.configure(bg='grey')


def rand_word():
    global word
    global r
    rndm = random.randint(1, 92238)
    with open(r'Custom Words mid range.csv') as fd:
        read = csv.reader(fd)
        for i, j in enumerate(read):
            if i == rndm:
                word = j[0]
                r = len(word)
                print(word)  ###delete.............................




# All Frames
ftitle = Frame(root, bg='grey')
ftitle.grid(row=0, column=0, columnspan=8, sticky=W + E)
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
fbox = Frame(root, bg='grey', bd=2, relief=SUNKEN)
fbox.grid(row=1, column=0, columnspan=8, ipadx=90, sticky=W + E)
Grid.rowconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 0, weight=1)
ferror = Frame(root, bg='grey')
ferror.grid(row=2, column=0, columnspan=8, sticky=W + E)
Grid.rowconfigure(root, 2, weight=1)
Grid.columnconfigure(root, 0, weight=1)
fkey = Frame(root, bg='grey', border=1, relief=SUNKEN, pady=0)
fkey.grid(row=3, column=0, columnspan=8, sticky=N + S + W + E)
Grid.rowconfigure(root, 2, weight=1)
Grid.columnconfigure(root, 0, weight=1)

# Title Label
title = Label(ftitle, text='Welcome to the HANGMAN Game', bg='grey', fg='white', borderwidth=5, font=('Arial Bold', 20))
title.grid(row=0, column=0, sticky=W + E)
Grid.rowconfigure(ftitle, 0, weight=1)
Grid.columnconfigure(ftitle, 0, weight=1)




# Blank Space/ Entry Box
def dash():
    global box
    global r
    box = []
    for i in range(r):
        box.append(Entry(fbox, font=("Calibri", 25), justify="center", width=6, bg="#1E6FBA", fg="yellow",
                         disabledbackground="#1E6FBA", disabledforeground="yellow", highlightbackground="black",
                         highlightcolor="red", highlightthickness=1, bd=2))
        box[i].grid(row=0, column=i, padx=5, pady=15, sticky=W + E)
        Grid.rowconfigure(fbox, 0, weight=1)
        Grid.columnconfigure(fbox, i, weight=1)




# Length printing Label
def prlen():
    prln = Label(fbox, text='(Guess the ' + str(r) + ' lettered word...)',
                 bg='grey', fg='white', font=('Arial Bold', 12))
    prln.grid(row=1, column=0, columnspan=r - 1, sticky=W + E)
    Grid.rowconfigure(fbox, 1, weight=1)
    Grid.columnconfigure(fbox, 0, weight=1)




## Error Labels
def errchanger(error):
    chance = Label(ferror, text='You have only \' 6 \' chances', bg='grey', fg='white', borderwidth=5,
                   font=('Arial', 10))
    chance.grid(row=0, column=0, sticky=E)
    err = Label(ferror, text='Error : ' + str(error), bg='grey', fg='white', borderwidth=5, font=('Arial Bold', 10))
    err.grid(row=0, column=8, sticky=W + E)




# Control function
def cmd(char):
    global error
    global correct
    if char in done:  # Repeat button
        mb.showerror('Nope', 'You\'ve already Entered this...\nTry another...')
    else:  # New button
        done.append(char)
        if char in word:  # Right ans
            for i, j in enumerate(word):  # Put the right ans in box
                if j == char:
                    box[i].insert(0, char.upper())
                    correct += 1
            if correct == r:  # if win
                youwon()
        else:  # Wrong ans
            error += 1
            errchanger(error)  # Error counter
            if error == 6:  # if lose
                youlose()



# lose
def youlose():
    mb.showinfo('Oppsssss!', 'Answer was : ' + word.upper() + '\nBetter luck next time...')
    if mb.askyesno('???', 'Do you wanna play again?'):
        play()
    else:
        root.destroy()

# win
def youwon():
    mb.showinfo('Yeeee!!!', 'You did it...\nYou are a Genious for sure!')
    if mb.askyesno('???', 'Do you wanna play again? \U0001F914'):
        play()
    else:
        root.destroy()




## all buttons
def buttns():
    butt = []
    for i in ascii_lowercase:
        butt.append(Button(fkey, text=i.upper(), bg='grey', fg='white', command=lambda x=i: cmd(x)))
    frow = 7
    fcol = 0
    for i in range(26):
        butt[i].grid(row=frow, column=fcol, sticky=W + E + N + S)
        Grid.rowconfigure(fkey, frow, weight=1)
        Grid.columnconfigure(fkey, fcol, weight=1)
        fcol += 1
        if fcol == 8:
            fcol = 0
            frow += 1
        if i == 23:
            fcol = 3




def play():
    global done
    global box
    global correct
    global error
    done = []
    box = []
    correct = 0
    error = 0
    rand_word()
    dash()
    prlen()
    errchanger(error)
    buttns()

play()
root.mainloop()