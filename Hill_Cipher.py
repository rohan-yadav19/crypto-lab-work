# Hill Cipher Encryption and Decryption Program
# CNS LAB

import numpy as np

def hill_cipher():

    def encrypt(text, key):
        n = int(len(key) ** 0.5)
        key_matrix = np.array(key).reshape(n, n)

        text = text.upper().replace(" ", "")
        while len(text) % n != 0:
            text += 'X'

        text_matrix = [ord(c) - ord('A') for c in text]
        text_matrix = np.array(text_matrix).reshape(-1, n).T

        encrypted_matrix = np.dot(key_matrix, text_matrix) % 26

        encrypted_text = "".join(
            chr(num + ord('A')) for num in encrypted_matrix.T.flatten()
        )

        return encrypted_text


    def decrypt(cipher, key):
        n = int(len(key) ** 0.5)
        key_matrix = np.array(key).reshape(n, n)

        det = int(round(np.linalg.det(key_matrix)))
        det_inv = pow(det, -1, 26)

        adjugate = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
        inverse_key = (det_inv * adjugate) % 26

        cipher_matrix = [ord(c) - ord('A') for c in cipher]
        cipher_matrix = np.array(cipher_matrix).reshape(-1, n).T

        decrypted_matrix = np.dot(inverse_key, cipher_matrix) % 26

        decrypted_text = "".join(
            chr(num + ord('A')) for num in decrypted_matrix.T.flatten()
        )

        return decrypted_text


    print("Hill Cipher Program")
    print("1. Encrypt")
    print("2. Decrypt")

    choice = int(input("Choose an option: "))

    if choice in [1, 2]:
        text = input("Enter the text: ")
        n = int(input("Enter the size of the key matrix (n x n): "))

        print("Enter the key matrix row by row:")
        key = []
        for _ in range(n):
            row = list(map(int, input().split()))
            key.extend(row)

        if choice == 1:
            encrypted = encrypt(text, key)
            print("Encrypted Text:", encrypted)

        elif choice == 2:
            decrypted = decrypt(text, key)
            print("Decrypted Text:", decrypted)

    else:
        print("Invalid choice!")


# Run program
hill_cipher()