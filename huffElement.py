from comparable import Comparable


class HuffElement(Comparable):
    """
    This class is used in conjunction with the HuffMap class.
    The HuffMap class is a dictionary for storing the frequency 
    counts of characters found in a string, and the Huffman code 
    for that character. The key for the HuffMap is the character 
    and the value is a HuffElement object, which contains the
    character, its frequency in the string, and its Huffman code.    
    """
    def __init__(self, char):
        """
        Create a HuffElement object for the passed in character.
        Initialize the character, the frequency to zero 
        and the code to the empty string.
        """
        self._ch = char
        self._ch_freq = 0
        self._code = ""

    def inc_freq(self):
        """
        Increment the character frequency count
        """
        self._ch_freq += 1
               
    def get_freq(self):
        """
        Return the character frequency count
        """
        return self._ch_freq
        
    def set_freq(self, count):
        """
        Set the character frequency count
        """
        self._ch_freq = count

    def get_code(self):
        """
        Return the Huffman code for the character
        """
        return self._code

    def set_code(self, code):
        """
        Set the Huffman code for the character
        """
        self._code = code

    def get_char(self):
        """
        Return the char.
        :return: _ch
        """
        return self._ch
    
    def compare(self, other_huff_elem):
        """
        Use the character frequency count for comparison
        """
        if other_huff_elem.get_freq() < self.get_freq():
            return 1
        elif other_huff_elem.get_freq() > self.get_freq():
            return -1
        else:
            return 0
        
    def __str__(self):
        """
        Returns a string representation of this HuffElement
        """
        return str(self._ch) + ":" + str(self._ch_freq)
