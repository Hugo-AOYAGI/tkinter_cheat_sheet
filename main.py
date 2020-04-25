import tkinter as tk
import time
import os
from ctypes import windll
import examples as exs
import tkinter.messagebox

windll.shcore.SetProcessDpiAwareness(1)

class Window:
    def __init__(self, title, size):
        self.root = tk.Tk()
        # Setting window title
        self.root.title(title)

        #Setting window size
        self.root.geometry("{}x{}".format(size[0], size[1]))

        # Default variable values
        self.style_sheet = {"__none__": {}} # Handles all the widget styling
        self.menus = {} # Stores all the menus (tk Frames)
        self.shortcuts = {} # Stores all the keyboard shortcuts
        self.lastIteration = 0 # Stores the last time the Loop method was called to allow constant frame rate
        self.frame_rate = 15 # Stores frame rate, default = 15 fps
        self.process = True # Stores if window is still open
        self.widgets = {} # Stores the widgets
        self.current_menu = self.addMenu("root") # Creates the default menu
        self.images = {}

        # Change self.process value on window close
        self.root.protocol("WM_DELETE_WINDOW", self.close_handler)
        self.onStart()
    
    # FUNCTIONS TO BE CREATED BY USER ===>

    def onStart(self):
        pass

    def update(self):
        pass

    def checkInputs(self):
        pass

    # <===

    # Load all the images in a folder
    def loadImagesFromFolder(self, directory):
        allowed = [".png", ".jpg", ".PNG", ".gif"]
        for filename in os.listdir(directory):
            for suf in allowed:
                if filename.endswith(suf):
                    self.images.update({filename.replace(suf, ""): tk.PhotoImage(file=os.path.join(directory, filename))})
                    break

    # Changes the current menu
    def goToMenu(self, menu):
        # self.current_menu.lower()
        tk.Misc.lower(self.current_menu)
        self.current_menu = self.menus[menu]
        # self.current_menu.lift()
        tk.Misc.lift(self.current_menu)

    # Adds a menu to the window 
    def addMenu(self, name, autoplace = True, canvas = False, style = "__none__", **kwargs):
        arguments = dict(self.style_sheet[style], **kwargs)
        # Check if shoud create canvas or frame
        frame = tk.Frame(self.root, arguments) if not canvas else tk.Canvas(self.root, arguments)
        self.menus.update({name: frame})
        if autoplace:
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        return frame
    
    # Gets called when the user presses the close button
    def close_handler(self):
        self.process = False
        self.root.destroy()

    # Adds a keyboard shortcut to the app
    def addShortcut(self, keySym, command, widget = False):
        binder = widget if widget != False else self.root
        binder.bind(keySym, command)
    
    # Adds a widget to the window
    def addWidget(self, menu, name, cls, style = "__none__", **kwargs):
        arguments = dict(self.style_sheet[style], **kwargs)
        widget = cls(self.menus[menu], arguments)
        self.widgets.update({name: widget})
        return widget

    # Retrieves the styling from the stylesheet
    def getStyling(self, style):
        return style if isinstance(style, dict) else self.style_sheet[style]
    
    # Allows for shorter syntax in the code when placing a widget with a tuple of size and position
    def place(self, name, tup, isMenu = False):
        widget = self.widgets[name] if not isMenu else self.menus[name]
        widget.place(relx=tup[0], rely=tup[1], relwidth=tup[2], relheight=tup[3])
    
    # Load a style sheet for the app
    def addStyleSheet(self, path, separate_tags = False):
        if separate_tags:
            self.style_sheet, self.tags = loadStyleSheet(path, separate_tags)
        else:
            self.style_sheet = loadStyleSheet(path, False)
    
    def Loop(self):
        # Get constant frame rate by checking last iteration
        if time.time() - self.lastIteration < 1/self.frame_rate:
            time.sleep(1/self.frame_rate - (time.time() - self.lastIteration))
        self.lastIteration = time.time()
        # Update the window and canvas if there is one
        self.checkInputs()
        self.update()
    
