class FoundWord:
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

    def setindex(self, i):
        '''
        Args:
            i: integer tuple (row, column of the starting index
        Returns:
            Nothing
        '''
        self.index = i

    def setdirection(self, d):
        '''
        Args:
            d: a direction unit vector tuple (row, column) that describes the
            direction that the word runs in the CharArray.
        Returns:
            Nothing
        '''
        self.direction = d

    def setlength(self, l):
        '''
        Args:
            l: The length of the string that defines the word.
        Retuns:
            Nothing
        '''
        self.length = l
