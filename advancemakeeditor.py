from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror
class makeeditor(Frame):
	fonttype="Helvatica"
	fontsize=16
	filename = None
	#Fonts############################
	def fontHelvetica(self):
		text.config(font=("Helvetica",self.fontsize))
		self.fonttype="Helvatica"

	def fontArial(self):
		text.config(font=("Arial",self.fontsize))
		self.fonttype="Arial"

	def fontTNR(self):
		text.config(font=("Times New Roman",self.fontsize))
		self.fonttype="Times New Roman"

	def fontGothic(self):
		text.config(font=("Gothic",self.fontsize))
		self.fonttype="Gothic"

	#Hotkeys
	def newFileHK(self):
		self.filename=None
		text.delete(0.0, END)

	def saveFileHK(self):
		global filename
		if self.filename == None:
			saveAsHK()
		else:
			t = text.get(0.0, END)
			f = open(self.filename, "w")
			f.write(t)
			f.close()

	def saveAsHK(self,*args):
		f = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
		t = text.get(0.0, END)
		try:
			f.write(t.rstrip())
			f.close()
		except:
			showerror(title ="UPS", message="Could not save file")

	def openFileHK(self):
		f = filedialog.askopenfile(mode='r')
		t = f.read()
		f.close()
		text.delete(0.0, END)
		text.insert(0.0, t)

	#Loops commands

	def newFile(self):
		self.filename=None
		text.delete(0.0, END)

	def saveFile(self):
		if self.filename == None:
			saveAs()
		else:
			t = text.get(0.0, END)
			f = open(self.filename, "w")
			f.write(t)
			f.close()

	def saveAs(self,*args):
		f = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
		t = text.get(0.0, END)
		try:
			f.write(t.rstrip())
		except:
			showerror(title ="UPS", message="Could not save file")

	def openFile(self):
		f = filedialog.askopenfile(mode='r')
		try:
			t = f.read()
			text.delete(0.0, END)
			text.insert(0.0, t)
		except:
			pass
		
		
	def size16(self):
		text.config(font=(self.fonttype,16))
		self.fontsize=16
		
	def size18(self):
		text.config(font=(self.fonttype,18))
		self.fontsize=18
		
	def size20(self):
		text.config(font=(self.fonttype,20))
		self.fontsize=20

	def size22(self):
		text.config(font=(self.fonttype,22))
		self.fontsize=22
		
	def bgwhite(self):
		text.config(bg='white')
		
	def bgblack(self):
		text.config(bg='black')
		
	def bggray(self):
		text.config(bg='gray')
		
	def fgblue(self):
		text.config(fg='blue')

	def fggreen(self):
		text.config(fg='green')

	def fgorange(self):
		text.config(fg='orange')

	def __init__(self,root):	
		menubar = Menu(root)
		filemenu = Menu(menubar)
		filemenu.add_command(label="New", command=self.newFile, accelerator="Ctrl+N")
		filemenu.add_command(label="Open", command=self.openFile, accelerator="Ctrl+O")
		filemenu.add_command(label="Save", command=self.saveFile, accelerator="Ctrl+S")
		filemenu.add_command(label="Save as...", command=self.saveAs, accelerator="Ctrl+B")
		filemenu.add_separator()
		filemenu.add_command(label="Quit", command=root.quit, accelerator="Ctrl+Q")
		menubar.add_cascade(label="File", menu=filemenu)
		###############################################################################

		#####Hot-Keys#######################
		root.bind("<Control-n>", self.newFileHK)
		root.bind("<Control-o>", self.openFileHK)
		root.bind("<Control-s>", self.saveFileHK)
		root.bind("<Control-b>", self.saveAsHK)
		root.bind("<Control-q>", self.quit)
		####################################

		###################################################################
		formatOptions = Menu(menubar)
		formatOptions.add_command(label="Arial", command=self.fontArial)
		formatOptions.add_command(label="Helvetica", command=self.fontHelvetica)
		formatOptions.add_command(label="Times New Roman", command=self.fontTNR)
		formatOptions.add_command(label="Gothic", command=self.fontGothic)
		menubar.add_cascade(label="Font", menu=formatOptions)
		###################################################################

		###################################################################
		sizeOptions = Menu(menubar)
		sizeOptions.add_command(label="16", command=self.size16)
		sizeOptions.add_command(label="18", command=self.size18)
		sizeOptions.add_command(label="20", command=self.size20)
		sizeOptions.add_command(label="22", command=self.size22)
		menubar.add_cascade(label="Size", menu=sizeOptions)
		###################################################################

		###################################################################
		backgroundOptions = Menu(menubar)
		backgroundOptions.add_command(label="white", command=self.bgwhite)
		backgroundOptions.add_command(label="black", command=self.bgblack)
		backgroundOptions.add_command(label="gray", command=self.bggray)
		menubar.add_cascade(label="Background", menu=backgroundOptions)
		###################################################################

		###################################################################
		forgroundOptions = Menu(menubar)
		forgroundOptions.add_command(label="blue", command=self.fgblue)
		forgroundOptions.add_command(label="green", command=self.fggreen)
		forgroundOptions.add_command(label="orange", command=self.fgorange)
		menubar.add_cascade(label="Color", menu=forgroundOptions)
		###################################################################
		root.config(menu=menubar)

root = Tk()
root.title("Make File Editor")
root.minsize(width=500, height=400)
root.maxsize(width=root.winfo_screenwidth(),height=root.winfo_screenheight())
text = Text(root, width=500, height=500,fg="blue",font=("Helvatica",16))
text.pack()
master=makeeditor(root)	
root.mainloop()

