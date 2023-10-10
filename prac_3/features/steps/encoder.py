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