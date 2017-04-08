from tkinter import *
from tkinter import filedialog
from chararray import CharArray
from foundwords import FoundWord
import search

def startscreen(root, frame):

    #prints entry message
    entrymessage = Label(master = frame, text="Hello and welcome to Zach and Conor's Word Search Solver! \n Press the button below to continue!", font = (16))
    entrymessage.pack()
    entrymessage.place(relx=0.5, rely=0.5, anchor="center")
    root.update()

    #prints continue button, if clicked will go to continuetopage2()
    continue_button = Button(master = frame, text="Continue",font = (16),command = lambda : continuetopage2(root, frame))
    continue_button.pack()
    continue_button.place(relx=0.5, rely=0.6, anchor = "center")

def continuetopage2(root, frame):

    #erasing writing from before
    frame.destroy()
    root.update()
    frame = Frame(width=1500, height=950, bg="", colormap="new")
    frame.pack()

    #TODO: Add button to open image editing application if photo is not already in correct format

    #displays prompt to choose file
    secondarymessage = Label(master = frame, text="Please press the button below to choose your file ", font = 16)
    secondarymessage.pack()
    secondarymessage.place(relx=0.5, rely=0.5, anchor="center")

    #once 'choose file' button is pressed, go to openfile()
    file_button = Button(master = frame, text = "Choose File", font = 16, command = lambda : openfile(frame))
    file_button.pack()
    file_button.place(relx=0.5, rely=0.6, anchor="center")

def openfile(frame):


    #user picks the 2 files to use, first is array, second is word bank TODO: instruct the user to pick in correct order
    filetoopen1 = filedialog.askopenfilename()
    filetoopen2 = filedialog.askopenfilename()

    #checking if arrary file is .txt, runs functions directly if so
    if filetoopen1[-3:] == 'txt':
        wordarray = search.arrayfromfile(filetoopen1)
        heightofarray = wordarray.height()
        widthofarray = wordarray.width()

    #checking if arrary file is .jpg, .jpeg or .png  ##TODO run image reader then find wordarrary, height, width
    if (filetoopen1[-3:] == 'jpg' or 'png') or (filetoopen1[-4:] == 'jpeg'):
        print("hi")

    #checking if wordbank file is .txt, TODO move search.dictfromfile() instructions from printtextfiletoUI() to this function
    if filetoopen2[-3:] == 'txt':
        print("hi")
    #checking if wordbank file is .txt, TODO run image reader then create foundwords here
    if (filetoopen2[-3:] == 'jpg' or 'png') or (filetoopen2[-4:] == 'jpeg'):
        # TODO run image reader
        print("hi")

    #checking if both files have been selected, once both files have been selected move to (printtextfiletoUI)
    a = 0
    if filetoopen2 != '':
        a = 1
    if a == 1:
        frame.destroy()
        frame = Frame(width=1500, height=950, bg="", colormap="new")
        frame.pack()
        printtextfiletoUI(wordarray, heightofarray, widthofarray, frame, filetoopen2)


def printtextfiletoUI(wordarray, heightofarray, widthofarray, frame, filetoopen2):

    #using letters for variables for ease of calculations -- TODO dont need c variable only type it once
    a = widthofarray
    b = heightofarray
    c = wordarray

    #creating grid upon which letters are placed
    textgrid = Canvas(master = frame, width = a * 50, height = b * 50, bg = "white")
    textgrid.pack()
    textgrid.place(relx = 0.5, rely = 0.5, anchor = "center")

    #creating the black lines of the grid
    for i in range(a):
        textgrid.create_line(i*50, 0, i*50, a*50)
        textgrid.create_line(0, i*50 , a*50, i*50 )
        for j in range(a):
            textgrid.create_text(j*50 + 25, i*50 + 25, text = c[i][j], font = 16)

    #TODO move all this to openfile()
    dicttofind = search.dictionaryfromfile(filetoopen2)
    foundwords = FoundWord()
    foundwords = search.find_words(dicttofind, c)

    #creating "solve" button, once hit continue to highlightsolution()
    continuetosolver = Button(master = frame, text = "Solve", font = 16, command = lambda : highlightsolution(wordarray,foundwords, textgrid))
    continuetosolver.place(relx = 0.5, rely = 0.95, anchor = "center")


