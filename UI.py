from tkinter import *
from tkinter import filedialog
from chararray import CharArray
from foundwords import FoundWord
import search

def startscreen(root, frame):

    entrymessage = Label(master = frame, text="Hello and welcome to Zach and Conor's Word Search Solver! \n Press the button below to continue!", font = (16))
    entrymessage.pack()
    entrymessage.place(relx=0.5, rely=0.5, anchor="center")
    root.update()
    continue_button = Button(master = frame, text="Continue",font = (16),command = lambda : continuetopage2(root, frame))
    continue_button.pack()
    continue_button.place(relx=0.5, rely=0.6, anchor = "center")

def continuetopage2(root, frame):

    frame.destroy()
    root.update()

    secondarymessage = Label(master = root, text="Please press the button below to choose your file ", font = 16)
    secondarymessage.pack()
    secondarymessage.place(relx=0.5, rely=0.5, anchor="center")
    file_button = Button(master = root, text = "Choose File", font = 16, command = openfile)
    file_button.pack()
    file_button.place(relx=0.5, rely=0.6, anchor="center")

def openfile():

   filetoopen = filedialog.askopenfilename()
   print(filetoopen)
   wordarray = search.arrayfromfile(filetoopen)
   heightofarray = wordarray.height()
   widthofarray = wordarray.width()

   return wordarray, heightofarray, widthofarray


def printtextfiletoUI(wordarray, heightofarray, widthofarray, frame):

    a = widthofarray + 1
    b = heightofarray + 1
    c = wordarray
    #frame.destroy()
    textgrid = Canvas(master = frame, width = a * 50, height = b * 50, bg = "white")
    textgrid.pack()
    textgrid.place(relx = 0.5, rely = 0.5, anchor = "center")
    for i in range(a):
        textgrid.create_line(i*50, 0, i*50, a*50)
        textgrid.create_line(0, i*50 , a*50, i*50 )
        for j in range(a):
            textgrid.create_text(j*50 + 25, i*50 + 25, text = c[i][j], font = 16)

    continuetosolver = Button(master = frame, text = "Solve", font = 16, command = lambda : highlightsolution(wordarray,(15,8), 7, (1,0), textgrid))
    continuetosolver.place(relx = 0.5, rely = 0.95, anchor = "center")

def highlightsolution(wordarray, FoundWord, textgrid):
    startingy = ((startingletter[0]-1)*50)
    startingx = ((startingletter[1]-1)*50)
    print(startingx)
    print(startingy)
    if direction == (-1,-1):
        for a in range(length - 1):
            textgrid.create_rect(startingx - a*50, startingy - a*50, startingx + 50 - a*50, startingy + 50 - a*50, fill = "yellow")
            #textgrid.create_text(startingy*50 + 25, startingx * 50 + 25, text = wordarray[])
    if direction == (-1,0):
        for a in range(length - 1):
            textgrid.create_rectangle(startingx - a*50, startingy, startingx + 50 - a*50, startingy + 50, fill = "yellow")

    if direction == (-1,1):
        for a in range(length - 1):
            textgrid.create_rectangle(startingx - a*50, startingy + a*50, startingx + 50 - a*50, startingy + 50 + a*50, fill = "yellow")

    if direction == (0,-1):
        for a in range(length - 1):
            textgrid.create_rectangle(startingx, startingy - a*50, startingx + 50, startingy + 50 - a*50, fill = "yellow")

    if direction == (0,1):
        for a in range(length - 1):
            textgrid.create_rectangle(startingx, startingy + a*50, startingx + 50, startingy + 50 + a*50, fill = "yellow")

    if direction == (1,-1):
        for a in range(length - 1):
            textgrid.create_rectangle(startingx + a*50, startingy - a*50, startingx + 50 + a*50, startingy + 50 - a*50, fill = "yellow")

    if direction == (1,0):
        for a in range(length):
            textgrid.create_rectangle(startingx + a*50, startingy, startingx + 50 + a*50, startingy + 50, fill = "yellow")
            textgrid.create_text(startingx + 25 + a*50, startingy  + 25, text = wordarray[startingletter[0]-1][a+startingletter[1]-1], font = 16)

    if direction == (1,1):
        for a in range(length - 1):
            textgrid.create_rectangle(startingx + a*50, startingy + a*50, startingx + 50 + a*50, startingy + 50 + a*50, fill = "yellow")
