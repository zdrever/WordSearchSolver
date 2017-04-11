import UI
from tkinter import *
from tkinter import filedialog
# from chararray import CharArray
# from foundwords import FoundWord
# import search

#TODO: don't need any of these functions above, should probably clean up and delete some
if __name__ == "__main__":

    #initializing the root and frame
    root = Tk()
    frame = Frame(width=1500, height=950, bg="", colormap="new")
    frame.pack()

    #running the first startscreen, only one function call in the main file, just how you wanted it Zach!
    UI.startscreen(root,frame)

root.mainloop()
