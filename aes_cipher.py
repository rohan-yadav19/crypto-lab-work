# Advanced Encryption Standard (AES) Encryption and Decryption Program
# CNS LAB

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from secrets import token_bytes


def aes_algorithm():

    def encrypt(text, key):
        cipher = AES.new(key, AES.MODE_CBC)
        iv = cipher.iv

        padded_text = pad(text.encode('utf-8'), AES.block_size)
        encrypted_text = cipher.encrypt(padded_text)

        return iv + encrypted_text   # prepend IV


    def decrypt(cipher_text, key):
        iv = cipher_text[:AES.block_size]

        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_message = cipher_text[AES.block_size:]

        decrypted_text = unpad(
            cipher.decrypt(encrypted_message),
            AES.block_size
        ).decode('utf-8')

        return decrypted_text


    print("AES Algorithm Program")
    print("1. Encrypt")
    print("2. Decrypt")

    choice = int(input("Choose an option: "))

    if choice == 1:
        text = input("Enter the text to encrypt: ")

        key = token_bytes(16)  # 16 bytes = 128-bit key
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
aes_algorithm()