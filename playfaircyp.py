import string

def generate_playfair_matrix(key):
    key = key.upper().replace('J', 'I')  
    key = key + string.ascii_uppercase  
    key = ''.join(dict.fromkeys(key)) 
    matrix = [[''] * 5 for _ in range(5)]
    key_index = 0
    for row in range(5):
        for col in range(5):
            matrix[row][col] = key[key_index]
            key_index += 1
    return matrix

def get_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col

def encrypt(plaintext, matrix):
    ciphertext = ''
    plaintext = plaintext.upper().replace('J', 'I')
    plaintext = ''.join(plaintext.split()) 
    if len(plaintext) % 2 != 0:
        plaintext += 'X'
    index = 0
    while index < len(plaintext):
        char1 = plaintext[index]
        char2 = plaintext[index + 1]
        row1, col1 = get_position(matrix, char1)
        row2, col2 = get_position(matrix, char2)
        if col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        elif row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]
        index += 2
    return ciphertext

def decrypt(ciphertext, matrix):
    plaintext = ''
    ciphertext = ciphertext.upper().replace('v', 'I')
    ciphertext = ''.join(ciphertext.split()) 
    index = 0
    while index < len(ciphertext):
        char1 = ciphertext[index]
        char2 = ciphertext[index + 1]
        row1, col1 = get_position(matrix, char1)
        row2, col2 = get_position(matrix, char2)
        if col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        elif row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]
        index += 2
    return plaintext

plaintext = input("Enter the message to encrypt/decrypt: ")
key = input("Enter the key: ")
matrix = generate_playfair_matrix(key)
encrypted_text = encrypt(plaintext, matrix)
print("Encrypted text:", encrypted_text)
decrypted_text = decrypt(encrypted_text, matrix)
print("Decrypted text:", decrypted_text)