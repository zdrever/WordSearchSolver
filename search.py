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


def arrayfromfile(filename):
    '''Initializes a CharArray from a text file representation of
    a word search array.

    Args:
        filename: string of the filename that neeads to be read

    Raises:
        RuntimeError: if the strings of character in the file to be
        read aren't all the same length. Most likely cause is the OCR
        didn't work on the photo of the array

    @TODO: Implement Error handling. Is it possible to handle size of row
    errors in the UI?
    '''
    print("Building array in memory from text file")
    C = CharArray()

    with open(filename) as f:
        rows = f.readlines()
        for line in rows:
            if '0' in line:
                line = line.replace('0', 'O')
            if ' ' in line:
                line = line.replace(' ', '')
            if '!' in line:
                line = line.replace('!', 'I')
            if '1' in line:
                line = line.replace('1', 'I')
            if '2' in line:
                line = line.replace('2', 'Z')
            C.append(list(line.strip().upper()))
    return C


def dictionaryfromfile(filename):
    '''Fill the word list with words read from a text file

    Args:
        filename: string of the filename that needs to be read

    Returns:
        wordlist: dict that maps a letter of words to a list of words that
        start with that letter
        count: the number of words that are in the dictionary
    '''
    print("Building word dictionary from file in memory")
    wordlist = dict()
    count = 0
    with open(filename) as f:
        rows = f.readlines()
        for line in rows:
            row_list = list()
            if ',' in line:
                row_list = [line.strip() for line in line.split(',')]
            else:
                row_list = line.strip().split()
            for token in row_list:
                token = token.upper()
                if token[0] not in wordlist:
                    wordlist[token[0]] = list()
                    wordlist[token[0]].append(token)
                else:
                    wordlist[token[0]].append(token)
                count += 1
    return wordlist, count


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

def word_bfs(word, queue, array):
    '''Uses a (variation of) *breadth first search* to find a word in the
    CharArray.

    Args:
        word: the word as a string
        queue: the ordered list of potential found words to be considered
        array: the CharArray that is to be searched for the word

    Returns:
        found: a single FoundWord instance. If the word is not found the
        the FoundWord instance will be the all zeros.

    '''
    found = FoundWord()
    letter = 2
    # Keep track of how many we've added back so we know when to start
    # looking at the next letter
    added_back = 0
    while len(queue) > 1:
        f = queue.pop(0)
        # index, direction, length = foundword from queue set
        next_letter = array.direction_find(f.index, f.direction, letter)
        # Edge of the array case
        if not next_letter:
            # Check if we need to start looking at the next letter
            if added_back == len(queue):
                added_back = 0
                letter += 1
            continue
        if letter == len(word):
            print(len(queue))
            break
        # If we've reached the end of the length of the word
        if word[letter] == next_letter:
            queue.append(f)
            added_back += 1
        # Check if we need to start looking at the next letter

        if added_back == len(queue):
            added_back = 0
            letter += 1


    # Check the rest of the word
    if len(queue) == 1:
        flag = True
        f = queue.pop()
        for i in range(letter, f.length-1):
            next_letter = array.direction_find(f.index, f.direction, letter)
            if word[i] != next_letter:
                flag = False
                print("Letter Not Found. Letter {} in word not found. {} in array found instead"
                .format(word[i], next_letter))
                break
            letter +=  1

        if flag == True:
            print("Found!", word)
            found = f

    if found.length == 0:
        print("Word not found:", word)

    return found


def assemble_queue(word, position_to_neighbours, array):
    '''Given a word, assemble the queue of possibly found words.

    Args:
        word: the word that we are searching for

    Returns:
        queue: a list of possible found words
    '''
    queue = list()
    # for each x,y index in position_to_neighbours, check if the second letter in
    # the word is in the neighbours of the instance of the first word
    for pos, nbrs in position_to_neighbours.items():
        if word[1] not in nbrs:
            continue
        else:
            i = pos
            # Need to make sure there can be two instances of directions for
            # the same instance of a letter in the array
            d_indices = [i for i, x in enumerate(nbrs) if x == word[1]]
            direction = [directions[index] for index in d_indices]
            l = len(word)
            # Append all the possible found words to the queue
            for d in direction:
                queue.append(FoundWord(i, d, l))
    return queue

def find_words(dictionary, array):
    '''Given the dictionary of words to find, go through the dictionary and
    and find all words.

    The idea behind this algorithm is to search the array of characters in a
    better way than just brute force O(mn). There are three steps:

        1. For every group of words that starts with the same first letter,
        find all instances of the first letter in the array and return a
        dictionary that maps the indices of these instances and the
        neighbours of all these instances.

            This dict is assembled in indexToNeighbours()

        2. Build a queue of found words using the dictionary that was assembled
        above. We can easily and quickly check the neighbours of indices for
        and instance of the second letter in the word. If the second letter
        is in the neighbours of the starting index, we put the starting index,
        the direction the second letter runs in proximity to the first, and the
        length of the word to be found into the queue. This is now a possible
        found word.

            This step is done in assemble_queue()

        3. Pop the first element off the front of that queue. Given that we have
        the first index and the direction that the word will run, we can find
        the third letter in that direction from the starting index. If it
        matches the third letter of the word, add it to the back of the queue.
        Keep going for all letters until the queue has one element or less
        remaining. The last element is the found word. Store this found word in
        the set 'found' that is returned at the end.

            This bfs is done in word_bfs()

    Args:
        words: dict that maps the start letter of words to all words that start
        with that letter
        array: the 2D CharArray

    Returns:
        A set of FoundWords.
    '''
    print("Find Words")
    found = set()
    for char in dictionary:
        # Take the list of words that start with the character 'char'
        wordlist = dictionary[char]
        # find letter index --> neighbour relation for all instances of a character once
        position_to_neighbours = indexToNeighbours(char, array)
        # for each word, calculate the possible starts and directions depending
        # upon the first two letters of the word
        for word in wordlist:
            queue = assemble_queue(word, position_to_neighbours, array)

            # IDEA: is there an easy check to remove directions that are not
            # far enough away from the edge for the word to fit?
            # letter = 2 since we already checked the first two letters

            found.add(word_bfs(word, queue, array))

    return found

if __name__ == "__main__":
    C = arrayfromfile("TestCases/wordsearch5.txt")

    wordlist= dictionaryfromfile("TestCases/wordsearch5words.txt")
    # print(wordlist)

    # for char in wordlist:
        # print(indexToNeighbours(char, C))

    found = find_words(wordlist, C)
    # print(found)

    for f in found:
        print(f.index, f.direction, f.length)
