from huffMap import HuffMap
from huffTree import HuffTree
from huffPQ import HuffPQ


class Huffman:
    """
    This Huffman class does the following:
      1. Compresses a passed in string of characters from a text file:
         - build the character frequency map of HuffElements
         - build the Huffman Tree using the HuffPQ of HuffTrees
         - recursively walk the Huffman tree assigning the 
           correct binary code to each leaf HuffNode which contain
           the HuffElement for the character  
         - build the Huffman encoded binary string by retrieving the
           correct code from the HuffElements for each character
           in the file string
      2. Decompresses the encoded binary string
         - each binary character (0 or 1) is retrieved from the
           binary encoded string and used to walk the Huffman tree 
         - traverse the Huffman tree starting from the root going left 
           with '0' and right with '1' until you find a leaf node
         - retrieve the file string character from the HuffElement 
           in the HuffNode and add it to the output string.
    """
    def __init__(self):
        """
        Constructor: Create the Huffman class object
        Initialize the huff_map instance variable to a HuffMap
        Initialize the huffTree instance variable to None
        """
        self.huff_map = HuffMap()
        self.huffTree = None

    def build_huff_map(self, file_str):
        """
        Populate the huffMap from the passed in file string:
         - keys: file characters
         - values: HuffElements holding character frequency counts
         
        Loop though each character in the file string
          1. If the huffMap does not contain the character, 
             add the character to the map
          2. Retrieve the HuffElement from the map and increment 
             the frequency
        """
        for i in range(len(file_str)):
            if file_str[i] in self.huff_map:
                elem = self.huff_map.get_huff_elem(file_str[i])
                elem.inc_freq()
            else:
                self.huff_map.add_char(file_str[i])

    def build_huff_tree(self):
        """
        1. Create an empty Huff Priority Queue: HuffPQ
        2. Create the set of character keys from the HuffMap
        3. Build a forest of HuffTrees one from each 
           HuffElement in the HuffMap using the character key 
           set to retrieve the HuffElements and enqueue each 
           single node HuffTree to the HuffPQ
        4. Loop through the HuffPQ min heap, dequeueing the two  
           lowest frequency count HuffTrees and combine them into 
           a new HuffTree, enqueueing the new single HuffTree back 
           to the HuffPQ and repeating until there is only one 
           HuffTree in the HuffPQ
        5. Dequeue the single HuffTree from the HuffPQ 
           and set it to the HuffTree instance variable
        """
        huff_pq = HuffPQ()      # 1
        keys = self.huff_map.get_key_set()      # 2
        for char in keys:       # 3
            tree = HuffTree(element=self.huff_map.get_huff_elem(char))
            huff_pq.enqueue(tree)
        while len(huff_pq) > 1:     # 4
            left = huff_pq.dequeue()
            right = huff_pq.dequeue()
            node = HuffTree(left_tree=left, right_tree=right)
            huff_pq.enqueue(node)
        self.huffTree = huff_pq.dequeue()       # 5

    def build_huff_codes(self, root):
        """
        This is the helper function for the recursive assign_code
        method that walks the Huffman Tree (self.huff_tree)
        building the code for each character in the file string
        starting from the root of the Huffman Tree.
        
        If the passed in root is not None, call assign_code
        """
        if root is not None:
            self.assign_code(root)

    def assign_code(self, root):
        """
        Recursively get the binary bits for the code as you
        walk the Huffman Tree to the leaf node.
        The base case is when the left subtree of the root is None
        1. Get the code from the root HuffNode and add '0' to it
           Set this new code in the HuffNode of the left subtree 
           of root, and then call assign_code passing in the
           left subtree of root
        2. Get the code from the root HuffNode and add '1' to it
           Set this new code in the HuffNode of the right subtree 
           of root, and then call assign_code passing in the
           right subtree of root 
        """
        if root.left is not None:

            root.left.set_code(root.get_code() + "0")
            self.assign_code(root.left)

            root.right.set_code(root.get_code() + "1")
            self.assign_code(root.right)

    def build_binary_str(self, file_str):
        """
        Builds a binary string of ones and zeros by walking through 
        the passed in file_str and replacing each character with the 
        code in the HuffElement which is retrieved from the HuffMap
        Return the binary string
        """
        binary_str = ""
        for letter in str(file_str):
            elem = self.huff_map.get_huff_elem(letter)
            if elem is not None:
                binary_str += elem.get_code()
        return binary_str

    def compress(self, file_str):
        """
        Compresses a passed in string of characters from a text file:
        1. take the passed in file_str and add EOF marker
        1. build the character frequency map of HuffElements
        2. build the Huffman Tree using the HuffPQ of HuffTrees
        3. build the Huffman codes, recursively traversing the tree
        4. build the Huffman encoded binary string and return it
        """
        file_str += ""
        self.build_huff_map(file_str)
        self.build_huff_tree()
        self.build_huff_codes(self.huffTree.root)
        return self.build_binary_str(file_str)

    def decompress(self, binary_str):
        """
        1. Get the root node of the Huffman tree and set a 
           current node pointing to the root node
        2. Loop through each character (0 or 1) in the binary_str:
           a. Traverse the Huffman tree starting from the root going
              left with '0' and right with '1' until you find a leaf 
              node
           b. When you find a leaf node (both left and right node
              pointers are None), retrieve the file string character 
              from the HuffNode 
           c. Check the character for the EOF char 
              and break when found
           d. Add character to decompressed string
           e. Reset the current node pointer to root
        3. Return the decompressed string
        """
        curr_node = self.huffTree.get_root()
        decompressed_str = ""
        for i in range(len(binary_str)):
            if binary_str[i] == "0":
                curr_node = curr_node.left
            elif binary_str[i] == "1":
                curr_node = curr_node.right
            if curr_node.left is None and curr_node.right is None:
                decompressed_str += curr_node.get_char()
                curr_node = self.huffTree.get_root()
        return decompressed_str
