# Playfair Cipher Encryption and Decryption Program
# CNS LAB

def playfair_cipher():

    def create_matrix(key):
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        matrix = []
        used = set()

        key = key.upper().replace("J", "I")

        for char in key + alphabet:
            if char not in used and char.isalpha():
                matrix.append(char)
                used.add(char)

        return [matrix[i:i + 5] for i in range(0, 25, 5)]


    def find_position(matrix, char):
        for i, row in enumerate(matrix):
            if char in row:
                return i, row.index(char)
        return None


    def encrypt(text, key):
        text = text.upper().replace("J", "I").replace(" ", "")
        matrix = create_matrix(key)

        if len(text) % 2 != 0:
            text += "X"

        encrypted = ""

        for i in range(0, len(text), 2):
            a, b = text[i], text[i + 1]
            row1, col1 = find_position(matrix, a)
            row2, col2 = find_position(matrix, b)

            if row1 == row2:
                encrypted += matrix[row1][(col1 + 1) % 5]
                encrypted += matrix[row2][(col2 + 1) % 5]

            elif col1 == col2:
                encrypted += matrix[(row1 + 1) % 5][col1]
                encrypted += matrix[(row2 + 1) % 5][col2]

            else:
                encrypted += matrix[row1][col2]
                encrypted += matrix[row2][col1]

        return encrypted


    def decrypt(cipher, key):
        matrix = create_matrix(key)
        decrypted = ""

        for i in range(0, len(cipher), 2):
            a, b = cipher[i], cipher[i + 1]
            row1, col1 = find_position(matrix, a)
            row2, col2 = find_position(matrix, b)

            if row1 == row2:
                decrypted += matrix[row1][(col1 - 1) % 5]
                decrypted += matrix[row2][(col2 - 1) % 5]

            elif col1 == col2:
                decrypted += matrix[(row1 - 1) % 5][col1]
                decrypted += matrix[(row2 - 1) % 5][col2]

            else:
                decrypted += matrix[row1][col2]
                decrypted += matrix[row2][col1]

        return decrypted


    print("Playfair Cipher Program")
    print("1. Encrypt")
    print("2. Decrypt")

    choice = int(input("Choose an option: "))

    if choice in [1, 2]:
        text = input("Enter the text: ")
        key = input("Enter the key: ")

        if choice == 1:
            encrypted = encrypt(text, key)
            print("Encrypted Text:", encrypted)

        elif choice == 2:
            decrypted = decrypt(text, key)
            print("Decrypted Text:", decrypted)

    else:
        print("Invalid choice!")


# Program execution
playfair_cipher()