import string
import random
def encrypt(code_book):
    cipherText = ''
    plainText = input("Enter Plain Text: ").upper()
    plainText = plainText.replace(" ","")
    for i in plainText:
        cipherText += code_book[i]
    print("\nCipher Text :", cipherText)
def decrypt(code_book):
    code_book = { v:k for (k,v) in code_book.items()}    
    plainText = ''
    cipherText = input("\nEnter Cipher Text: ").upper()
    plainText = plainText.replace(" ","")
    for i in cipherText:
        plainText += code_book[i]
    print("\nPlanin Text :", plainText)

def get_code_book():
    keys = [i for i in string.ascii_uppercase] 
    values = keys.copy()
    random.shuffle(values)
    res = {}
    for key in keys:
        for value in values:
            res[key] = value
            values.remove(value)
            break
    return res
code_book = get_code_book()

encrypt(code_book)
decrypt(code_book)

