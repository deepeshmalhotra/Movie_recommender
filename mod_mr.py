from csv import reader
from termcolor import colored
from tkinter import ttk
import tkinter as tk

win=tk.Tk()

#Label
name_label=ttk.Label(win,text='Enter your name- ')
name_label.grid(row=0,column=0)

#entrybox
name_var=tk.StringVar()
name_entrybox= ttk.Entry(win, width=50, textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

basis_label=ttk.Label(win,text='Okayy..so..tell me on what basis you want to watch movies..')
basis_label.grid(row=1,column=0)

choice1=tk.StringVar()
basis_btn= ttk.Radiobutton(win, text='Rating',value=1, textvariable=choice1)
basis_btn.grid(row=2,column=0)

choice2=tk.StringVar()
basis_btn= ttk.Radiobutton(win, text='Genre',value=1, textvariable=choice2)
basis_btn.grid(row=3,column=0)

win.title("Movie_Recommender")
win.mainloop()