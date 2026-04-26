from tkinter import *
from tkinter import messagebox
import random

def no():
    messagebox.showinfo( ' ', "haha, its fixed then. its a date")
    quit()

def motionMouse(event):
    btnYes.place(x=random.randint(0, 500), y=random.randint(0, 500))

root = Tk()
root.geometry('1000x500')
root.title("survey")
root.resizable(width=False, height=False)
root['bg'] = 'white'

label = Label(root, text='so whats the end verdict? are we meeting again? (emotionally available?)', font='Arial 20 bold').pack()
btnYes = Button(root, text='(in a polite tone) NO', font= 'Arial 20 bold')
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>', motionMouse)
btnNo = Button(root, text='yeah! ', font= 'Arial 20 bold', command=no).place(x=350, y=100)

root.mainloop()
