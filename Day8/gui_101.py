# Basic GUI programs


import tkinter as tk


def main():
    # creating root as object and .Tk() is class
    root = tk.Tk()
    # setting window width and height
    root.geometry("1200x800")
    # .mainloop() required to keep gui window active and running
    root.mainloop()


main()
