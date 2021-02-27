from tkinter import Tk, Frame, Menu, Toplevel, Button


class M21(Frame):

    def __init__(self, **kwargs):
        super().__init__()
        self.title = kwargs.get('title')
        self.initUI()

    def initUI(self):
        # Base title
        self.master.title(self.title)

        # Main menu
        menubar = Menu(self.master)

        # Filemenu
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New",        command=self.__pass__)
        filemenu.add_command(label="Open",       command=self.__pass__)
        filemenu.add_command(label="Save",       command=self.__pass__)
        filemenu.add_command(label="Save as...", command=self.__pass__)
        filemenu.add_command(label="Close",      command=self.__pass__)
        filemenu.add_separator()
        filemenu.add_command(label="Exit",       command=self.master.quit)

        # Edit menu
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo",       command=self.__pass__)
        editmenu.add_separator()
        editmenu.add_command(label="Cut",        command=self.__pass__)
        editmenu.add_command(label="Copy",       command=self.__pass__)
        editmenu.add_command(label="Paste",      command=self.__pass__)
        editmenu.add_command(label="Delete",     command=self.__pass__)
        editmenu.add_command(label="Select All", command=self.__pass__)

        # tools menu
        toolsmenu = Menu(menubar, tearoff=0)
        toolsSubmenuShowIn = Menu(toolsmenu)
        toolsSubmenuSearchIn = Menu(toolsmenu)

        # tools submenu show in
        toolsSubmenuShowIn.add_command(label="Musescore")
        toolsSubmenuShowIn.add_command(label="Frescobaldi")

        # tools submenu search in
        toolsSubmenuSearchIn.add_command(label="Core Corpus")
        toolsSubmenuSearchIn.add_command(label="Local Corpus")

        # add tools's submenus to itself
        toolsmenu.add_cascade(label="Show in",
                              menu=toolsSubmenuShowIn, underline=0)
        toolsmenu.add_cascade(label="Search in",
                              menu=toolsSubmenuSearchIn, underline=0)

        # Helpmenu
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.__pass__)
        helpmenu.add_command(label="About...",   command=self.__pass__)

        # Join
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Edit", menu=editmenu)
        menubar.add_cascade(label="Tools", menu=toolsmenu)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.master.config(menu=menubar)

    def onExit(self):
        self.quit()

    def __pass__(self):
        filewin = Toplevel(self.master)
        button = Button(filewin, text="Do nothing button")
        button.pack()


def main(**kwargs):
    root = Tk()
    root.geometry(kwargs.get('geometry'))
    app = M21(title=kwargs.get('title'))
    root.mainloop()
