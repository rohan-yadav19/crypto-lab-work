# RSA Algorithm Encryption and Decryption Program
# CNS LAB

import random
from sympy import isprime
from math import gcd


# Generate a random prime number
def generate_prime(start=100, end=500):
    while True:
        prime = random.randint(start, end)
        if isprime(prime):
            return prime


# Compute modular inverse (fixed version)
def modular_inverse(e, phi):
    return pow(e, -1, phi)


# RSA Key Generation
def generate_keys():
    while True:
        p = generate_prime()
        q = generate_prime()

        if p == q:
            continue

        n = p * q
        phi = (p - 1) * (q - 1)

        e = random.randint(2, phi - 1)
        while gcd(e, phi) != 1:
            e = random.randint(2, phi - 1)

        try:
            d = modular_inverse(e, phi)
            return (e, n), (d, n)
        except ValueError:
            continue  # retry if inverse fails


# Encryption
def encrypt(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]


# Decryption
def decrypt(encrypted_message, private_key):
    d, n = private_key
    return ''.join(chr(pow(char, d, n)) for char in encrypted_message)


# Main Program
def rsa_algorithm():
    print("Generating RSA keys...")

    public_key, private_key = generate_keys()

    print("Public Key:", public_key)
    print("Private Key:", private_key)

    message = input("Enter a message to encrypt: ")

    encrypted = encrypt(message, public_key)
    print("Encrypted Message:", encrypted)

    decrypted = decrypt(encrypted, private_key)
    print("Decrypted Message:", decrypted)


# Run program
rsa_algorithm()