def highlightsolution(wordarray, FoundWord, textgrid):

    #defining some variables for later calculation use
    for f in FoundWord:
        row, column = f.index
        dx, dy = f.direction
        length = f.length
        startingx = (column*50)
        startingy = (row*50)


    # messy code ahead - sorry! TODO: maybe try clean up by grouping some directions together? Could probably
    #work out a way to use dx, dy as multiples so I could group all the horizontal/verticals together, anything going backwards
    #was giving me problems through


    #Highlighting the solution with a red line through the letters
        if (dx, dy) == (-1,-1):
            for a in range(length):
                #creates the line
                textgrid.create_line(startingx +25, startingy +25, startingx - (length-1)*50 +25, startingy - (length-1)*50 + 25, fill = "red", width = 2)
                if a!= length:
                    #redraws the letters - looks bad if I don't do this
                    textgrid.create_text(startingx + 25 - a*50, startingy + 25 - a*50, text = wordarray[row-a][column-a], font=16)

        if (dx, dy) == (-1,0):
            for a in range(length):
                textgrid.create_line(startingx + 25, startingy +40 , startingx + 25 , startingy - 50*a +10 , fill = "red", width = "2")
                if a!= length:
                    textgrid.create_text(startingx + 25 , startingy - a*50 +25, text = wordarray[row-a][column], font = 16)

        if (dx, dy) == (-1,1):
            for a in range(length):
                textgrid.create_line(startingx + 25, startingy + 25, startingx + length*50 - 25, startingy - (length - 1)*50 + 25, fill = "red", width = "2")
                if a != length:
                    textgrid.create_text(startingx + 25 + a*50, startingy + 25 - a*50, text = wordarray[row - a][column + a], font = 16)

        if (dx, dy) == (0,-1):
            for a in range(length):
                textgrid.create_line(startingx + 40 , startingy + 25, startingx - 50*a +10, startingy +25 , fill = "red", width = "2")
                if a!= length:
                    textgrid.create_text(startingx + 25 - a*50 , startingy + 25, text = wordarray[row][column-a], font = 16)

        if (dx, dy) == (0,1):
            for a in range(length):
                textgrid.create_line(startingx + 10, startingy+25, startingx+50*length - 10, startingy +25 , fill = "red", width = "2")
                if a!= length:
                    textgrid.create_text(startingx + 25+ a*50 , startingy  + 25, text = wordarray[row][column+a], font = 16)

        if (dx, dy) == (1,-1):
            for a in range(length):
                textgrid.create_line(startingx + 25, startingy +25, startingx - (length-1)*50 + 25, startingy  + length*50 - 25, fill = "red", width = "2")
                if a != length:
                    textgrid.create_text(startingx + 25 -a*50, startingy +25 + a*50, text = wordarray[row + a][column - a], font = 16)

        if (dx, dy) == (1,0):
            for a in range(length):
                textgrid.create_line(startingx + 25, startingy + 10, startingx + 25, startingy + length*50 - 10 , fill = "red", width = "2")
                if a!= length:
                    textgrid.create_text(startingx + 25 , startingy + a*50 + 25, text = wordarray[row+a][column], font = 16)

        if (dx, dy) == (1,1):
            for a in range(length):
                textgrid.create_line(startingx + 25, startingy +25, startingx + length*50 - 25, startingy + length*50 - 25, fill = "red"
                , width = "2")
                if a!= length:
                    textgrid.create_text(startingx + 25 + a*50, startingy +25 + a*50, text=wordarray[row+a][column+a], font = 16)
