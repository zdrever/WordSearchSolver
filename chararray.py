class CharArray:
    '''Type to represent word search array of characers.

    Attributes:
        __array: 2D array (list of lists)
        __height: max index of rows
        __width: max index of columns
    '''

    def __init__(self):
        self.__array = list()

    def __getitem__(self, index):
        return self.__array[index]

    def height(self):
        '''Returns the maximum index of the rows'''
        return len(self.__array)-1

    def width(self):
        '''Returns the maximum index of the columns'''
        return len(self.__array[0])-1

    def readfile(self, filename):
        '''Initializes a CharArray from a text file representation of
        a word search array.

        Args:
            filename: string of the filename that neeads to be read

        Raises:
            RuntimeError: if the strings of character in the file to be
            read aren't all the same character. Most likely cause is the OCR
            didn't work on the photo of the array

        @TODO: Make the RuntimeError. For now assume proper .txt file
        format
        '''
        with open(filename) as f:
            rows = f.readlines()
            for line in rows:
                self.__array.append(list(line.strip()))

    def neighbours(self, p):
        '''Finds the neighbours of the character in position p.

        Args:
            p: position tuple (row, column) defining a position
            of a character in __array

        Returns:
            list: all characters that immediately surround the character in
            position p. Ordering is left to right, top to bottom
        '''
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        x, y = p
        print("x,y",x,y)
        # Corner Cases
        # Top Left
        if x == 0 and y == 0:
            return [self.__array[x][y+1],\
            self.__array[x+1][y],\
            self.__array[x+1][y+1]]
        # Top Right
        elif x == 0 and y == self.width():
            return [self.__array[x][y-1],\
            self.__array[x+1][y-1],\
            self.__array[x+1][y]]
        # Bottom Left
        elif x == self.height() and y == 0:
            return [self.__array[x-1][y],\
            self.__array[x-1][y+1],\
            self.__array[x][y+1]]
        # Bottom Right
        elif x == self.height() and y == len(self.__array[0])-1:
            return [self.__array[x-1][y-1],\
            self.__array[x-1][y],\
            self.__array[x][y-1]]

        # Edge Cases
        # Top
        elif x == 0:
            delta = [(dx, dy) for (dx, dy) in directions if dx != -1]
        # Bottom
        elif x == self.height():
            delta = [(dx, dy) for (dx, dy) in directions if dx != 1]
        # Left
        elif y == 0:
            delta = [(dx, dy) for (dx, dy) in directions if dy != -1]
        # Right
        elif y == self.width():
            delta = [(dx, dy) for (dx, dy) in directions if dy != 1]

        # General Case
        else:
            delta = [(dx,dy) for (dx, dy) in directions]

        # Return Values
        ret = list()
        for (dx, dy) in delta:
            ret.append(self.__array[x+dx][y+dy])
        return ret
