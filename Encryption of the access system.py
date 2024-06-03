def encrypt_message(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char
    return encrypted_message

def main():
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value for encryption: "))
    encrypted_message = encrypt_message(message, shift)
    print("Encrypted Message:", encrypted_message)

if __name__ == "__main__":
    main()
