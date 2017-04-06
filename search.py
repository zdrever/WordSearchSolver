from chararray import CharArray
from foundwords import FoundWord
import re

wordlist = dict()

directions = {0: (-1,-1),
              1: (-1,0),
              2: (-1,1),
              3: (0,-1),
              4: (0,1),
              5: (1,-1),
              6: (1,0),
              7: (1,1)}


def check_array(C):
    total = 0
    for i in range(C.height()):
        total += len(C[i])
    if total/len(C[0]) != C.height():
        print("PROBLEM IN ARRAY")


def arrayfromfile(filename):
    '''Initializes a CharArray from a text file representation of
    a word search array.

    Args:
        filename: string of the filename that needs to be read

    Returns:
        CharArray type built from a txt file
    Raises:
        RuntimeError: if the strings of character in the file to be
        read aren't all the same length. Most likely cause is the OCR
        didn't work on the photo of the array

    @TODO: Implement Error handling. Is it possible to handle size of row
    errors in the UI?
    '''
    C = CharArray()
    problems = list()
    with open(filename) as f:
        rows = [line.upper().strip() for line in f.readlines()]
        i = 0
        j = 0
        for line in rows:
            C.append(list())
            for char in line:
                if char.isalpha():
                    C[i].extend(char)
                else:
                    problems += (i,j)
                j += 1
            i += 1
            j = 0

    return C, problems


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
                row_list = line.strip(',').upper().split()
            else:
                row_list = line.strip().upper().split()
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
    for x in range(array.height()):
        for y in range(array.width()):
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
    # print(dictionary)
    for char in dictionary:
        wordlist = dictionary[char]
        # find letter index --> neighbour relation for all instances of a character once
        position_to_neighbours = indexToNeighbours(char, array)
        # for each word, calculate the possible starts and directions depending
        # upon the first two letters of the word
        # print(wordlist)
        for word in wordlist:
            queue = list()
            # for each x,y index in position_to_neighbours, check if the second letter in
            # the word is in the neighbours of the instance of the first word
            for pos, nbrs in position_to_neighbours.items():
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
                f = queue.pop(0)
                # index, direction, length = foundword from queue set
                next_letter = array.direction_find(f.index, f.direction, letter)
                if not next_letter:
                    if added_back == len(queue):
                        added_back = 0
                        letter += 1
                    continue
                if word[letter] == next_letter:
                    queue.append(f)
                    added_back += 1
                if added_back == len(queue):
                    added_back = 0
                    letter += 1
            if not queue:
                print("WORD NOT IN ARRAY- SHIT!")
            else:
                f = queue.pop()
                found.add(f)

            # @TODO: Handle Fucked up word searches
    return found

if __name__ == "__main__":
    C, problems = arrayfromfile("TestCases/wordsearch2.txt")
    # print(C[0])
    print(problems)
    for i in range(C.height()):
        print(C[i])

    wordlist = dictionaryfromfile("TestCases/wordsearch2words.txt")
    # print(wordlist)

    # for char in wordlist:
    #     print(indexToNeighbours(char, C))

    found = find_words(wordlist, C)
    # print(found)

    # for f in found:
    #     print("index {}, direction {}, length {}".format(f.index, f.direction, f.length))


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
