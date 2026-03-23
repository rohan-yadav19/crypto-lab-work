# Diffie-Hellman Key Exchange Algorithm
# CNS LAB

import random


# Function to compute modular exponentiation
def modular_exponentiation(base, exponent, modulus):
    return pow(base, exponent, modulus)


def diffie_hellman_key_exchange():
    # Step 1: Public values
    p = int(input("Enter a prime number (p): "))
    g = int(input("Enter a base (g): "))

    print(f"Publicly shared values: p = {p}, g = {g}")

    # Step 2: Private keys
    private_key_a = random.randint(1, p - 1)
    private_key_b = random.randint(1, p - 1)

    print("Private keys have been selected.")

    # Step 3: Public keys
    public_key_a = modular_exponentiation(g, private_key_a, p)
    public_key_b = modular_exponentiation(g, private_key_b, p)

    print("Public Key A:", public_key_a)
    print("Public Key B:", public_key_b)

    # Step 4: Shared secret
    shared_secret_a = modular_exponentiation(public_key_b, private_key_a, p)
    shared_secret_b = modular_exponentiation(public_key_a, private_key_b, p)

    print("Shared Secret computed by A:", shared_secret_a)
    print("Shared Secret computed by B:", shared_secret_b)

    # Verification
    if shared_secret_a == shared_secret_b:
        print("Key exchange successful! Shared secret is established.")
    else:
        print("Key exchange failed.")


# Run program
diffie_hellman_key_exchange()