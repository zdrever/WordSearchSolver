from tkinter import *
from tkinter import filedialog
from chararray import CharArray
from foundwords import FoundWord
import search
import ocrAPI


def resetprogram(root, frame):
    ''' Restarts the program. Goes to start screen immediately.

    Args:
        root: window which contains all other widgets
        frame: adjustable widget that other widgets can be placed on

    '''

    #clears frame and recreates a blank one
    frame.destroy()
    frame = Frame(width=1500, height=950, bg="", colormap="new")
    frame.pack()

    #starts the program over
    startscreen(root,frame)

def startscreen(root, frame):
    ''' Start screen shown at beginning of program. Contains Continue button
        which allows you to progress through the program.

    Args:
        root: window which contains all other widgets
        frame: adjustable widget that other widgets can be placed on

    '''

    #prints entry message
    entrymessage = Label(master = frame, text="Hello and welcome to Zach and\
 Conor's Word Search Solver! \n Press the button below to continue!", font = (16))
    entrymessage.pack()
    entrymessage.place(relx=0.5, rely=0.5, anchor="center")
    root.update()

    #prints continue button, if clicked will go to choosefilescreen()
    continue_button = Button(master = frame, text="Continue",font = (16),\
    command = lambda : choosefilescreen(root, frame))
    continue_button.pack()
    continue_button.place(relx=0.5, rely=0.6, anchor = "center")

def choosefilescreen(root, frame):
    '''Screen where you choose your file. Contains Choose File button.

    Args:
        root: window which contains all other widgets
        frame: adjustable widget that other widgets can be placed on

    '''

    #erasing writing from before
    frame.destroy()
    root.update()
    frame = Frame(width=1500, height=950, bg="", colormap="new")
    frame.pack()

    #displays prompt to choose file
    secondarymessage = Label(master = frame, text="Please press the button\
 below to choose your file. Choose the word array file first, and the word\
 bank file second. ", font = 16)
    secondarymessage.pack()
    secondarymessage.place(relx=0.5, rely=0.5, anchor="center")

    #once 'choose file' button is pressed, go to openfile()
    file_button = Button(master = frame, text = "Choose File", font = 16, \
    command = lambda : openfile(root,frame))
    file_button.pack()
    file_button.place(relx=0.5, rely=0.6, anchor="center")

def openfile(root,frame):
    ''' Opens window where user chooses file. Once files are chosen, continue
        to printing out the array and wordbank.

    Args:
        root: window which contains all other widgets
        frame: adjustable widget that other widgets can be placed on

    '''

    #Declaring which file types are allowed
    allowedfiletypes = [
    ('Allowed File Types', '*.txt ; *.png ; *.jpeg ; *.jpg'), ('All File Types', '*')
    ]

    #user picks the 2 files to use, first is array, second is word bank
    #we use while loops to ensure the user has picked a file. If cancel is hit,
    #the program will ask for the file again
    wordarrayfile = ''
    while wordarrayfile == '':
        wordarrayfile = filedialog.askopenfilename(title = "Choose your array file", \
        filetypes = allowedfiletypes)

    wordbankfile = ''
    while wordbankfile == '':
        wordbankfile = filedialog.askopenfilename(title = "Choose your word bank file")

    #checking if arrary file is .txt, runs functions directly if so
    if wordarrayfile[-3:] == 'txt':
        print("Getting array from .txt file.")
        wordarray = search.arrayfromfile(wordarrayfile)
        heightofarray = wordarray.height()
        widthofarray = wordarray.width()

    #checking if arrary file is .jpg, .jpeg or .png
    elif (wordarrayfile[-3:] == 'jpg' or 'png') or (wordarrayfile[-4:] == 'jpeg'):
        print("Getting array from image file.")
        print(wordarrayfile)
        # write to the file array.txt the response from the API server
        ocrAPI.text_array_from_image(wordarrayfile)
        wordarray = search.arrayfromfile('array.txt')
        heightofarray = wordarray.height()
        widthofarray = wordarray.width()

    #checking if wordbank file is .txt
    if wordbankfile[-3:] == 'txt':
        print("Getting word list from .txt file.")
        dicttofind, wordcount = search.dictionaryfromfile(wordbankfile)
        foundwords = search.find_words(dicttofind, wordarray)

    #checking if wordbank file is .jpg, jpeg or png
    elif (wordbankfile[-3:] == 'jpg' or 'png') or (wordbankfile[-4:] == 'jpeg'):
        print("Getting word list from image file.")
        print(wordbankfile)
        # write to the file words.txt the response from the API server
        ocrAPI.text_wordlist_from_image(wordbankfile)
        dicttofind, wordcount = search.dictionaryfromfile('words.txt')
        foundwords = search.find_words(dicttofind, wordarray)

    #checking if both files have been selected, once both files have been
    #selected move to (printtextfiletoUI)
    a = 0
    if wordbankfile != '':
        a = 1
    if a == 1:
        frame.destroy()
        frame = Frame(width=1500, height=950, bg="", colormap="new")
        frame.pack()
        printtextfiletoUI(wordarray, heightofarray, widthofarray, root, frame, \
        foundwords, dicttofind, wordcount)


