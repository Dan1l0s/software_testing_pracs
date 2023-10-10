from features.steps.encoder import Encoder

def main():
    encoder = Encoder()
    while True:
        try:
            cmd = int(input("""Select the option you need (1-8):
    1) Encrypt string using Caesar cypher
    2) Decrypt string using Caesar cypher
    3) Encrypt string using Playfair cypher
    4) Decrypt string using Playfair cypher
    5) Encrypt string using Vigenere cypher
    6) Decrypt string using Vigenere cypher
    7) Encrypt string using Vernam cypher
    8) Decrypt string using Vernam cypher\n"""))
        except:
            print("Input a number in range [1-8] to select an option or type 'exit' to close program")
            continue
        
        match cmd:
            case 1 | 2:
                string = ""
                while len(string) == 0:
                    string = input(f"Type a string to {('encrypt', 'decrypt')[cmd == 2]}:\n")
                while True:
                    try:
                        offset = int(input("Type the offset of the cypher: "))
                        break
                    except:
                        print("Offset must be an integer in the range [1-25]!")
                if cmd == 1:
                    result = encoder.caesar_encrypt(string, offset)
                    print(f"Encrypted string:\n", result, sep="")
                else:
                    result = encoder.caesar_decrypt(string, offset)
                    print(f"Decrypted string:\n", result, sep="")
            
            case _:
                print("Incorrect option!")

if __name__ == '__main__':
    main()