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
            if array[i][j] == letter:
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
        letter_x_y = find_letter_indices(char, array)
        # pull the word list from the dictionary of words to find
        wordlist = dictionary[char]
        # for each word, calculate the possible starts and directions depending
        # upon the first two letters of the word
        for word in wordlist:
            # for each x,y index in letter_x_y, check if the second letter in
            # the word is in the neighbours of the instance of the first word
            for x_y, nbrs in letter_x_y:
                if word[1] not in nbrs:
                    continue
                else:
                    i = x_y
                    # Need to make sure there can be two instances of directions for
                    # the same index
                    d_indices = [i for i, x in enumerate(my_list) if x == word[0]]
                    direction = [directions[index] for index in d_indices]
                    l = len(word)
                    for d in direction:
                        f = FoundWord(i, d, l)
                    to_check += f

            # IDEA: is there an easy check to remove directions that are not
            # far enough away from the edge for the word to fit?

            while len(to_check) > 1:
                l_count = 2
                f = to_check.pop()
                # index, direction, length = foundword from to_check set
                i, d, l = f
                dx, dy = d
                x, y = i
                index = (x + dx * l_count, y + dy * l_count)
                if word[l_count] == array.direction_find(index, d):
                    to_check += f
                l_count += 1

            found += to_check

    return found

if __name__ == "__main__":
    a = CharArray()
    a.arrayfromfile("testarray.txt")
    print(a[0])

    wordlist= dictionaryfromfile("testwords.txt")
    print(words)

    for char in wordlist:
        print(find_letter_indices(char, )



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
