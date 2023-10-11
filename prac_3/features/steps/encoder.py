import numpy as np

class Encoder:
    def caesar_encrypt(self, text: str, offset: int) -> str:
        try:
            offset = int(offset)
        except:
            raise TypeError('Text must be a string and offset must be an integer')
        if offset < 1:
            raise ValueError('Offset must be in range [1, 32]')

        text = str(text)
        result = ""
        alphabet_ru_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        alphabet_ru_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        alphabet_en = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

        for symbol in text:
            if symbol in alphabet_ru_upper:
                result += alphabet_ru_upper[alphabet_ru_upper.find(symbol) + offset]

            elif symbol in alphabet_ru_lower:
                result += alphabet_ru_lower[alphabet_ru_lower.find(symbol) + offset]

            elif symbol in alphabet_en:
                if (symbol.isupper()):
                    result += chr((ord(symbol) + offset - 65) % 26 + 65)
                else:
                    result += chr((ord(symbol) + offset - 97) % 26 + 97)
            else:
                result += symbol
        return result
    
    def caesar_decrypt(self, text: str, offset: int) -> str:
        try:
            offset = int(offset)
        except:
            raise TypeError('Text must be a string and offset must be an integer')
        if offset < 1:
            raise ValueError('Offset must be in range [1, 32]')
        
        text = str(text)
        result = ""
        alphabet_ru_upper = "ЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЁЕДГВБАЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЁЕДГВБА"
        alphabet_ru_lower = "яюэьыъщшчцхфутсрпонмлкйизжёедгвбаяюэьыъщшчцхфутсрпонмлкйизжёедгвба" 
        alphabet_en = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

        for symbol in text:
            if symbol in alphabet_ru_upper:
                result+=alphabet_ru_upper[alphabet_ru_upper.find(symbol) + offset]

            elif symbol in alphabet_ru_lower:
                result+=alphabet_ru_lower[alphabet_ru_lower.find(symbol) + offset]

            elif symbol in alphabet_en:
                if(symbol.isupper()): 
                    result += chr((ord(symbol) - offset - 65) % 26 + 65) 
                else: 
                    result += chr((ord(symbol) - offset - 97) % 26 + 97)
            else:
                result += symbol    
        return result


    def vernam_encrypt(self, word, key):
        word = str(word)
        key = str(key)

        if len(word) != len(key):
            raise ValueError('The text must be the same lenght as key')
        
        coded = ''

        for i in range(len(word)):
            sym1 = ord(word[i])
            sym2 = ord(key[i])

            coded += str(sym1^sym2)
            if i != len(word)-1:
                coded += ' '

        return coded

    def vernam_decrypt(self, coded, key):
        coded = str(coded)
        key = str(key)

        while coded.count('  ')>0:
            coded = coded.replace('  ', ' ')
        coded = coded.split(' ')
        
        if len(coded) != len(key):
            raise ValueError('The text must be the same lenght as key')
      
        word = ''

        for i in range(len(coded)):
            try:
                sym1 = int(coded[i])
            except:
                raise ValueError('The text must be numbers separated by a space')
            sym2 = ord(key[i])

            word += chr(sym1^sym2)

        return word

    def playfair_encrypt(self, uncyph_str, keyword):
        if not keyword.isalpha():
            raise TypeError("Text and keyword must be a string")
        
        matrix = initialize_matrix(keyword)

        uncyph_str = uncyph_str.replace(" ", "")
        uncyph_str = uncyph_str.replace("J", "I")
        uncyph_str = uncyph_str.upper()
        uncyph_str = ''.join(c for c in uncyph_str if c.isalpha())

        pos = 1
        while pos < len(uncyph_str):
            if uncyph_str[pos-1] == uncyph_str[pos]:
                uncyph_str = uncyph_str[:pos] + 'X' + uncyph_str[pos:]
            pos += 2
        if len(uncyph_str) % 2 == 1:
            uncyph_str += 'X'

        matrix = np.array(matrix)
        pos = 1
        str_len = len(uncyph_str)
        while pos < str_len:
            a = np.where(matrix == uncyph_str[pos-1])
            a_line, a_column = a[0][0], a[1][0]
            b = np.where(matrix == uncyph_str[pos])
            b_line, b_column = b[0][0], b[1][0]

            if a_line == b_line:
                uncyph_str = swap_from_line(matrix, a_line, a_column, uncyph_str, pos-1)
                uncyph_str = swap_from_line(matrix, b_line, b_column, uncyph_str, pos)
            elif a_column == b_column:
                uncyph_str = swap_from_column(matrix, a_line, a_column, uncyph_str, pos-1)
                uncyph_str = swap_from_column(matrix, b_line, b_column, uncyph_str, pos)
            else:
                uncyph_str = uncyph_str[:pos-1] + matrix[a_line][b_column] + uncyph_str[pos:]
                uncyph_str = uncyph_str[:pos] + matrix[b_line][a_column] + uncyph_str[pos+1:]
            pos += 2
        return uncyph_str
    
    def playfair_decrypt(self, cyph_str, keyword):
        if not keyword.isalpha():
            raise TypeError("Text and keyword must be a string")
        
        matrix = initialize_matrix(keyword)

        cyph_str = cyph_str.replace(" ", "")
        cyph_str = cyph_str.replace("J", "I")
        cyph_str = cyph_str.upper()

        pos = 1
        while pos < len(cyph_str):
            if cyph_str[pos-1] == cyph_str[pos]:
                cyph_str = cyph_str[:pos] + 'X' + cyph_str[pos:]
            pos += 2
        if len(cyph_str) % 2 == 1:
            cyph_str += 'X'

        matrix = np.array(matrix)
        pos = 1
        str_len = len(cyph_str)
        while pos < str_len:
            a = np.where(matrix == cyph_str[pos-1])
            a_line, a_column = a[0][0], a[1][0]
            b = np.where(matrix == cyph_str[pos])
            b_line, b_column = b[0][0], b[1][0]

            if a_line == b_line:
                cyph_str = swap_from_line_reverse(matrix, a_line, a_column, cyph_str, pos-1)
                cyph_str = swap_from_line_reverse(matrix, b_line, b_column, cyph_str, pos)
            elif a_column == b_column:
                cyph_str = swap_from_column_reverse(matrix, a_line, a_column, cyph_str, pos-1)
                cyph_str = swap_from_column_reverse(matrix, b_line, b_column, cyph_str, pos)
            else:
                cyph_str = cyph_str[:pos-1] + matrix[a_line][b_column] + cyph_str[pos:]
                cyph_str = cyph_str[:pos] + matrix[b_line][a_column] + cyph_str[pos+1:]
            pos += 2
        return cyph_str
    
    def vijn_encrypt(self, plain_text, key):
        if len(key)  == 0:
                raise ValueError('Len of key should be more than 0')
        encrypted_text = ""
        key_length = len(key)
        for i in range(len(plain_text)):
            char = plain_text[i]
            if char.isalpha():
                is_upper = char.isupper()
                char = char.upper()
                key_char = key[i % key_length].upper()
                key_code = ord(key_char) - ord('A')
                if 'A' <= char <= 'Z':
                    char_code = ord(char) - ord('A')
                    encrypted_char_code = (char_code + key_code) % 26
                    encrypted_char = chr(encrypted_char_code + ord('A'))
                elif 'А' <= char <= 'Я':
                    char_code = ord(char) - ord('А')
                    encrypted_char_code = (char_code + key_code) % 32
                    encrypted_char = chr(encrypted_char_code + ord('А'))
                if not is_upper:
                    encrypted_char = encrypted_char.lower()
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        return encrypted_text    

