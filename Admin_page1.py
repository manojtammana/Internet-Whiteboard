from tkinter import *

def doNothing():
    print("Manoj")

def admin_page():


    root = Tk()
    root.title('INTERNET WHITEBOARD ADMIN')
    root.geometry('800x500')

    menu = Menu(root)
    root.configure(background='orange')
    root.config(menu=menu)

    subMenu = Menu(menu)
    menu.add_cascade(label="Internet WhiteBoard", menu=subMenu)
    subMenu.add_command(label="Profile", command=doNothing)
    subMenu.add_command(label="Signout", command=doNothing)
    subMenu.add_separator()
    subMenu.add_command(label="Settings", command=doNothing)

    clickMenu = Menu(menu)
    menu.add_cascade(label="Help", menu=clickMenu)
    clickMenu.add_command(label="About Us", command=doNothing)
    frame = Frame(root)
    frame.pack()
    printButton = Button(frame, text="Create Employee", command=printMessage)
    printButton.pack(side=LEFT)

    printButton = Button(frame, text="Create User", command=printMessage)
    printButton.pack(side=LEFT)


    printButton = Button(frame, text="Configure IP", command=printMessage)
    printButton.pack(side=LEFT)


    printButton = Button(frame, text="Settings", command=printMessage)
    printButton.pack(side=LEFT)


    root.mainloop()

def printMessage(self):
        print("Session started by Manoj")

admin_page()




