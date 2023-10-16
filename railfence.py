#railfence
def encrypt_rail_fence(plaintext, num_rails):
    rail_fence = [['' for _ in range(len(plaintext))] for _ in range(num_rails)]
    rail = 0
    direction = 1

    # Write each character of the plaintext to the appropriate rail
    for char in plaintext:
        rail_fence[rail].append(char)
        rail += direction

        # Change direction when reaching the top or bottom rail
        if rail == num_rails - 1 or rail == 0:
            direction = -direction

    # Flatten the rail_fence to get the ciphertext
    ciphertext = ''.join([char for rail in rail_fence for char in rail if char != ''])
    return ciphertext

def decrypt_rail_fence(ciphertext, num_rails):
    rail_fence = [['' for _ in range(len(ciphertext))] for _ in range(num_rails)]
    rail = 0
    direction = 1
# Calculate the pattern of rails
    pattern = []
    for _ in range(len(ciphertext)):
        pattern.append(rail)
        rail += direction
        if rail == num_rails - 1 or rail == 0:
            direction = -direction

    # Write each character of the ciphertext to the appropriate rail
    index = 0
    for char in ciphertext:
        rail_fence[pattern[index]].append(char)
        index += 1

    # Read each rail to get the plaintext
    plaintext = ''.join([char for rail in rail_fence for char in rail])
    return plaintext
# Example usage:
plaintext = "PATELKIRTI"
num_rails = 3

ciphertext = encrypt_rail_fence(plaintext, num_rails)
decrypted_text = decrypt_rail_fence(ciphertext, num_rails)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:",decrypted_text)