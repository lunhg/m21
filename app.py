from Tkinter import *
from main import *

NAME = "Mupy"
VERSION = "0.0.1"

class App:
    def __init__(self, root):

        # frame
        self.frame = Frame(root)

        # inserir no root
        self.frame.pack()

        # fazer menu
        menu = Menu(root)
        root.config(menu=menu)
    
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=self.newFile)
        filemenu.add_command(label="Open...", command=self.openFile)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit_frame)

        helpmenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.about)

        
        # Inputs
        texts = [
            "search", 
            "fragmentize",
            "scramble pitch",
            "scramble octave",
            "show original",
            "process"
            ]

        self.inputs = []
        for i in range(0, len(texts)):
            _input = 0
            _frame = Frame(self.frame)
            if i == 0:       
                _label = Button(_frame, text=texts[i],command=self.search).grid(row=i,column=1)
                _input = Entry(_frame)
                _input.grid(row=i, column=0)
                _frame.grid()
            if i == 1:
                _label = Label(_frame, text=texts[i]).grid(row=i)
                for j in range(6):
                    v = IntVar()
                    rb = Radiobutton(_frame, text=j, variable=v, value=j).grid(row=i+1,column=j)
                
            elif i >= 2 and i<5:
                _input = Checkbutton(_frame, text=texts[i])
                _input.grid(row=i+1, column=j, sticky=W)
            else:
                _input = Button(_frame, text=texts[i], command=self.processar)
                _input.grid(row=i+1)

            _frame.grid(row=i)
            self.inputs.append(_input)
        
        # Console
        term = Frame(self.frame, width=300, height=300)
        term.grid(row=7)
        self.wid = term.winfo_id()
        
        # rodar
        root.mainloop()
    
    def search():
        o = Object()
        words = self.inputs[0].get().split(" ")
        command({"--search-only": True, "composer": words[0], "index": words[1]})
        
    def processar():
        
        i = self.inputs[1].get()
        n, o, _o = 0
        if self.inputs[3].get() == False:
            n = ""
        else:
            n = "-n"

        if self.inputs[4].get() == False:
            n = ""
        else:
            n = "-o"

        if self.inputs[5].get() == False:
            n = ""
        else:
            n = "-O"
     
    def command(options):
        command = "python main.py"
        for k,v in options:
            command += " --%s %s" % (k, v)
        
        xterm = "xterm -into %d -geometry 40x20 &" % (self.wid, command)
        os.system(xterm)

    def newFile():
        print "=> Creating new file"

    def openFile():
        print "=> new file"

    def quit_frame():
        print "=> Exiting"
        frame.quit
        
    def about():
        print "=> about"

# App
app = App(Tk())