def initialize_matrix(keyword):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', \
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    matrix = [[[], [], [], [], []], \
            [[], [], [], [], []], \
            [[], [], [], [], []], \
            [[], [], [], [], []], \
            [[], [], [], [], []]]
    pos = 0
    keyword = keyword.upper()
    for i in range (5):
        for j in range(5):
            if pos < len(keyword):
                letter_pos = alphabet.index(keyword[pos])
                keyword = keyword.replace(keyword[pos], '')
                matrix[i][j] = alphabet.pop(letter_pos)
            else:
                matrix[i][j] = alphabet.pop(0)
            pos += 1
    return matrix

def swap_from_line(matrix, line_num, column_num, str, str_pos):
    new_char_pos = column_num + 1
    if new_char_pos > 4:
        new_char_pos = 0
    return str[:str_pos] + matrix[line_num][new_char_pos] + str[str_pos+1:]

def swap_from_column(matrix, line_num, column_num, str, str_pos):
    new_char_pos = line_num + 1
    if new_char_pos > 4:
        new_char_pos = 0
    return str[:str_pos] + matrix[new_char_pos][column_num] + str[str_pos+1:]

def swap_from_line_reverse(matrix, line_num, column_num, str, str_pos):
    new_char_pos = column_num - 1
    if new_char_pos < 0:
        new_char_pos = 4
    return str[:str_pos] + matrix[line_num][new_char_pos] + str[str_pos+1:]

def swap_from_column_reverse(matrix, line_num, column_num, str, str_pos):
    new_char_pos = line_num - 1
    if new_char_pos < 0:
        new_char_pos = 4
    return str[:str_pos] + matrix[new_char_pos][column_num] + str[str_pos+1:]
