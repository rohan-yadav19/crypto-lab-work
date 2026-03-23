# MD5 Hashing Algorithm Implementation
# CNS LAB

import hashlib


def compute_md5_hash(input_string):
    # Create MD5 hash object
    md5_hash = hashlib.md5()

    # Encode and update
    md5_hash.update(input_string.encode('utf-8'))

    # Return hexadecimal hash
    return md5_hash.hexdigest()


def md5_program():
    input_string = input("Enter the string to hash using MD5: ")
    md5_result = compute_md5_hash(input_string)

    print("MD5 Hash:", md5_result)


# Run program
md5_program()