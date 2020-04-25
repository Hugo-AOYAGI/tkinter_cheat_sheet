from tkinter import *
import inspect

master = Tk()


def two_1():
    # Creating the widget and placing it, "master" is the tkinter window here
    frame = Frame(master, padx=5, pady=5, width=100, height=100)
    frame.pack(padx=10, pady=10)

def two_2():
    # Creating the widget and placing it, "master" is the tkinter window here
    lblframe = LabelFrame(master, text="Label Frame", padx=5, pady=5, width=100, height=100)
    lblframe.pack(padx=10, pady=10)

def two_3():
    # Creating the widget and placing it, "master" is the tkinter window here
    canv = Canvas(master, width=100, height=100)
    canv.pack()

    # Drawing a red rectangle on the canvas
    canv.create_rectangle(10, 10, 50, 30, fill="red")

def two_4():
    # Creating the widget and placing it, "master" is the tkinter window here
    lbl = Label(master, text="I am a label")
    lbl.pack()

def two_5():
    # Creating the widget and placing it, "master" is the tkinter window here
    msg = Message(master, text="This is a relatively long message.", width=50)
    msg.pack()

def two_6():
    # Creating the widget and placing it, "master" is the tkinter window here
    text = Text(master)
    text.pack()

    # Inserting text to the widget
    text.insert("end", "This is some text.", "tag") # Adding the tag as argument
    text.insert("end", "This is some other text.")
    # Configuring the tag
    text.tag_config("tag", background="blue", foreground="yellow")

def two_7():
    # Creating the widget and placing it, "master" is the tkinter window here
    btn = Button(master, text="I am a button", command=hello)
    btn.pack()

def two_8():
    # Creating the string variable
    v = StringVar()
    v.set("Default Value")
    
    # Creating the widget and placing it, "master" is the tkinter window here
    entry = Entry(master, textvariable=v)
    entry.pack()

def two_9():
    # Creating the string variable
    listvar = StringVar()
    listvar.set("one two three four")

    # Creating the widget and placing it, "master" is the tkinter window here
    listbox = Listbox(master, listvariable=listvar)
    listbox.pack()

def two_10():
    # Creating the widget and placing it, "master" is the tkinter window here
    mb =  Menubutton(master, text="options", relief=RAISED )
    mb.grid()
    # Linking a menu to that menu button
    mb.menu =  Menu(mb, tearoff=0)
    # Tearoff alows the user to spawn a new window containing the menu's options
    mb["menu"] =  mb.menu

    # Creating the control variables
    oneVar = IntVar()
    twoVar = IntVar()

    # Adding the checkbuttons to the menu
    mb.menu.add_checkbutton (label="one", variable=oneVar)
    mb.menu.add_checkbutton (label="two", variable=twoVar)

    mb.pack()

def two_11():
    # Creating the control variable
    variable = StringVar(master)
    
    # Setting the default value
    variable.set("one")

    # Creating the widget and placing it, "master" is the tkinter window here
    w = OptionMenu(master, variable, "one", "two", "three")
    w.pack()


def two_12():
    # Creating the control variable
    var = IntVar()

    # Creating the widget and placing it, "master" is the tkinter window here
    c = Checkbutton(master, text="Option", variable=var)
    c.pack()

def two_13():
    # Creating the control variable
    v = IntVar()

    # Creating the two widgets and placing them, "master" is the tkinter window here
    Radiobutton(master, text="One", variable=v, value=1).pack(anchor=W)
    Radiobutton(master, text="Two", variable=v, value=2, indicatoron=0).pack(anchor=W)
    # The same variable is set to both radiobuttons so the user can only select one option

def two_14():
    # Creating the widget and placing it, "master" is the tkinter window here
    w = Spinbox(master, from_=0, to=10)
    w.pack()
    w1 = Spinbox(master, values=(2, 4, 6, 8, 10))
    w1.pack()

def two_15():
    # Creating the window
    root = Tk()
    # Setting its name and size
    root.title("Root Window")
    root.geometry("400x200")

def two_16():
    top = Toplevel(master)

def two_17():
    # Creating the widget and placing it, "master" is the tkinter window here
    menubar = Menu(master)

    # Creating a pulldown menu, and adding it to the menu bar
    filemenu = Menu(menubar, tearoff=0)
    # Add options for the pull down menu
    filemenu.add_command(label="Open", command=hello)
    filemenu.add_command(label="Save", command=hello)
    # Add a separator :  this will draw an horizontal line
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=master.destroy)
    # Add the menu widget to the menubar
    menubar.add_cascade(label="File", menu=filemenu)

    # Creating more pulldown menus
    editmenu = Menu(menubar, tearoff=1)
    # Tearoff alows the user to spawn a new window containing the menu's options
    editmenu.add_command(label="Cut", command=hello)
    editmenu.add_command(label="Copy", command=hello)
    editmenu.add_command(label="Paste", command=hello)
    menubar.add_cascade(label="Edit", menu=editmenu)
    
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=hello)
    menubar.add_cascade(label="Help", menu=helpmenu)

    # Display the menu
    master.config(menu=menubar)


def two_18():
    # Creating the first paned window
    m1 = PanedWindow()
    m1.pack(fill=BOTH, expand=1)

    # Adding a label to the paned window
    left = Label(m1, text="left pane")
    m1.add(left)

    # Creating a second paned window within the first one to create a 3-paned window
    m2 = PanedWindow(m1, orient=VERTICAL)
    m1.add(m2)

    # Adding labels to the second paned window
    top = Label(m2, text="top pane")
    m2.add(top)

    bottom = Label(m2, text="bottom pane")
    m2.add(bottom)


def getCode(func):
    lines = inspect.getsource(func))
    return lines
    


def hello():
    print("Hello !")

two_9()
mainloop()