def printtextfiletoUI(wordarray, heightofarray, widthofarray, root, frame, \
                        foundwords, dicttofind, wordcount):
    ''' Prints the array file and word bank file to tkinter. Creates solve button
        that can be pressed to solve the wordsearch.

    Args:
        wordarrary: instance of the CharArray class. It is an array created from
                    a textfile.
        heightofarray: The height of the word array
        widthofarray: The width of the word array
        root: window which contains all other widgets
        frame: adjustable widget that other widgets can be placed on
        foundwords: list of words found in the word array - only passed to be
                    passed through to highlightsolution()
        dicttofind: list of words to find, word bank created from this list
        wordcount: number of words to find. Used to create dimensions of word bank

    '''
    #using letters for variables for ease of calculations
    a = widthofarray
    b = heightofarray
    c = wordcount

    #creating a list so I can iterate through it while printing the word bank
    wordstoprint = list()
    for char in dicttofind:
        for word in dicttofind[char]:
            wordstoprint.append(word)
    wordstoprint = sorted(wordstoprint)

    #finding the max word length for use in calculations
    d = max(len(w) for w in wordstoprint)

    #square array - nearly all wordsearches are square
    if a == b:
        #creating grid upon which letters are placed
        textgrid = Canvas(master = frame, width = a * 40, height = a * 40, bg = "white")
        textgrid.pack()
        textgrid.place(relx = 0.4, rely = 0.5, anchor = "center")
        #creating the black lines of the grid
        for i in range(a):
            #vertical lines
            textgrid.create_line(i*40, 0, i*40, a*40)
            #horizontal lines
            textgrid.create_line(0, i*40 , a*40, i*40 )
            for j in range(a):
                textgrid.create_text(j*40 + 20, i*40 + 20, text = wordarray[i][j], font = 16)

    # width < height
    if a < b:
        textgrid = Canvas(master = frame, width = a * 40, height = b * 40, bg = "white")
        textgrid.pack()
        textgrid.place(relx = 0.4, rely = 0.5, anchor = "center")
        #creating the black lines of the grid
        for i in range(b):
            textgrid.create_line(i*40, 0, i*40, b*40)
            textgrid.create_line(0, i*40 , a*40, i*40 )
            for j in range(a):
                textgrid.create_text(j*40 + 20, i*40 + 20, text = wordarray[i][j], font = 16)

    #width > height
    if a > b:
        textgrid = Canvas(master = frame, width = a * 40, height = b * 40, bg = "white")
        textgrid.pack()
        textgrid.place(relx = 0.4, rely = 0.5, anchor = "center")
        #creating the black lines of the grid
        for i in range(a):
            textgrid.create_line(i*40, 0, i*40, b*40)
            textgrid.create_line(0, i*40 , a*40, i*40 )
            for j in range(b):
                textgrid.create_text(i*40 + 20, j*40 + 20, text = wordarray[j][i], font = 16)

    #creating a wordbank the user can see, if less than 35 words we make one single list
    if c < 35:

        #making the background for the wordbank
        wordbank = Canvas(master = frame, width = d*14 + 20, height = c*25 + 20 , bg = "white")
        wordbank.pack()
        wordbank.place(relx = 0.9, rely = 0.5, anchor = "e")

        #printing the words for the wordbank
        for i in range(c):
            wordbank.create_text(5, i*25 + 20, text = wordstoprint[i], font = 16, anchor = "w")

    #creating a wordwordbank the user can see, if greater than 35, we split the list into two
    else:
        #making the background
        wordbank = Canvas(master = frame, width = 2*d*14 + 10, height = c*13, bg = "white")
        wordbank.pack()
        wordbank.place(relx = 0.9, rely = 0.5, anchor = "e")

        #printing the words
        for i in range(int(c/2)):
            wordbank.create_text(10, i*25 + 20, text = wordstoprint[i], font = 16, anchor = "w")
        for i in range(int((c/2)),c):
            wordbank.create_text(15+d*14, i*25 + 20 -int(c/2)*25, text = wordstoprint[i], font = 16, anchor = "w")


    #creating "solve" button, once hit continue to highlightsolution()
    continuetosolver = Button(master = frame, text = "Solve", font = 16, \
    command = lambda : highlightsolution(wordarray,foundwords, textgrid,root, frame))
    continuetosolver.place(relx = 0.5, rely = 0.95, anchor = "center")


