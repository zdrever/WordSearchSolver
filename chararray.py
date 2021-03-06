class CharArray:
    '''Type to represent word search array of characers.

    Attributes:
        array:
            2D array (list of lists)

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
        self.array = list()

    # list of directions. Index corresponds to the direction that
    # the tuple points to. See neighbours function for its use.
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    def __getitem__(self, index):
        '''Enables Indexing'''
        return self.array[index]

    def append(self, v):
        '''Allows for the CharArry to be appended to using the self.append method'''
        return self.array.append(v)

    def height(self):
        '''Returns the height of the array'''
        return len(self.array)

    def width(self):
        '''Returns the width of the array'''
        return len(self.array[0])

    def neighbours(self, p):
        '''Finds the neighbours of the character in position p.

        Args:
            p: position tuple (row, column) defining a position
            of a character in array

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
                ret.append(self.array[x+dx][y+dy])

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
        return self.array[x+dx][y+dy]
