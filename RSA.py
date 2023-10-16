import random

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to generate a random prime number
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

# Function to calculate the greatest common divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find the modular multiplicative inverse
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Generate two random prime numbers
bits = 16
p = generate_prime(bits)
q = generate_prime(bits)

# Calculate n and phi(n)
n = p * q
phi_n = (p - 1) * (q - 1)

# Choose a random public key exponent (e) such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
while True:
    e = random.randrange(2, phi_n)
    if gcd(e, phi_n) == 1:
        break

# Calculate the private key exponent (d) using the modular multiplicative inverse
d = mod_inverse(e, phi_n)

# Public key: (n, e)
# Private key: (n, d)

# Encryption function
def encrypt(message, n, e):
    return pow(message, e, n)

# Decryption function
def decrypt(ciphertext, n, d):
    return pow(ciphertext, d, n)

# Input a message from the user
message = int(input("Enter a number to encrypt: "))

# Check if the message is within the valid range
if message >= n:
    print("Message is too large for this RSA setup. Please choose a smaller number.")
else:
    # Encrypt the message
    ciphertext = encrypt(message, n, e)
    print(f"Ciphertext: {ciphertext}")

    # Decrypt the ciphertext
    decrypted_message = decrypt(ciphertext, n, d)
    print(f"Decrypted message: {decrypted_message}")
