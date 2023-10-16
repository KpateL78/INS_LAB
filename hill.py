import numpy as np
def charToNum(c):
    return ord(c) - ord('A')
def numToChar(num):
    return chr(num + ord('A'))
def matrixMultiply(keyMatrix, pair):
    result = np.dot(keyMatrix, pair) % 26
    return result
def hillCipherEncrypt(plaintext, keyMatrix):
    plaintext = plaintext.upper()
    while len(plaintext) % keyMatrix.shape[0] != 0:
        plaintext += 'X'

    ciphertext = ''
    for i in range(0, len(plaintext), keyMatrix.shape[0]):
        pair = np.array([charToNum(c) for c in plaintext[i:i + keyMatrix.shape[0]]])
        encryptedPair = matrixMultiply(keyMatrix, pair)
        encryptedText = ''.join([numToChar(num) for num in encryptedPair])
        ciphertext += encryptedText
    return ciphertext
def modInverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1 
def hillCipherDecrypt(ciphertext, keyMatrix):
    det = np.linalg.det(keyMatrix)
    detInverse = modInverse(int(det), 26)
    if detInverse == -1:
        print("Key matrix is not invertible.")
        return ""
    adjugate = (detInverse * np.round(det * np.linalg.inv(keyMatrix))).astype(int) % 26
    plaintext = ''
    for i in range(0, len(ciphertext), keyMatrix.shape[0]):
        pair = np.array([charToNum(c) for c in ciphertext[i:i + keyMatrix.shape[0]]])
        decryptedPair = matrixMultiply(adjugate, pair)
        decryptedText = ''.join([numToChar(num) for num in decryptedPair])
        plaintext += decryptedText

    return plaintext
keyMatrix = np.zeros((2, 2), dtype=int)
for i in range(2):
    for j in range(2):
        keyMatrix[i][j] = int(input(f"Enter element [{i}][{j}] of the key matrix: "))

plaintext = input("Enter the plaintext: ")

encryptedText = hillCipherEncrypt(plaintext, keyMatrix)
decryptedText = hillCipherDecrypt(encryptedText, keyMatrix)

print("Plaintext:", plaintext)
print("Encrypted Text:", encryptedText)
print("Decrypted Text:", decryptedText)