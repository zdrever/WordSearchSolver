from chararray import CharArray
from prefixtree import PrefixTree

wordlist = dict()

directions = {0: (-1,-1),\
              1: (-1,0),\
              2: (-1,1),\
              3: (0,-1),\
              4: (0,1),\
              5: (1,-1),\
              6: (1,0),\
              7: (1,1)}

def dictionaryfromfile(filename):
    '''Fill the word list with words read from a text file

    Args:
        filename: string of the filename that needs to be read
    '''
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

def find_letter_indices(letter, array):
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
    for x in range(array.height()-1):
        for y in range(array.width()-1):
            if array[i][j] = letter:
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

    for letter in dictionary:
        letter_i = find_letter_indices(letter, array)
        wordlist = dictionary[letter]
        for word in wordlist:
            







if __name__ == "__main__":
    a = CharArray()
    a.arrayfromfile("wordsearch1.txt")

    dictionaryfromfile("wordsearch1words.txt")




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