class CheatSheet(Window):
    def onStart(self):
        # Setting up the window's properties
        self.root.resizable(False, False)
        self.root.iconbitmap("assets/icons/icon.ico")
        self.addStyleSheet('style.txt', True)
        # Setting up the different categories
        self.categories = ["EVENTS LIST", "WIDGET LIST", "WIDGET\nPROPERTIES"]
        self.loadImagesFromFolder("assets")
        self.loadImagesFromFolder("assets/CodeExamples")
        self.current_article = 0
        exs.setupMaster(self.root)
        # Setting up the different menus
    
        # Navigation frame
        self.addMenu("nav", False, False, "nav_s")
        self.place("nav", (0.80, 0.15, 0.20, 0.85), True)
        
        # Adding all the navigation buttons
        for i, category in enumerate(self.categories):
            self.addWidget("nav", "navBtn" + str(i), tk.Button, "navBtn_s", text=category, command=lambda x=i: self.goToArticle(x + 1))
            self.place("navBtn" + str(i), (0, i*1/len(self.categories), 1, 1/len(self.categories) - 0.002))

        # Header frame
        self.addMenu("head", False, False, "head_s")
        self.place("head", (0, 0, 1, 0.15), True)

        self.addWidget("head", "titleMain", tk.Label, "titleMain_s", text="TKINTER CHEAT SHEET")
        self.place("titleMain", (0, 0, 1, 1))

        self.addWidget("head", "homeBtn", tk.Button, "homeBtn_s", image=self.images['home_icon'], command=lambda: self.goToArticle(0))
        self.place("homeBtn", (0.9, 0.2, 0.1, 0.6))

        # Default Main
        self.addMenu("article0", False, True, "article_s", scrollregion=(0,0,2000,800))
        self.place("article0", (0, 0.15, 0.8, 1), True)

        # Get the canvas dimensions
        self.root.update()
        self.can_w, self.can_h = self.menus["article0"].winfo_width(), self.menus["article0"].winfo_height()
        
        self.addWidget("article0", "article0img", tk.Label, image=self.images["article0"])
        self.menus["article0"].create_window(self.can_w/2, self.can_h/2.15, window=self.widgets["article0img"])

        # Mouse Wheel Event
        self.menus["article0"].bind_all("<MouseWheel>", self.onMousewheel)

        # Creating all the articles
        self.setupArticle1()
        self.setupArticle2()
        self.setupArticle3()

        self.goToMenu("article0")


    def onMousewheel(self, event):
        self.current_menu.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def goToArticle(self, i):
        self.current_article = i
        self.goToMenu("article" + str(i))
        no_scroll_articles = [0, 3]
        if not i in no_scroll_articles:
            self.resetScrollBar()
    
    def resetScrollBar(self):
        # Scroll Bar setup
        if "scrollbar" in self.widgets:
            self.widgets["scrollbar"].destroy()
        self.addWidget("article" + str(self.current_article), "scrollbar", tk.Scrollbar, orient="vertical", command=self.menus["article0"].yview)
        self.place("scrollbar", (0.973, 0, 0.025, 1*0.85))
        self.current_menu.config(yscrollcommand=self.widgets["scrollbar"].set)
        self.current_menu.bind_all("<MouseWheel>", self.onMousewheel)
        self.widgets["scrollbar"].config(command=self.current_menu.yview)
    
    def runExampleSeeCode(self, func, name):
        # Setting up window
        top = tk.Toplevel(self.root)
        top.geometry("800x550")
        top.title("Code Example")
        top.resizable(False, False)
        top.iconbitmap("assets/icons/icon.ico")
        # Adding widgets to the window
        background = tk.Label(top, image=self.images["ex_background1"])
        background.place(relx=0, rely=0, relwidth=1, relheight=1)

        code = tk.Label(top, image=self.images[name], bg="#37474f")
        code.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)

        top.bind("<Button-1>", lambda x: self.callfuncbtn(x, (690, 10, 780, 70), func))

    def callfuncbtn(self, event, rect, func):
        if event.x > rect[0] and event.x < rect[2] and event.y > rect[1] and event.y < rect[3]:
            if isinstance(func, str):
                eval(func + "()")
            else:
                func()
            
    def get_attributes(self, widget):
        widg = widget
        keys = widg.keys()
        properties = {}
        for key in keys:
            value = widg[key] if widg[key] else 'N/A'
            vtype = str(type(value))
            # Formatting the type
            vtype = vtype.replace("<class '", "").replace("'>", "")
            vtype = vtype.replace("_tkinter.Tcl_Obj", "TCL Object").replace("tkinter.Menu", "Menu").replace("int", "Integer").replace("str", "String")
            properties.update({key: [value, vtype]})
        # Creating properties window
        top = tk.Toplevel(self.root)
        top.geometry("800x550")
        top.title("Widget Properties")
        top.resizable(False, False)
        top.iconbitmap("assets/icons/icon.ico")
        # Adding header
        head = tk.Label(top, text="This is the title lolz")
        head.place(relx=0, rely=0, relwidth=1, relheight=0.2)
        # Adding listbox
        maxheight = 50*len(properties.keys()) + 450
        canv = tk.Canvas(top, scrollregion=(0, 0, 800, maxheight))
        canv.place(relx=0, rely=0, relwidth=1, relheight=1)
        sb = tk.Scrollbar(top, orient="vertical")
        sb.pack(side="right", fill="y")
        canv.config(yscrollcommand=sb.set)
        sb.config(command=canv.yview)
        canv.create_image((400, 2500), image=self.images["prop_win_main"])
        for i ,key in enumerate(properties.keys()):
            canv.create_image((400, 190+i*55), image=self.images["prop_win_prop"])
            canv.create_text(85, 190+i*55, text=key, font="Verdana 10",anchor="w", fill="#299200")
            canv.create_text(505, 190+i*55, text=properties[key][1], font="Verdana 8",anchor="e", fill="#0c7cba")
            canv.create_text(550, 190+i*55, text=properties[key][0], font="Verdana 8",anchor="w", fill="#0c7cba")
        canv.create_text(350, 65, text=widget.winfo_class(), anchor="w", font="Verdana 20 bold", fill="#19967d")
        widget.destroy()
        
    def setupArticle1(self):
        self.addMenu("article1", False, True, "article_s", scrollregion=(0,0,1000,6000))
        self.place("article1", (0, 0.15, 0.8, 1), True)
        self.addWidget("article1", "article1img", tk.Label, image=self.images["article1"])
        self.menus["article1"].create_window(self.can_w/2, self.can_h*3.6, window=self.widgets["article1img"])

        self.addWidget("article1", "trybtn1-1", tk.Button, "try_it_btn_s", command = exs.one_1)
        self.menus["article1"].create_window(118, 800, window=self.widgets["trybtn1-1"])

        self.addWidget("article1", "trybtn1-2", tk.Button, "try_it_btn_s", command = exs.one_2)
        self.menus["article1"].create_window(118, 5628, window=self.widgets["trybtn1-2"])
    
    def setupArticle2(self):
        self.addMenu("article2", False, True, "article_s", scrollregion=(0,0,1000,4150))
        self.place("article2", (0, 0.15, 0.8, 1), True)
        self.addWidget("article2", "article2img", tk.Label, image=self.images["article2"])
        self.menus["article2"].create_window(self.can_w/2, self.can_h*2.5, window=self.widgets["article2img"])

        btn_positions = [1495, 1590, 1685, 2040, 2130, 2220, 2590, 2675, 2765, 2900, 3030, 3120, 3205, 3335, 3570, 3660, 3790, 3920]
        for i, pos in enumerate(btn_positions):
            self.addWidget("article2", "trybtn2-" + str(i+1), tk.Button, image=self.images["seeExBtn"], highlightthickness=0, bd=0, command=lambda x=i: self.runExampleSeeCode("exs.two_{}".format(x+1), "2_{}".format(x+1)))
            self.menus["article2"].create_window(1000, pos, window=self.widgets["trybtn2-" + str(i+1)])
        
    def setupArticle3(self):
        self.addMenu("article3", False, True, "article_s", scrollregion=(0,0,1000,800))
        self.place("article3", (0, 0.15, 0.8, 1), True)
        self.addWidget("article3", "article3img", tk.Label, image=self.images["article3"])
        self.menus["article3"].create_window(self.can_w/2, self.can_h/2.35, window=self.widgets["article3img"])
        self.widgets["article3img"].bind("<Button-1>", self.buttonGridCallBack)
        
    def buttonGridCallBack(self, event):
        init_y = 241
        hz = [178, 665]
        w, h = 412, 45
        widgets = [[tk.Frame, tk.LabelFrame, tk.Canvas, tk.Label, tk.Message, tk.Text, tk.Button, tk.Entry, tk.Listbox], [tk.Menubutton, "OptionMenu", tk.Checkbutton, tk.Radiobutton, tk.Spinbox, "Tk", tk.Menu, tk.Toplevel, tk.PanedWindow]]
        for i in range(2):
            for j in range(9):
                if event.x > hz[i] and event.x < hz[i] + w and event.y > init_y + h*j and event.y < init_y + h*(j+1):
                    # Handling some problematic cases
                    if widgets[i][j] == "Tk":
                        tkinter.messagebox.showinfo("Widget Properties", "The Tk widget does not have any properties !\nIts attributes are set using methods such as geometry or title.\n To learn more about those, read the 'Tkinter Functions' part.")
                    elif widgets[i][j] == "OptionMenu":
                        v = tk.StringVar(self.root)
                        self.get_attributes(tk.OptionMenu(self.root, v, "0", "1", "2"))
                    else:
                        self.get_attributes(widgets[i][j](self.root))


