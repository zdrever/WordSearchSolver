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
    secondarymessage = Label(master = frame, text="Please press the button below to choose your file. Choose the word array file first, and the word bank file second. ", font = 16)
    secondarymessage.pack()
    secondarymessage.place(relx=0.5, rely=0.5, anchor="center")

    #once 'choose file' button is pressed, go to openfile()
    file_button = Button(master = frame, text = "Choose File", font = 16, command = lambda : openfile(frame))
    file_button.pack()
    file_button.place(relx=0.5, rely=0.6, anchor="center")

def openfile(frame):


    #user picks the 2 files to use, first is array, second is word bank
    wordarrayfile = filedialog.askopenfilename()
    wordbankfile = filedialog.askopenfilename()

    #checking if arrary file is .txt, runs functions directly if so
    if wordarrayfile[-3:] == 'txt':
        print("hi0")
        wordarray = search.arrayfromfile(wordarrayfile)
        heightofarray = wordarray.height()
        widthofarray = wordarray.width()

    #checking if arrary file is .jpg, .jpeg or .png  ##TODO run image reader then find wordarrary, height, width
    elif (wordarrayfile[-3:] == 'jpg' or 'png') or (wordarrayfile[-4:] == 'jpeg'):
        print("hi1")

    #checking if wordbank file is .txt
    if wordbankfile[-3:] == 'txt':
        print("hi2")
        dicttofind,wordcount = search.dictionaryfromfile(wordbankfile)
        foundwords = search.find_words(dicttofind, wordarray)

    #checking if wordbank file is .jpg, jpeg or png, TODO run image reader then create foundwords here
    elif (wordbankfile[-3:] == 'jpg' or 'png') or (wordbankfile[-4:] == 'jpeg'):
        # TODO run image reader
        print("hi3")

    #checking if both files have been selected, once both files have been selected move to (printtextfiletoUI)
    a = 0
    if wordbankfile != '':
        a = 1
    if a == 1:
        frame.destroy()
        frame = Frame(width=1500, height=950, bg="", colormap="new")
        frame.pack()
        printtextfiletoUI(wordarray, heightofarray, widthofarray, frame, foundwords, dicttofind, wordcount)


def printtextfiletoUI(wordarray, heightofarray, widthofarray, frame, foundwords, dicttofind, wordcount):

    #using letters for variables for ease of calculations
    a = widthofarray
    b = heightofarray
    c = wordcount

    wordstoprint = set()
    for z in dicttofind:
        dicttofind[z] = wordstoprint
    #creating grid upon which letters are placed
    textgrid = Canvas(master = frame, width = a * 40, height = b * 40, bg = "white")
    textgrid.pack()
    textgrid.place(relx = 0.4, rely = 0.5, anchor = "center")

    #creating the black lines of the grid
    for i in range(a):
        textgrid.create_line(i*40, 0, i*40, a*40)
        textgrid.create_line(0, i*40 , a*40, i*40 )
        for j in range(a):
            textgrid.create_text(j*40 + 20, i*40 + 20, text = wordarray[i][j], font = 16)

    wordbank = Canvas(master = frame, width = 500, height = 800, bg = "white")
    wordbank.pack()
    wordbank.place(relx = 0.8, rely = 0.5, anchor = "center")
    if c < 20:
        for k in range(c):
            wordbank.create_text(250, c*40 + 20, text = wordstoprint[k], font = 16)

    #creating "solve" button, once hit continue to highlightsolution()
    continuetosolver = Button(master = frame, text = "Solve", font = 16, command = lambda : highlightsolution(wordarray,foundwords, textgrid))
    continuetosolver.place(relx = 0.5, rely = 0.95, anchor = "center")


def highlightsolution(wordarray, FoundWord, textgrid):

    #defining some variables for later calculation use
    for f in FoundWord:
        row, column = f.index
        dx, dy = f.direction
        length = f.length
        startingx = (column*40)
        startingy = (row*40)


    # messy code ahead - sorry! TODO: maybe try clean up by grouping some directions together? Could probably
    #work out a way to use dx, dy as multiples so I could group all the horizontal/verticals together, anything going backwards
    #was giving me problems through


    #Highlighting the solution with a yellow line through the letters

        #diagonal - up and to the left
        if (dx, dy) == (-1,-1):
            for a in range(length):
                #creates the line
                textgrid.create_line(startingx + 25, startingy + 25, startingx - (length-1)*40 + 15, startingy - (length-1)*40 + 15, fill = "yellow", width = 4)
            for a in range(length):
                #yellowraws the letters - I have to do two for loops or else it doesn't yellowraw properly
                textgrid.create_text(startingx + 20 - a*40, startingy + 20 - a*40, text = wordarray[row-a][column-a], font=16)

        #vertical - sraight up
        if (dx, dy) == (-1,0):
            for a in range(length):
                textgrid.create_line(startingx + 20, startingy + 32 , startingx + 20 , startingy - 40*a + 8 , fill = "yellow", width = 4)
            for a in range(length):
                textgrid.create_text(startingx + 20 , startingy - a*40 + 20, text = wordarray[row-a][column], font = 16)

        #diagonal - up and to the right
        if (dx, dy) == (-1,1):
            for a in range(length):
                textgrid.create_line(startingx + 15, startingy + 25, startingx + length*40 - 25, startingy - (length - 1)*40 + 25, fill = "yellow", width = 4)
            for a in range(length):
                textgrid.create_text(startingx + 20 + a*40, startingy + 20 - a*40, text = wordarray[row - a][column + a], font = 16)

        #horizontal - to the left
        if (dx, dy) == (0,-1):
            for a in range(length):
                textgrid.create_line(startingx + 32 , startingy + 20, startingx - 40*a + 8, startingy + 20, fill = "yellow", width = 4)
            for a in range(length):
                textgrid.create_text(startingx + 20 - a*40 , startingy + 20, text = wordarray[row][column-a], font = 16)

        #horizontal - to the right
        if (dx, dy) == (0,1):
            for a in range(length):
                textgrid.create_line(startingx + 8, startingy + 20, startingx + 40*length - 8, startingy + 20 , fill = "yellow", width = 4)
            for a in range(length):
                textgrid.create_text(startingx + 20 + a*40 , startingy  + 20, text = wordarray[row][column+a], font = 16)

        #diagonal - down and to the left
        if (dx, dy) == (1,-1):
            for a in range(length):
                textgrid.create_line(startingx + 25, startingy + 15, startingx - (length-1)*40 + 15, startingy  + length*40 - 15, fill = "yellow", width = 4)
            for a in range(length):
                textgrid.create_text(startingx + 20 -a*40, startingy + 20 + a*40, text = wordarray[row + a][column - a], font = 16)

        #vertical - straight down
        if (dx, dy) == (1,0):
            for a in range(length):
                textgrid.create_line(startingx + 20, startingy + 8, startingx + 20, startingy + length*40 - 8 , fill = "yellow", width = 4)
            for a in range(length):
                textgrid.create_text(startingx + 20 , startingy + a*40 + 20, text = wordarray[row+a][column], font = 16)

        #diagonal - down and to the right
        if (dx, dy) == (1,1):
            for a in range(length):
                textgrid.create_line(startingx + 15, startingy + 15, startingx + length*40 - 15, startingy + length*40 - 15, fill = "yellow", width = 4)
            for a in range(length):
                textgrid.create_text(startingx + 20 + a*40, startingy + 20 + a*40, text=wordarray[row+a][column+a], font = 16)
