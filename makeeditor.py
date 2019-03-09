from tkinter import *
from tkinter import filedialog
fonttype="Helvatica"
fontsize=16
#Fonts############################
def fontHelvetica():
	global text,fonttype,fontsize
	text.config(font=("Helvetica",fontsize))
	fonttype="Helvatica"

def fontArial():
	global text,fonttype,fontsize
	text.config(font=("Arial",fontsize))
	fonttype="Arial"

def fontTNR():
	global text,fonttype,fontsize
	text.config(font=("Times New Roman",fontsize))
	fonttype="Times New Roman"

def fontGothic():
	global text,fonttype,fontsize
	text.config(font=("Gothic",fontsize))
	fonttype="Gothic"

#Hotkeys
def newFileHK(self):
	global filename
	filename = "Untitled"
	text.delete(0.0, END)

def saveFileHK(self):
	global filename
	if filename == None:
		saveAs(self)
	else:
		t = text.get(0.0, END)
		f = open(filename, "w")
		f.write(t)
		f.close()

def saveAsHK(self):
	f = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
	t = text.get(0.0, END)
	try:
		f.write(t.rstrip())
	except:
		showerror(title ="UPS", message="Could not save file")

def openFileHK(self):
	f = filedialog.askopenfile(mode='r')
	t = f.read()
	text.delete(0.0, END)
	text.insert(0.0, t)

#Loops commands
filename = None

def newFile():
	global filename
	filename = "Untitled"
	text.delete(0.0, END)

def saveFile():
	global filename
	if filename == None:
		saveAs(self)
	else:
		t = text.get(0.0, END)
		f = open(filename, "w")
		f.write(t)
		f.close()

def saveAs():
	f = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
	t = text.get(0.0, END)
	try:
		f.write(t.rstrip())
	except:
		showerror(title ="UPS", message="Could not save file")

def openFile():
	f = filedialog.askopenfile(mode='r')
	t = f.read()
	text.delete(0.0, END)
	text.insert(0.0, t)
	
def size16():
	global text,fonttype,fontsize
	text.config(font=(fonttype,16))
	fontsize=16
	
def size18():
	global text,fonttype,fontsize
	text.config(font=(fonttype,18))
	fontsize=18
	
def size20():
	global text,fonttype,fontsize
	text.config(font=(fonttype,20))
	fontsize=20

def size22():
	global text,fonttype,fontsize
	text.config(font=(fonttype,22))
	fontsize=22
	
def bgwhite():
	global text
	text.config(bg='white')
	
def bgblack():
	global text
	text.config(bg='black')
	
def bggray():
	global text
	text.config(bg='gray')
	
def fgblue():
	global text
	text.config(fg='blue')

def fggreen():
	global text
	text.config(fg='green')

def fgorange():
	global text
	text.config(fg='orange')

	

######################################################################

#Main GUI
root = Tk()
root.title("Make File Editor")
root.minsize(width=500, height=400)
root.maxsize(width=root.winfo_screenwidth(),height=root.winfo_screenheight())
text = Text(root, width=500, height=500,fg='blue',bg='white')
text.pack()

###############################################################################
menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile, accelerator="Ctrl+N")
filemenu.add_command(label="Open", command=openFile, accelerator="Ctrl+O")
filemenu.add_command(label="Save", command=saveFile, accelerator="Ctrl+S")
filemenu.add_command(label="Save as...", command=saveAs, accelerator="Ctrl+B")
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit, accelerator="Ctrl+Q")
menubar.add_cascade(label="File", menu=filemenu)
###############################################################################

#####Hot-Keys#######################
root.bind("<Control-n>", newFileHK)
root.bind("<Control-o>", openFileHK)
root.bind("<Control-s>", saveFileHK)
root.bind("<Control-b>", saveAsHK)
root.bind("<Control-q>", quit)
####################################

###################################################################
formatOptions = Menu(menubar)
formatOptions.add_command(label="Arial", command=fontArial)
formatOptions.add_command(label="Helvetica", command=fontHelvetica)
formatOptions.add_command(label="Times New Roman", command=fontTNR)
formatOptions.add_command(label="Gothic", command=fontGothic)
menubar.add_cascade(label="Font", menu=formatOptions)
###################################################################

###################################################################
sizeOptions = Menu(menubar)
sizeOptions.add_command(label="16", command=size16)
sizeOptions.add_command(label="18", command=size18)
sizeOptions.add_command(label="20", command=size20)
sizeOptions.add_command(label="22", command=size22)
menubar.add_cascade(label="Size", menu=sizeOptions)
###################################################################

###################################################################
backgroundOptions = Menu(menubar)
backgroundOptions.add_command(label="white", command=bgwhite)
backgroundOptions.add_command(label="black", command=bgblack)
backgroundOptions.add_command(label="gray", command=bggray)
menubar.add_cascade(label="Background", menu=backgroundOptions)
###################################################################

###################################################################
forgroundOptions = Menu(menubar)
forgroundOptions.add_command(label="blue", command=fgblue)
forgroundOptions.add_command(label="green", command=fggreen)
forgroundOptions.add_command(label="orange", command=fgorange)
menubar.add_cascade(label="Color", menu=forgroundOptions)
###################################################################

root.config(menu=menubar)
root.mainloop()

