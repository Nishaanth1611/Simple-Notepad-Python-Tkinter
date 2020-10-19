import os
import tkinter 
import tkinter as tk
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad: 
    root=Tk()
    _file=None
    TextArea = Text(root)
    def __init__(self,**kwargs): 
        #To intializing basic elements
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
 
        # To initialize features of file menu
        FileMenu.add_command(label="New",command=self.newfile)
        FileMenu.add_command(label="Open", command=self.openfile)
        FileMenu.add_command(label="Save", command=self.savefile)
        FileMenu.add_separator()										 
        FileMenu.add_command(label="Exit", command=self.quit) 
        MenuBar.add_cascade(label="File", menu=FileMenu)	 
        
        # To initialize features of edit menu
        EditMenu.add_command(label="Cut", command=self.cut)	 
        EditMenu.add_command(label="Copy", command=self.copy)
        EditMenu.add_command(label="Paste", command=self.paste)
        EditMenu.add_command(label="Find", command=self.find_window)
        MenuBar.add_cascade(label="Edit", menu=EditMenu)	 

        # To initialize features of help menu 
        HelpMenu.add_command(label="Info", command=self.info)
        HelpMenu.add_command(label="About Developers", command=self.dev)
        HelpMenu.add_command(label="Contact Us", command=self.contact)
        MenuBar.add_cascade(label="About", menu=HelpMenu)					 
        
        # To initialize features of scrollbar	 
        self.root.config(menu=MenuBar) 
        ScrollBar.pack(side=RIGHT,fill=Y)
        ScrollBar.config(command=self.TextArea.yview)	 
        self.TextArea.config(yscrollcommand=ScrollBar.set) 
    
    def run(self): 
        self.root.mainloop()    
    
    def quit(self): 
        self.root.destroy()

    def info(self): 
        showinfo("Info","This a Simple Notepad made from Python Tkinter.\nThis contain many scratchly made functions like New, Open, Save, Cut, Copy, Paste and Find.")

    def dev(self): 
        showinfo("About Developers","This notepad is developed by Nishaanth K and Heflin Stephen Raj S")

    def contact(self): 
        showinfo("Contact Us","Contact Us:\nNishaanth K : https://www.linkedin.com/in/nishaanth-k \nHeflin Stephen Raj S : https://www.linkedin.com/in/heflin-stephen-raj/ ")

    def newfile(self): 
        self.root.title("Untitled - Notepad") 
        self._file = None
        self.TextArea.delete(1.0,END)

    def openfile(self):
        self._file = askopenfilename(defaultextension=".txt", filetypes=[("Text Documents","*.txt"),("All Files","*.*")]) 
        if self._file == "": 
            # no file to open 
            self._file = None
        else: 
            # Try to open the file
            self.root.title(os.path.basename(self._file) + " - Notepad") 
            self.TextArea.delete(1.0,END) 
            file = open(self._file,"r") 
            self.TextArea.insert(1.0,file.read()) 
            file.close() 

    def savefile(self): 
        if self._file == None: 
            # Save as new file 
            self._file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("Text Documents","*.txt"),("All Files","*.*")]) 
            if self._file == "": 
                self._file = None
            else: 
                # Try to save the file 
                file = open(self._file,"w") 
                file.write(self.TextArea.get(1.0,END)) 
                file.close()                
                self.root.title(os.path.basename(self._file) + " - Notepad") 
                         
        else: 
            file = open(self._file,"w") 
            file.write(self.TextArea.get(1.0,END)) 
            file.close()

    def find_window(self):
        app=tk.Tk()
        app.title("find")
        app.minsize(250,100)
        info = Label(app,text='Enter the text to find: ')
        edit = Entry(app)  
        edit.focus_set()  
        btn = Button(app, text='Find')
        close = Button(app, text = "Close")
        close["command"] = lambda text= self.TextArea, app = app : self.find_clear(text,app) 
        btn["command"] = lambda text_to_search=edit, app= self.TextArea : self.find(app, text_to_search) 
        app.protocol("WM_DELETE_WINDOW", lambda text= self.TextArea, app = app : self.find_clear(text,app))
        info.grid(row=0,column=0)
        edit.grid(row=0,column=1)  
        btn.grid(row=2,column=0)  
        close.grid(row=2,column=1)
        
        app.mainloop()
    
    def find(self,text,app): 
        text.tag_remove('found', '1.0', END)  
        s = app.get()  
        if s: 
            idx = '1.0'
            while 1: 
                idx = text.search(s, idx, nocase=1,stopindex=END)  
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(s))  
                text.tag_add('found', idx, lastidx)  
                idx = lastidx 
        text.tag_config('found', foreground='white',background="black")  
        app.focus_set() 

    def find_clear(self,text, app):
        text.tag_remove('found', '1.0', END)
        app.destroy()
      
    def cut(self): 
        self.TextArea.event_generate("<<Cut>>") 

    def copy(self): 
        self.TextArea.event_generate("<<Copy>>") 

    def paste(self): 
        self.TextArea.event_generate("<<Paste>>")

notepad = Notepad()
notepad.run()
