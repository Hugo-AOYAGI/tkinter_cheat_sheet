from tkinter import *
import tkinter.messagebox
import inspect

master = 0
def setupMaster(root):
    global master
    master = root

def callbackSpaceBar(event, top):
    lbl = Label(top, text="User pressed the spacebar.")
    lbl.pack()

def appClosingHandler(top):
    if tkinter.messagebox.askokcancel("Quit", "Do you wish to quit ?"):
        top.destroy()
    else:
        top.lift()

def one_1():
    top = Toplevel(master)
    master.eval('tk::PlaceWindow %s center' % top.winfo_pathname(top.winfo_id()))
    top.bind("<space>", lambda x: callbackSpaceBar(x, top))

def one_2():
    top = Toplevel(master)
    master.eval('tk::PlaceWindow %s center' % top.winfo_pathname(top.winfo_id()))
    top.protocol("WM_DELETE_WINDOW", lambda:appClosingHandler(top))

def two_1():
    top = Toplevel(master)
    # Creating the widget and placing it, "master" is the tkinter window here
    frame = Frame(top, padx=5, pady=5, width=100, height=100)
    frame.pack(padx=10, pady=10)

def two_2():
    top = Toplevel(master)
    # Creating the widget and placing it, "master" is the tkinter window here
    lblframe = LabelFrame(top, text="Label Frame", padx=5, pady=5, width=100, height=100)
    lblframe.pack(padx=10, pady=10)

def two_3():
    top = Toplevel(master)
    # Creating the widget and placing it, "master" is the tkinter window here
    canv = Canvas(top, width=100, height=100)
    canv.pack()

    # Drawing a red rectangle on the canvas
    canv.create_rectangle(10, 10, 50, 30, fill="red")

def two_4():
    top = Toplevel(master)
    # Creating the widget and placing it, "master" is the tkinter window here
    lbl = Label(top, text="I am a label")
    lbl.pack()

def two_5():
    top = Toplevel(master)
    # Creating the widget and placing it, "master" is the tkinter window here
    msg = Message(top, text="This is a relatively long message.", width=50)
    msg.pack()

def two_6():
    top = Toplevel(master)
    # Creating the widget and placing it, "master" is the tkinter window here
    text = Text(top)
    text.pack()

    # Inserting text to the widget
    text.insert("end", "This is some text.", "tag") # Adding the tag as argument
    text.insert("end", "This is some other text.")
    # Configuring the tag
    text.tag_config("tag", background="blue", foreground="yellow")

def two_7():
    top = Toplevel(master)
    # Creating the widget and placing it, "master" is the tkinter window here
    btn = Button(top, text="I am a button", command=hello)
    btn.pack()

def two_8():
    top = Toplevel(master)
    # Creating the string variable
    v = StringVar()
    v.set("Default Value")
    
    # Creating the widget and placing it, "master" is the tkinter window here
    entry = Entry(top, textvariable=v)
    entry.pack()

def two_9():
    top = Toplevel(master)
    # Creating the string variable
    listvar = StringVar()
    listvar.set("one two three four")

    # Creating the widget and placing it, "master" is the tkinter window here
    listbox = Listbox(top, listvariable=listvar)
    listbox.pack()

def two_10():
    top = Toplevel(master)
    # Creating the widget and placing it, "master" is the tkinter window here
    mb =  Menubutton(top, text="options", relief=RAISED )
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
    top = Toplevel(master)
    # Creating the control variable
    variable = StringVar(master)
    
    # Setting the default value
    variable.set("one")

    # Creating the widget and placing it, "master" is the tkinter window here
    w = OptionMenu(top, variable, "one", "two", "three")
    w.pack()


def two_12():
    top = Toplevel(master)
    # Creating the control variable
    var = IntVar()

    # Creating the widget and placing it, "master" is the tkinter window here
    c = Checkbutton(top, text="Option", variable=var)
    c.pack()

def two_13():
    top = Toplevel(master)
    # Creating the control variable
    iv = IntVar()

    # Creating the two widgets and placing them, "master" is the tkinter window here
    Radiobutton(top, text="One", variable=iv, value=1).pack(anchor=W)
    Radiobutton(top, text="Two", variable=iv, value=2, indicatoron=0).pack(anchor=W)
    # The same variable is set to both radiobuttons so the user can only select one option

def two_14():
    top = Toplevel(master)
    # Creating the widget and placing it, "master" is the tkinter window here
    w = Spinbox(top, from_=0, to=10)
    w.pack()
    w1 = Spinbox(top, values=(2, 4, 6, 8, 10))
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
    top = Toplevel(master)
    # Creating the widget and placing it, "master" is the tkinter window here
    menubar = Menu(top)
    # Creating a pulldown menu, and adding it to the menu bar
    filemenu = Menu(menubar, tearoff=0)
        # Tearoff alows the user to spawn a new window containing the menu's options 
    # Add options for the pull down menu
    filemenu.add_command(label="Open", command=hello)
    filemenu.add_command(label="Save", command=hello)
    # Add a separator :  this will draw an horizontal line
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=top.destroy)
    # Add the menu widget to the menubar
    menubar.add_cascade(label="File", menu=filemenu)
    # Display the menu
    top.config(menu=menubar)


def two_18():
    top = Toplevel(master)
    # Creating the first paned window
    m = PanedWindow(top, orient="vertical")
    m.pack(fill=BOTH, expand=1)

    # Adding labels to the paned window
    top = Label(m, text="top pane", bg="red")
    m.add(top)

    bottom = Label(m, text="bottom pane", bg="yellow")
    m.add(bottom)


def hello():
    print("Hello !")


