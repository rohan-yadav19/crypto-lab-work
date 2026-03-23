# SHA-1 Hashing Algorithm Implementation
# CNS LAB

import hashlib


def compute_sha1_hash(input_string):
    # Create SHA-1 hash object
    sha1_hash = hashlib.sha1()

    # Encode and update
    sha1_hash.update(input_string.encode('utf-8'))

    # Return hexadecimal hash
    return sha1_hash.hexdigest()


def sha1_program():
    input_string = input("Enter the string to hash using SHA-1: ")
    sha1_result = compute_sha1_hash(input_string)

    print("SHA-1 Hash:", sha1_result)


# Run program
sha1_program()