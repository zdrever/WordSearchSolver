from basictree import BasicTree
class PrefixTree(BasicTree):
    '''PrefixTree class (specialized for wordsearching)

    Every node has a character value, nodes down the
    tree represent the value of the path above them.

    PrefixTree(v): initializes an empty tree ie. it is a leaf

    The Tope Node has value == None

    This class is meant to be initilized and then filled
    by reading from a text file for the purposes of this
    project
    '''


    def __init__(self, value=None, children=None):

        # The parent (super) class needs to be initialized.  It will
        # check the children for consistency
        super().__init__(children)

        # Initialize initial node value == None
        self.__value = value

    def get_value(self):
        return self.__value

    def set_value(self, v):
        self.__value = v

    # def get_letter(self, letter, tree):
    #     children = self.get_children()
    #     if letter in children:
    #         return children.index(letter)
    #     else:
    #         return False

    def add_word(self, token):
        children = self.get_children()
        node = self.__value
        print("node", node)
        for child in children:
            print("child", child.get_value())
        for char in token:
            print("char", char)
            if char in [child.get_value() for child in children]:
                print("char in children")


                node = children[i]
                children = node.get_children()
            else:
                temp = PrefixTree(char)
                print("temp value", temp.get_value())
                children.append(temp)
                node = temp.get_value()
                children = temp.get_children()

            # print(self.get_shape())




        # children = self.get_children()
        # for char in token:
        #     print(char)
        #     if char not in children:
        #         temp = PrefixTree(char)
        #         temp.set_value(char)
        #         children.append(temp)
        #         children = temp.get_children()
        #     else:
        #         for i in len(children) - 1:
        #             if char == children.get_value():
        #                 children = children[i].get_children()
        #     print(children)

    def treefromfile(self, filename):
        with open(filename) as f:
            rows = f.readlines()
            for line in rows:
                for token in line.strip().split():
                    print(token)
                    self.add_word(token)
