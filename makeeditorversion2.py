from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror
	
class makeeditor(Frame):
	filename = None
	fonttype="Helvatica"
	fontsize=16
	background="White"
	fontcolor="Blue"
	wrap=NONE
	count=0
	#Font############################
	def font(self):
		frame=Tk()
		frame.minsize(300,300)
		frame.maxsize(width=(root.winfo_screenwidth()//3),height=(root.winfo_screenheight()//3))
		fonttype=StringVar(frame)
		fontsize=StringVar(frame)
		fonts={"Arial","Courier","Comic Sans MS","fixedsys","Helvatica","MS Sans Serif","MS Serif","Symbol","System","Times New Roman","Verdana"}
		sizes={10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68}
		fonttype.set(self.fonttype)
		fontsize.set(self.fontsize)
		Label(frame,text="Choose Font Type").grid(row=1,column=1,columnspan=3)
		Label(frame,text="Choose Font Size").grid(row=1,column=4,columnspan=3)
		fonttype_select=OptionMenu(frame,fonttype,*fonts)
		fontsize_select=OptionMenu(frame,fontsize,*sizes)
		fonttype_select.grid(row=3,column=1,columnspan=3)
		fontsize_select.grid(row=3,column=4,columnspan=3)
		b1=Button(frame,text="Ok",command=lambda:self.change(frame,fonttype.get(),fontsize.get()))
		b2=Button(frame,text="cancel",command=lambda:frame.destroy())
		b1.grid(row=7,column=3)
		b2.grid(row=7,column=7)
		frame.mainloop()
		
	def change(self,frame,a,b):
		self.fonttype=a
		self.fontsize=b
		text.config(font=(self.fonttype,self.fontsize))
		frame.destroy()
	#Hotkeys
	
	def color(self):
		frame=Tk()
		frame.minsize(300,300)
		frame.maxsize(width=(root.winfo_screenwidth()//3),height=(root.winfo_screenheight()//3))
		background=StringVar(frame)
		fontcolor=StringVar(frame)
		colors={'Black','White','Cyan', 'Azure', 'Yellow', 'Violet', 'Chartreuse', 'Blue', 'Magenta', 'Spring Green', 'Red', 'Orange', 'Green'}
		background.set(self.background)
		fontcolor.set(self.fontcolor)
		Label(frame,text="Choose Backgrond Color").grid(row=1,column=1,columnspan=3)
		Label(frame,text="Choose Font Color").grid(row=1,column=4,columnspan=3)
		background_select=OptionMenu(frame,background,*colors)
		fontcolor_select=OptionMenu(frame,fontcolor,*colors)
		background_select.grid(row=3,column=1,columnspan=3)
		fontcolor_select.grid(row=3,column=4,columnspan=3)
		b1=Button(frame,text="Ok",command=lambda:self.change2(frame,background.get(),fontcolor.get()))
		b2=Button(frame,text="cancel",command=lambda:frame.destroy())
		b1.grid(row=7,column=3)
		b2.grid(row=7,column=7)
		frame.mainloop()
		
	def change2(self,frame,a,b):
		if a==b:
			showerror(title="Same Color",message="Color Name Can't Be Same")
		else:
			self.background=a
			self.fontcolor=b
			text.config(bg=self.background,fg=self.fontcolor)
		frame.destroy()
	
	def wrapline(self):
		if self.count==1:
			self.wrap=NONE
			self.count=0
		elif self.count==0:
			self.wrap="word"
			self.count=1
		if self.wrap==NONE:
			xaxis=Scrollbar(root,orient="horizontal")
			xaxis.pack(side=BOTTOM, fill=X)
			text.config(xscrollcommand=xaxis.set)
			text.config(wrap=self.wrap)
		else:
			text.config(wrap=self.wrap)
	def newFileHK(self):
		text.delete(0.0, END)
		self.filename=None

	def saveFileHK(self):
		if self.filename == None:
			self.saveAsHK()
		else:
			t = text.get(0.0, END)
			f = open(self.filename, "w")
			f.write(t)
			f.close()

	def saveAsHK(self,*args):
		f = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
		t = text.get(0.0, END)
		try:
			f.write(t)
			f.close()
		except:
			showerror(title ="File Selection Error", message="Could not save file")

	def openFileHK(self):
		f = filedialog.askopenfile(mode='r')
		try:
			t = f.read()
			f.close()
			text.delete(0.0, END)
			text.insert(0.0, t)
		except:
			pass
	#Loops commands

	def newFile(self):
		self.filename=None
		text.delete(0.0, END)

	def saveFile(self):
		if self.filename == None:
			self.saveAs()
		else:
			t = text.get(0.0, END)
			f = open(self.filename, "w")
			f.write(t)
			f.close()

	def saveAs(self):
		f = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
		t = text.get(0.0, END)
		try:
			f.write(t)
		except:
			showerror(title ="File Selection Error", message="Could not save file")

	def openFile(self):
		f = filedialog.askopenfile(mode='r')
		try:
			t = f.read()
			text.delete(0.0, END)
			text.insert(0.0, t)
		except:
			pass
		

	def __init__(self,root):
		if self.wrap==NONE:
			xaxis=Scrollbar(root,orient="horizontal")
			xaxis.pack(side=BOTTOM, fill=X)
			text.config(xscrollcommand=xaxis.set)
		
		yaxis=Scrollbar(root,orient="vertical")
		yaxis.pack(side=RIGHT, fill=Y)
		text.pack(side=LEFT,fill=Y)
		text.config(yscrollcommand=yaxis.set)
		
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
		root.bind("<Control-n>", lambda event:self.newFileHK())
		root.bind("<Control-o>", lambda event:self.openFileHK())
		root.bind("<Control-s>", lambda event:self.saveFileHK())
		root.bind("<Control-b>", lambda event:self.saveAsHK())
		root.bind("<Control-q>", lambda event:self.quit())
		####################################

		
		viewOptions=Menu(menubar)
		viewOptions.add_command(label="Font",command=self.font)
		viewOptions.add_command(label="Size",command=self.font)
		menubar.add_cascade(label="Format",menu=viewOptions)

		####################################
		colorOptions=Menu(menubar)
		colorOptions.add_command(label="Background",command=self.color)
		colorOptions.add_command(label="Font Color",command=self.color)
		menubar.add_cascade(label="Color",menu=colorOptions)
		root.config(menu=menubar)
		###################################
		wrapOptions=Menu(menubar)
		self.var=IntVar()
		wrapOptions.add_checkbutton(label="Wrap",variable=self.var.get(),command=self.wrapline)
		menubar.add_cascade(label="View",menu=wrapOptions)

root = Tk()
root.title("Make File Editor")
root.minsize(width=500, height=400)
root.maxsize(width=root.winfo_screenwidth(),height=root.winfo_screenheight())
text = Text(root, width=500, height=500,fg="blue",font=("Helvatica",16),wrap=NONE)
master=makeeditor(root)	
root.mainloop()