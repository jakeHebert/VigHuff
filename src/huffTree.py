from huffElement import HuffElement
from comparable import Comparable


class HuffTree(Comparable):
    """
    This class represents a Huffman Encoding Tree.
    There are two types of HuffTrees that are built
      1. the leaf nodes: built with the HuffElements
      2. the internal nodes: built with two HuffTrees
    """

    def __init__(self, element=None, left_tree=None, right_tree=None):
        """
        Constructor:
        The constructor parameters have default values.
        The constructor must be called using these keyword arguments:
        1. when building the internal nodes for the Huffman Tree, the
           element parameter is None
        2. when building the leaf nodes the left and right subtree
           root nodes will be None
        Initialize the root HuffNode instance variable appropriately
        a) for the leaf Node, root is initialized with a HuffNode
           using the element parameter
        b) for the internal Node, root is initialized with a
           HuffNode using a HuffElement where the character is EOF.
           Set the frequency correctly as described in the Project
           document.
        """
        if element is None:
            self.root = HuffNode(HuffElement(""))
            self.root.left = left_tree.root
            self.root.right = right_tree.root
            freq = left_tree.root.get_freq() + right_tree.root.get_freq()
            self.root.set_freq(freq)
        else:
            self.root = HuffNode(element)

    def get_root(self):
        """
        Returns the root of the tree
        """
        return self.root

    def compare(self, other_huff_tree):
        """
        Compare the root node of this HuffTree
        to that of the other HuffTree
        """
        if self.root.get_freq() < other_huff_tree.root.get_freq():
            return -1
        if self.root.get_freq() > other_huff_tree.root.get_freq():
            return 1
        return 0


class HuffNode(Comparable):

    def __init__(self, element):
        """
        Constructor that initializes element from passed in variable.
        Sets left and right to none.
        :param element: variable to be set to self.element.
        """
        self.element = element
        self.left = None
        self.right = None

    def get_char(self):
        """
        Returns the char held in element.
        :return: (char)element.
        """
        return self.element.get_char()

    def get_freq(self):
        """
        Returns the frequency of the char.
        """
        return self.element.get_freq()

    def get_code(self):
        """
        Returns huffman code for the element.
        """
        return self.element.get_code()

    def set_freq(self, count):
        """
        Sets the frequency of the element to count.
        """
        self.element.set_freq(count)

    def set_code(self, code):
        """
        Sets the code of the element to code.
        """
        self.element.set_code(code)

    def compare(self, other_node):
        """
        Compares two elements to each other.
        :return: -1 if element is smaller, 0 if equal, 1 is element is larger.
        """
        return self.element.compare(other_node)

    def __str__(self):
        """
        Returns a string representation of the HuffNode obj
        """
        return "{} : {}".format(self.get_char(), self.get_freq())
