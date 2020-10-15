import tkinter 
import tkinter as tk
import os	 
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class Notepad: 
    root=Tk()
    _file=None
    TextArea = Text(root)
    def __init__(self,**kwargs): 
        MenuBar = Menu(self.root)
        FileMenu = Menu(MenuBar, tearoff=0) 
        EditMenu = Menu(MenuBar, tearoff=0) 
        HelpMenu = Menu(MenuBar, tearoff=0) 
        ScrollBar = Scrollbar(self.TextArea)
        self.root.title("Untitled - Notepad") 
        self.root.geometry('500x500') 
        self.root.grid_rowconfigure(0, weight=1) 
        self.root.grid_columnconfigure(0, weight=1) 
        self.TextArea.grid(sticky = N + E + S + W) 
        FileMenu.add_command(label="New",command=self.newFile)
         
        # To open a already existing file 
        FileMenu.add_command(label="Open", command=self.openFile) 
        
        # To save current file 
        FileMenu.add_command(label="Save", command=self.saveFile)	 

        # To create a line in the dialog		 
        FileMenu.add_separator()										 
        FileMenu.add_command(label="Exit", command=self.quitApplication) 
        MenuBar.add_cascade(label="File", menu=FileMenu)	 
        
        # To give a feature of cut 
        EditMenu.add_command(label="Cut", command=self.cut)			 
    
        # to give a feature of copy	 
        EditMenu.add_command(label="Copy", command=self.copy)		 
        
        # To give a feature of paste 
        EditMenu.add_command(label="Paste", command=self.paste)

        EditMenu.add_command(label="Find", command=self.find_window)	 
        
        # To give a feature of editing 
        MenuBar.add_cascade(label="Edit", menu=EditMenu)	 
        
        # To create a feature of description of the notepad 
        HelpMenu.add_command(label="About Notepad", command=self.showAbout) 
        MenuBar.add_cascade(label="Help", menu=HelpMenu) 

        self.root.config(menu=MenuBar) 

        ScrollBar.pack(side=RIGHT,fill=Y)					 
        
        # Scrollbar will adjust automatically according to the content		 
        ScrollBar.config(command=self.TextArea.yview)	 
        self.TextArea.config(yscrollcommand=ScrollBar.set) 
    
        
    def quitApplication(self): 
        self.root.destroy() 
        # exit() 

    def showAbout(self): 
        showinfo("Notepad","This notepad is created by Nishaanth K") 

    def openFile(self): 
        
        self._file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")]) 

        if self._file == "": 
            
            # no file to open 
            self._file = None
        else: 
            
            # Try to open the file 
            # set the window title 
            self.root.title(os.path.basename(self._file) + " - Notepad") 
            self.TextArea.delete(1.0,END) 

            file = open(self._file,"r") 

            self.TextArea.insert(1.0,file.read()) 

            file.close() 

        
    def newFile(self): 
        self.root.title("Untitled - Notepad") 
        self._file = None
        self.TextArea.delete(1.0,END) 

    def saveFile(self): 

        if self._file == None: 
            # Save as new file 
            self._file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")]) 

            if self._file == "": 
                self._file = None
            else: 
                
                # Try to save the file 
                file = open(self._file,"w") 
                file.write(self.TextArea.get(1.0,END)) 
                file.close() 
                
                # Change the window title 
                self.root.title(os.path.basename(self._file) + " - Notepad") 
                
            
        else: 
            file = open(self._file,"w") 
            file.write(self.TextArea.get(1.0,END)) 
            file.close() 

    def find_window(self):
        app=tk.Tk()
        app.geometry('300x300')
        fram = Frame(app) 
        Label(fram,text='Text to find:').grid()  
        edit = Entry(fram)  
        edit.grid()  
        edit.focus_set()  
        butt = Button(fram, text='Find')   
        butt.grid()  
        fram.grid() 
        text = Text(app) 
        text.grid()
        find_btn = tk.Button(app, text = "New Window button")
        app.mainloop()
    
    def find(self): 
        self.TextArea.tag_remove('found', '1.0', END)  
        s = self.edit.get()  
        if s: 
            idx = '1.0'
            while 1: 
                idx = self.TextArea.search(s, idx, nocase=1, stopindex=END)  
                if not idx: 
                    break
            
                lastidx = '%s+%dc' % (idx, len(s))  
                self.TextArea.tag_add('found', idx, lastidx)  
                idx = lastidx 

            self.TextArea.tag_config('found', foreground='red')  
        self.edit.focus_set()

    def cut(self): 
        self.TextArea.event_generate("<<Cut>>") 

    def copy(self): 
        self.TextArea.event_generate("<<Copy>>") 

    def paste(self): 
        self.TextArea.event_generate("<<Paste>>")

    def search(self):
        
        dir_path = askdirectory()
        for root, files in os.walk(dir_path): 
            for file in files:  
                 if file.endswith('.txt'): 
                     print (root+'/'+str(file))
    
    def run(self): 

        # Run root application 
        self.root.mainloop()


notepad = Notepad()
notepad.run()
