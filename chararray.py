class CharArray:
    '''Type to represent word search array of characers.

    Attributes:
        __array:
            2D array (list of lists)
        __height:
            max index of rows
        __width:
            max index of columns

    Methods:
        height:
            returns the maximum index of the rows
        width:
            returns the maxmimus index of the columns
        readfile:
            takes a text representation of the array
            and fills the already initialized CharArray
        neighbours:
            takes a position tuple and returns all the
            characters in the immediate vicinity of
            the position
    '''

    def __init__(self):
        self.__array = list()

    def __getitem__(self, index):
        return self.__array[index]

    def height(self):
        '''Returns the height of the array'''
        return len(self.__array)

    def width(self):
        '''Returns the width of the array'''
        return len(self.__array[0])

    def arrayfromfile(self, filename):
        '''Initializes a CharArray from a text file representation of
        a word search array.

        Args:
            filename: string of the filename that neeads to be read

        Raises:
            RuntimeError: if the strings of character in the file to be
            read aren't all the same length. Most likely cause is the OCR
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
        elif x == 0 and y == self.width()-1:
            return [self.__array[x][y-1],\
            self.__array[x+1][y-1],\
            self.__array[x+1][y]]
        # Bottom Left
        elif x == self.height()-1 and y == 0:
            return [self.__array[x-1][y],\
            self.__array[x-1][y+1],\
            self.__array[x][y+1]]
        # Bottom Right
        elif x == self.height()-1 and y == self.width()-1:
            return [self.__array[x-1][y-1],\
            self.__array[x-1][y],\
            self.__array[x][y-1]]

        # Edge Cases
        # Top
        elif x == 0:
            delta = [(dx, dy) for (dx, dy) in directions if dx != -1]
        # Bottom
        elif x == self.height()-1:
            delta = [(dx, dy) for (dx, dy) in directions if dx != 1]
        # Lefts
        elif y == 0:
            delta = [(dx, dy) for (dx, dy) in directions if dy != -1]
        # Right
        elif y == self.width()-1:
            delta = [(dx, dy) for (dx, dy) in directions if dy != 1]

        # General Case
        else:
            delta = [(dx,dy) for (dx, dy) in directions]

        # Return Values
        ret = list()
        for (dx, dy) in delta:
            ret.append(self.__array[x+dx][y+dy])
        return ret

        def direction_find(index, direction):
            '''Given an index and a direction, return the next letter in that
            direction.

            Args:
                index: the index of a letter
                direction: an x,y unit direction tuple

            Returns:
                The next character in that direction
            '''
            x,y = index
            dx,dy = direction
            return self.__array[x+dx][y+dy]
