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