def openCheatSheet():
    cs = CheatSheet("Tkinter Cheat Sheet", (1400, 800))
    cs.root.mainloop()

def loadStyleSheet(path, separate_tags):
    style_sheet = {}
    tags_dict = {}
    # Opening file
    with open(path, "r") as css_file:
        file_string = css_file.read()
        file_string = file_string.replace("\n", "")
        file_string = file_string.replace("}", "{")
        # Getting all the css class names and properties as array elements
        file_array = file_string.split("{")
        for k in range(int(len(file_array) / 2)):
            # Getting the css class name
            name = file_array[2*k].strip(" ")
            properties = file_array[2*k+1]
            # Formatting the properties into a dictionnary
            properties = properties.split(";")
            prop_dict = {}
            # Looping through all the properties of the class
            for property_ in properties:
                if not property_.strip(" ") == "":
                    # Getting the name and values
                    property_name, property_val = property_.split(":")
                    # Setting up tags 
                    # Formatting the name and values
                    property_name = property_name.strip(" ")
                    property_val = property_val.strip(" ")
                    # Updating the class dictionary
                    if property_name[0:3] == "t__" and separate_tags:
                        tags_dict.update({property_name.strip("t__"): property_val})
                    else:
                        prop_dict.update({property_name: property_val})
            style_sheet.update({name: prop_dict})
    # Adding null value to the style sheet
    style_sheet.update({"__none__": {}})
    return style_sheet if not separate_tags else style_sheet, tags_dict


def helloworld():
    print("hello world")


if __name__ == "__main__":
    openCheatSheet()
               
