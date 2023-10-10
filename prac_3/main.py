import os

from features.steps.encoder import Encoder

def main():
    os.chdir(os.path.dirname(__file__))
    encoder = Encoder()
    mode = None
    while not mode:
        try:
            mode = int(input("Choose interaction mode:\n1 - manual string input\n2 - encrypt file.txt content\nYour choice: "))
            if mode != 1 and mode != 2:
                mode = None
                print("Mode should be '1' or '2' integer!")
                continue
            if mode == 2:
                try:
                    with open('file.txt', 'r') as file:
                        tmp = file.read()
                    tmp = None
                except Exception as e:
                    print(e)
                    print("There is no file 'file.txt', try again!")
                    mode = None
                    continue
            break
        except:
            print("Mode should be '1' or '2' integer!")

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
    8) Decrypt string using Vernam cypher
    0) Exit the application\nYour choice: """))
        except:
            print("Input a number in range [1-8] to select an option or type 'exit' to close program")
            continue
        
        match cmd:
            case 1 | 2:
                if mode == 2:
                    with open('file.txt', 'r') as file:
                        string = file.read()
                else:
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
                else:
                    result = encoder.caesar_decrypt(string, offset)
                
                if mode == 1:
                    print(f"{('Decrypted', 'Encrypted')[cmd == 1]} string:\n", result, sep="")
                else:
                    with open('file.txt', 'w') as file:
                        file.write(result)
                    print(f"File content was updated!")

            case 0:
                return
            case _:
                print("Incorrect option!")

if __name__ == '__main__':
    main()