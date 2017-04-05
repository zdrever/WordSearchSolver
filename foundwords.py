class FoundWords:
    '''A class to represent found words in a word search

    Attributes:
        __word: the list that contains the three sub attributes
        index: The index of the starting letter in the array
        direction: the direction the word runs in the array
        length: the length of the word
    '''

    def __init__(self, i = None, d = None, l = None):
        self.index = i
        self.direction = d
        self.length = l
        self.__word = list(index, direction, length)

    def setindex(self, i):
         self.index = i

    def setdirection(self, d):
        self.direction = d

    def setlength(self, l):
        self.length = l
