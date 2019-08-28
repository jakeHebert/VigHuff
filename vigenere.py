"""
Background to Using the Vigenere Square for Encryption

The rows are associated with the characters in the key and the columns
are associated with the characters in the message to encrypt.  The key
will be used over and over again matching the letters in the message
with the letters in the key.

Encryption: Find the ciphertext character in the Vigenere square
matrix by the following steps:
a) Using the character from the key, find the row where it exists by
   looking down column 0 until you find the correct row.
b) Using the character from the plaintext message, find column where
   it exists by looking across row 0 until you find the correct column.
c) The ciphertext character will be the one in the in the matrix
   having the row and column found above.
d) Add the ciphertext letter to the coded message.

Decryption: Find the plaintext character in the Vigenere square
matrix by the following steps:
a) Find the ciphertext letter in the Vigenere square, using the key
   letter row.
b) In that same column, get the character at row 0, this is the
   plaintext letter.
c) Add the plaintext letter to the decoded message.
"""


class Vigenere:

    def __init__(self, key):
        """
        Create Vigenere object: key and matrix
        """
        self._key = key
        self._vig_squ = self.create_vig_square()

    def create_vig_square(self):
        """
        Create the vigenere square, using 128 rows and 128 columns
        Use a nested list for the matrix and a nested loop to create 
           each inner row and add it to the outer matrix.
        Each element of the inner row is one more in ASCII code value 
           than the previous element.  After getting to 128, you must
           go back to 0.
        """
        vig_square = []
        
        for row in range(128):
            char_num = row
            vig_row = []
            for col in range(128):
                char = chr(char_num) 
                vig_row.append(char)
                char_num = char_num + 1 
                if char_num == 128:
                    char_num = 0
            vig_square.append(vig_row)  
              
        return vig_square

    def encrypt(self, msg):
        """
        Traverse the message getting each letter 
           and finding its encoding:
        Get the row index of the key char using get_row_index
        Get the column index of the message char using get_col_index
        Use the row and column indices to find the code character
           in the Vigenere square
        Add code character to encoded message    
        """
        coded_msg = ""
        key_index = 0
            
        for ch in msg:
            row = self.get_row_index(self._key[key_index])
            col = self.get_col_index(ch)
            coded_msg = coded_msg + self._vig_squ[row][col]
            key_index = (key_index + 1) % len(self._key)
        
        return coded_msg

    def decrypt(self, coded_msg):
        """
        Traverse the code getting each letter 
           and finding its decoding:
        Get the message character using get_plain_text_char 
        Add message character to decoded message   
        """
        decoded_msg = ""
        key_index = 0 
        for ch in coded_msg:
            msg_char = self.get_plain_text_char(ch, self._key[key_index])
            decoded_msg = decoded_msg + msg_char
            key_index = (key_index + 1) % len(self._key) 
        return decoded_msg

    def get_col_index(self, char):
        """
        The first row of the Vigenere square is vig_squ[0].
        This is used to match chars from the message to encrypt.
        Return the column index in row 0 containing the char
        """
        
        col_index = self._vig_squ[0].index(char)
        return col_index 

    def get_row_index(self, key_char):
        """
        The first column of the Vigenere square is vig_squ[][0]
        This is used to match chars from the key.
        Return the row index in col 0 containing the key char
        """
        for row in range(128):
            if self._vig_squ[row][0] == key_char:
                row_index = row
        return row_index

    def get_plain_text_char(self, coded_char, key_char):
        """
        Use the row index of the key char and the column index of
        the coded message char in that row to locate the column in
        row 0 of the plaintext char and return that element value.
        """
        row_index = self.get_row_index(key_char)
        col_index = self._vig_squ[row_index].index(coded_char)
        plain_text_char = self._vig_squ[0][col_index]
        return plain_text_char
