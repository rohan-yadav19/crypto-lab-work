# Data Encryption Standard (DES) Encryption and Decryption Program
# CNS LAB

from Crypto.Cipher import DES
from secrets import token_bytes


# Padding to ensure block size compatibility (8 bytes)
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text


def des_algorithm():

    def encrypt(text, key):
        cipher = DES.new(key, DES.MODE_ECB)
        padded_text = pad(text)
        encrypted_text = cipher.encrypt(padded_text.encode('utf-8'))
        return encrypted_text


    def decrypt(cipher_text, key):
        cipher = DES.new(key, DES.MODE_ECB)
        decrypted_text = cipher.decrypt(cipher_text).decode('utf-8').rstrip()
        return decrypted_text


    print("DES Algorithm Program")
    print("1. Encrypt")
    print("2. Decrypt")

    choice = int(input("Choose an option: "))

    if choice == 1:
        text = input("Enter the text to encrypt: ")

        key = token_bytes(8)  # 8-byte key for DES
        print("Generated Key (Save this for decryption):", key.hex())

        encrypted = encrypt(text, key)
        print("Encrypted Text (hex):", encrypted.hex())


    elif choice == 2:
        cipher_text = bytes.fromhex(input("Enter the encrypted text (in hex): "))
        key = bytes.fromhex(input("Enter the key (in hex): "))

        decrypted = decrypt(cipher_text, key)
        print("Decrypted Text:", decrypted)


    else:
        print("Invalid choice!")


# Run program
des_algorithm()