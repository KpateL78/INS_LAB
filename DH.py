import random

# Function to calculate (base^exp) % mod efficiently
def fast_modulo(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result

# Generate random prime number
def generate_prime(bits=256):
    while True:
        num = random.getrandbits(bits)
        if num > 1 and is_prime(num):
            return num

# Check if a number is prime
def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Miller-Rabin primality test
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = fast_modulo(a, n - 1, n)
        if x != 1:
            return False
    return True

# Diffie-Hellman Key Exchange
def diffie_hellman():
    # Generate random prime number and primitive root
    prime = generate_prime()
    primitive_root = random.randint(2, prime - 2)

    # Alice's private key and public key
    alice_private_key = random.randint(2, prime - 2)
    alice_public_key = fast_modulo(primitive_root, alice_private_key, prime)

    # Bob's private key and public key
    bob_private_key = random.randint(2, prime - 2)
    bob_public_key = fast_modulo(primitive_root, bob_private_key, prime)

    # Shared secret computation
    alice_shared_secret = fast_modulo(bob_public_key, alice_private_key, prime)
    bob_shared_secret = fast_modulo(alice_public_key, bob_private_key, prime)

    return prime, primitive_root, alice_private_key, alice_public_key, bob_private_key, bob_public_key, alice_shared_secret, bob_shared_secret

if __name__ == "__main__":
    prime, primitive_root, alice_private_key, alice_public_key, bob_private_key, bob_public_key, alice_shared_secret, bob_shared_secret = diffie_hellman()

    print(f"Prime: {prime}")
    print(f"Primitive Root: {primitive_root}")
    print(f"Alice's Private Key: {alice_private_key}")
    print(f"Alice's Public Key: {alice_public_key}")
    print(f"Bob's Private Key: {bob_private_key}")
    print(f"Bob's Public Key: {bob_public_key}")
    print(f"Alice's Shared Secret: {alice_shared_secret}")
    print(f"Bob's Shared Secret: {bob_shared_secret}")

    if alice_shared_secret == bob_shared_secret:
        print("Shared secrets match. Key exchange successful!")
    else:
        print("Shared secrets do not match. Key exchange failed!")
