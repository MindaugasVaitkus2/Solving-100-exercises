#Create a program that asks the user to submit text through a GUI

#!/usr/bin/python3

from tkinter import *

gui_file = open ('../inputs&outputs/Ex98.txt', 'a+')

def save_and_delete():
    gui_file = open ('../inputs&outputs/Ex98.txt', 'a+')
    text = e.get() + "\n"
    gui_file.write(text)
    gui_file.close()
    e.delete(0, 'end')

def save_and_close():
    gui_file = open ('../inputs&outputs/Ex98.txt', 'a+')
    text = e.get() + "\n"
    gui_file.write(text)
    gui_file.close()
    e.delete(0, 'end')
    window.destroy()   

def add_line():
    text = e.get() + "\n"
    gui_file.write(text)
    e.delete(0, 'end')

window = Tk()
v = StringVar()
e = Entry (window, textvariable=v)


e.grid(row = 0, column = 0)


button1 = Button(window, text = "Add line", command = add_line).grid(row=0, column=1)
button2 = Button(window, text = "Save changes", command = save_and_delete).grid(row = 0, column = 2)
button3 = Button(window, text = "Save and Close", command = save_and_close).grid(row = 0, column = 3)

window.mainloop()

# how he did it:

# from tkinter import *
 
# window = Tk()
 
# file = open("user_gui.txt", "a+")
 
# def add():
#     file.write(e2_value.get() + "\n")
#     entry.delete(0, END)
 
# def save():
#     global file
#     file.close()
#     file = open("user_gui.txt", "a+")
 
# def close():
#     file.close
#     window.destroy()
 
# user_value = StringVar()
# entry = Entry(window, textvariable=user_value)
# entry.grid(row=0, column=0)
 
# button_add = Button(window, text="Add line", command=add)
# button_add.grid(row=0, column=1)
 
# button_save = Button(window, text="Save changes", command=save)
# button_save.grid(row=0, column=2)
 
# button_close = Button(window, text="Save and Close", command=close)
# button_close.grid(row=0,column=3)
 
# window.mainloop()
# Explanation:

# We're using the standard tkinter  library here. In line 3 we create the window of the interface and then we open a text file in a+  mode and we create three functions. These functions will be executed when the user presses one of the three buttons defined in line 24 through line 31. For example, button_add  is attached to the add  function, so when the button is pressed, the text that was entered in the Entry widget defined in line 21 is written in the text file. 