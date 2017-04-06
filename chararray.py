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
        neighbours:
            takes a position tuple and returns all the
            characters in the immediate vicinity of
            the position
    '''

    def __init__(self):
        self.__array = list()

    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    def __getitem__(self, index):
        return self.__array[index]

    def append(self, i):
        return self.__array.append(i)

    def height(self):
        '''Returns the height of the array'''
        return len(self.__array)

    def width(self):
        '''Returns the width of the array'''
        return len(self.__array[0])

    def neighbours(self, p):
        '''Finds the neighbours of the character in position p.

        Args:
            p: position tuple (row, column) defining a position
            of a character in __array

        Returns:
            list: all characters that immediately surround the character in
            position p. Ordering is left to right, top to bottom. Positions that
            are set to None are not on the array.
        '''
        directions = self.directions
        x, y = p

        ret = list()
        for (dx, dy) in directions:
            if x + dx < 0 or x + dx > self.height()-1:
                ret.append(None)
            elif y + dy < 0 or y + dy > self.width()-1:
                ret.append(None)
            else:
                ret.append(self.__array[x+dx][y+dy])

        return ret

    def direction_find(self, index, direction, leaps = 1):
        '''Given an index and a direction, return the next letter in that
        direction.

        Args:
            index: the index of a letter
            direction: an x,y unit direction tuple

        Returns:
            False: if the next character in that direction would be off the
            edge of the array
            Next Character: if the next character is on the array.
        '''
        x,y = index
        dx,dy = direction
        dx = dx * leaps
        dy = dy * leaps
        if x + dx < 0 or x + dx > self.height()-1:
            return False
        if y + dy < 0 or y + dy > self.width()-1:
            return False
        return self.__array[x+dx][y+dy]
