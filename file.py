from tkinter import *
import tkinter.filedialog as fd 
import os


def saveAs():
	a = text_area.get(0.0,END)
	files = [('All Files','*.*'),('Text Document','*.txt*')]
	sd = fd.asksaveasfilename(defaultextension=files)
	root.title(sd)
	with open(sd,'w') as file:
		file.write(a)

def openFile():
	of = fd.askopenfilename()
	root.title(of)
	with open(of,'r+') as f:
		text = f.read()
		text_area.insert(0.0,text)


def save():
	#global sd
	a = text_area.get(0.0,END)
	filename = root.title()
	with open(filename,'w') as file:
		file.write(a)


def cut():
	t = text_area.selection_get()
	text_area.delete('sel.first','sel.last')
	root.clipboard_clear()
	root.clipboard_append(t)

def copy():
	t = text_area.selection_get()
	root.clipboard_clear()
	root.clipboard_append(t)

def paste():
	t = root.clipboard_get()
	text_area.insert(text_area.index(INSERT),t)
	
	
def new():
	root.title('Untitled')
	text_area.delete(0.0,END)

def do_popup(event):
	try:
		edit.tk_popup(event.x_root,event.y_root)
	finally:
		edit.grab_release()


root = Tk()
root.title("Notepad--")
text_area = Text(root)

menubar = Menu(root)

filemenu = Menu(menubar)
filemenu.add_command(label="New",commmand = lambda: new())
filemenu.add_command(label="Open",command=lambda: openFile())
filemenu.add_command(label="Save",command=lambda : save())
filemenu.add_command(label="Save As",command=lambda : saveAs())

editmenu = Menu(menubar)
editmenu.add_command(label="Cut",command=lambda: cut())
editmenu.add_command(label="Copy",command=lambda: copy())
editmenu.add_command(label="Paste",command=lambda: paste())

edit = Menu(root)
edit.add_command(label="Cut",command=lambda: cut())
edit.add_command(label="Copy",command=lambda: copy())
edit.add_command(label="Paste",command=lambda: paste())


menubar.add_cascade(label="File",menu=filemenu)
menubar.add_cascade(label="Edit",menu=editmenu)

text_area.bind("<Button-3>",do_popup)

text_area.pack()
root.config(menu=menubar)
root.iconphoto(False,PhotoImage(file='icon.png'))
root.mainloop()
