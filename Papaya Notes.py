import sys
from tkinter import *
from tkinter.filedialog import askopenfilename

root=Tk("Text Editor")
text=Text(root) 
text.grid() 


def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation= askopenfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()

def openfile():
    savelocation= askopenfilename()
    file2=open(savelocation, "r+")
    text.insert('1.0', file2.read())
	
def FontHelvetica():
    global text
    text.config(font="Helvetica")

def FontCourier():
    global text
    text.config(font="Courier")

button=Button(root, text="Save", command=saveas) 
button.grid()
button=Button(root, text="Open", command=openfile) 
button.grid()
    
font=Menubutton(root, text="Font") 
font.grid() 
font.menu=Menu(font, tearoff=0) 
font["menu"]=font.menu
Helvetica=IntVar() 
arial=IntVar() 
times=IntVar() 
Courier=IntVar()
font.menu.add_checkbutton(label="Courier", variable=Courier, 
command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=Helvetica,
command=FontHelvetica) 

root.mainloop()
