from tkinter import *

def doNothing():
    print("Manoj")
def user_page():


    root = Tk()

    root.title('INTERNET WHITEBOARD USER')
    root.geometry('800x500')
    root.configure(background='orange')


    menu = Menu(root)
    root.config(menu=menu)

    subMenu = Menu(menu)
    menu.add_cascade(label="Internet WhiteBoard", menu=subMenu)
    subMenu.add_command(label="Profile", command=doNothing)
    subMenu.add_command(label="Signout", command=doNothing)
    subMenu.add_separator()
    
    clickMenu = Menu(menu)
    menu.add_cascade(label="Help", menu=clickMenu)
    clickMenu.add_command(label="About Us", command=doNothing)
    frame = Frame(root)
    frame.pack()

    printButton = Button(frame, text="JOIN SESSION", command=printMessage)
    printButton.pack(side=LEFT)
    root.mainloop()    


        
def printMessage():
        print("Session started by Manoj")

user_page()