def highlightsolution(wordarray, FoundWord, textgrid,root, frame):
    ''' Highlights the solution on the word array.

    Args:
        wordarrary: instance of the CharArray class. It is an array created from a textfile.
        FoundWord: list of words found in the word array - Instance of the class FoundWord
        textgrid: Array of letters put onto a grid which displays the letters
        root: window which contains all other widgets
        frame: adjustable widget that other widgets can be placed on

    '''

    #Reset button - just writes on top of solve button
    resetbutton = Button(master = frame, text = "Restart Program", font = 18)
    resetbutton.place(relx = 0.5, rely = 0.95, anchor = "center")
    resetbutton['command'] = lambda: resetprogram(root, frame)


    #defining some variables for later calculation use
    for f in FoundWord:
        row, column = f.index
        dx, dy = f.direction
        length = f.length
        startingx = (column*40)
        startingy = (row*40)

    #Highlighting the solution with a yellow line through the letters

        #diagonal - up and to the left
        if (dx, dy) == (-1,-1):
            for a in range(length):
                #creates the line
                textgrid.create_line(startingx + 25, startingy + 25, startingx - (length-1)*40 + 15,\
                startingy - (length-1)*40 + 15, fill = "yellow", width = 4)
            for a in range(length):
                #redraws the letters - I have to do two for loops or else it doesn't redraw properly
                textgrid.create_text(startingx + 20 - a*40, startingy + 20 - a*40, \
                text = wordarray[row-a][column-a], font=16)

        #vertical - sraight up
        if (dx, dy) == (-1,0):
            for a in range(length):
                textgrid.create_line(startingx + 20, startingy + 32 , startingx + 20 ,\
                startingy - 40*a + 8 , fill = "yellow", width = 4)
            for a in range(length):
                textgrid.create_text(startingx + 20 , startingy - a*40 + 20, \
                text = wordarray[row-a][column], font = 16)

        #diagonal - up and to the right
        if (dx, dy) == (-1,1):
            for a in range(length):
                textgrid.create_line(startingx + 15, startingy + 25, startingx + length*40 - 15, \
                startingy - (length - 1)*40 + 15, fill = "yellow", width = 4)
            for a in range(length):
                textgrid.create_text(startingx + 20 + a*40, startingy + 20 - a*40, \
                text = wordarray[row - a][column + a], font = 16)

        #horizontal - to the left
        if (dx, dy) == (0,-1):
            for a in range(length):
                textgrid.create_line(startingx + 32 , startingy + 20, startingx - 40*a + 8,\
                startingy + 20, fill = "yellow", width = 4)
            for a in range(length):
                textgrid.create_text(startingx + 20 - a*40 , startingy + 20,\
                text = wordarray[row][column-a], font = 16)

        #horizontal - to the right
        if (dx, dy) == (0,1):
            for a in range(length):
                textgrid.create_line(startingx + 8, startingy + 20, startingx + 40*length - 8, \
                startingy + 20 , fill = "yellow", width = 4)
            for a in range(length):
                textgrid.create_text(startingx + 20 + a*40 , startingy  + 20,\
                text = wordarray[row][column+a], font = 16)

        #diagonal - down and to the left
        if (dx, dy) == (1,-1):
            for a in range(length):
                textgrid.create_line(startingx + 25, startingy + 15, startingx - (length-1)*40 + 15, \
                startingy  + length*40 - 15, fill = "yellow", width = 4)
            for a in range(length):
                textgrid.create_text(startingx + 20 -a*40, startingy + 20 + a*40,\
                 text = wordarray[row + a][column - a], font = 16)

        #vertical - straight down
        if (dx, dy) == (1,0):
            for a in range(length):
                textgrid.create_line(startingx + 20, startingy + 8, startingx + 20,\
                startingy + length*40 - 8 , fill = "yellow", width = 4)
            for a in range(length):
                textgrid.create_text(startingx + 20 , startingy + a*40 + 20,\
                text = wordarray[row+a][column], font = 16)

        #diagonal - down and to the right
        if (dx, dy) == (1,1):
            for a in range(length):
                textgrid.create_line(startingx + 15, startingy + 15, startingx + length*40 - 15, \
                startingy + length*40 - 15, fill = "yellow", width = 4)
            for a in range(length):
                textgrid.create_text(startingx + 20 + a*40, startingy + 20 + a*40, \
                text=wordarray[row+a][column+a], font = 16)
