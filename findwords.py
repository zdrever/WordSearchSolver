from chararray import CharArray
from foundwords import FoundWord

wordlist = dict()

directions = {0: (-1,-1),
              1: (-1,0),
              2: (-1,1),
              3: (0,-1),
              4: (0,1),
              5: (1,-1),
              6: (1,0),
              7: (1,1)}

def dictionaryfromfile(filename):
    '''Fill the word list with words read from a text file

    Args:
        filename: string of the filename that needs to be read

    Returns:
        dict that maps a letter of words to a list of words that
        start with that letter
    '''
    wordlist = dict()
    with open(filename) as f:
        rows = f.readlines()
        for line in rows:
            row_list = list()
            if "," in line:
                row_list = line.strip().split(",")
            else:
                row_list = line.strip().split()
            for token in row_list:
                if token[0] not in wordlist:
                    wordlist[token[0]] = list()
                    wordlist[token[0]].append(token)
                else:
                    wordlist[token[0]].append(token)

    return wordlist


def indexToNeighbours(letter, array):
    '''Given a letter, find all indices of that letter in the CharArray
    using a binary search

    Args:
        letter: a character
        array: the 2d CharArray to search

    Return:
        dictionary mapping an the index of a instance of a letter to a list
        of all neighbours of that index.
    '''
    ret = dict()
    print(array.height())
    print(array.width())
    for x in range(array.height()):
        for y in range(array.width()):
            print(x,y)
            if array[x][y] == letter:
                ret[(x,y)] = array.neighbours((x,y))
    return ret

def find_words(dictionary, array):
    '''Given the dictionary of words to find, go through the dictionary and
    and find all words.

    Args:
        words: dict that maps the start letter of words to all words that start
        with that letter
        array: the 2D CharArray

    Returns:
        A set of FoundWords.
    '''
    found = set()
    for char in dictionary:
        # find letter index --> neighbour relation for all instances of a character once
        position_to_neighbours = indexToNeighbours(char, array)
        print("position_to_neighbours", position_to_neighbours)
        # pull the word list from the dictionary of words to find
        wordlist = dictionary[char]
        # for each word, calculate the possible starts and directions depending
        # upon the first two letters of the word
        print(wordlist)
        for word in wordlist:
            queue = list()
            print("word:", word)
            # for each x,y index in position_to_neighbours, check if the second letter in
            # the word is in the neighbours of the instance of the first word
            for pos, nbrs in position_to_neighbours.items():
                print("index {}, nbrs {}, word[1] {}".format(pos, nbrs, word[1]))
                if word[1] not in nbrs:
                    continue
                else:
                    i = pos
                    # Need to make sure there can be two instances of directions for
                    # the same index
                    d_indices = [i for i, x in enumerate(nbrs) if x == word[1]]
                    direction = [directions[index] for index in d_indices]
                    l = len(word)
                    for d in direction:
                        queue.append(FoundWord(i, d, l))

            # IDEA: is there an easy check to remove directions that are not
            # far enough away from the edge for the word to fit?
            letter = 2
            added_back = 0
            while len(queue) > 1:
                print("letter index", letter)
                f = queue.pop(0)
                print("f.index", f.index)
                # index, direction, length = foundword from queue set
                print("direction", f.direction)
                next_letter = array.direction_find(f.index, f.direction, letter)
                if not next_letter:
                    print("GET OUTTA HERE")
                    if added_back == len(queue):
                        added_back = 0
                        letter += 1
                    continue
                if word[letter] == next_letter:
                    queue.append(f)
                    added_back += 1
                print("len(queue)",len(queue))
                print("added_back", added_back)
                if added_back == len(queue):
                    added_back = 0
                    letter += 1
            f = queue.pop()
            found.add(f)

            # @TODO: Handle Fucked up word searches
    return found

if __name__ == "__main__":
    a = CharArray()
    a.arrayfromfile("testarray.txt")
    print(a[0])

    wordlist= dictionaryfromfile("testwords.txt")
    print(wordlist)

    for char in wordlist:
        print(indexToNeighbours(char, a))

    found = find_words(wordlist, a)
    print(found)
    for f in found:
        print(f.index)


    # print("X max", a.height())
    # print("Y max",len(a[0]))
    # print("TOP LEFT")
    # print(a.neighbours((0,0)))
    # print("TOP RIGHT")
    # print(a.neighbours((0,14)))
    # print("BOTTOM LEFT")
    # print(a.neighbours((14,0)))
    # print("BOTTOM RIGHT")
    # print(a.neighbours((14,14)))
