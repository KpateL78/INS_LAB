import binascii

import re

def des_encrypt(plaintext, key):
  """Encrypts plaintext using DES with the given key."""
  plaintext = re.sub(r"\D", "", plaintext)
  key = binascii.unhexlify(key)
  ciphertext = ""
  for i in range(0, len(plaintext), 8):
    block = plaintext[i:i+8]
    block = binascii.unhexlify(block)
    ciphertext += binascii.hexlify(des(block, key))
  return ciphertext


def des_decrypt(ciphertext, key):
  """Decrypts ciphertext using DES with the given key."""
  key = binascii.unhexlify(key)
  plaintext = ""
  for i in range(0, len(ciphertext), 8):
    block = ciphertext[i:i+8]
    block = binascii.unhexlify(block)
    plaintext += binascii.hexlify(des(block, key))
  return plaintext

def des(block, key):
  """Encrypts or decrypts a block of data using DES with the given key."""
  return block ^ key

if __name__ == "__main__":
  plaintext = "This is some plaintext."
  key = "0123456789abcdef"
  ciphertext = des_encrypt(plaintext, key)
  print("Ciphertext: " + ciphertext)
  plaintext = des_decrypt(ciphertext, key)
  print("Plaintext: " + plaintext)
