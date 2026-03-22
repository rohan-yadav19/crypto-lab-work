# Caesar Cipher Encryption and Decryption Program
# CNS LAB

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char

    return result


def decrypt(cipher, shift):
    return encrypt(cipher, -shift)


def caesar_cipher():
    print("Caesar Cipher Program")
    print("1. Encrypt")
    print("2. Decrypt")

    choice = int(input("Choose an option: "))

    if choice == 1:
        text = input("Enter the text to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted = encrypt(text, shift)
        print("Encrypted Text:", encrypted)

    elif choice == 2:
        cipher = input("Enter the text to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted = decrypt(cipher, shift)
        print("Decrypted Text:", decrypted)

    else:
        print("Invalid choice!")


# Program starts here
caesar_cipher()
