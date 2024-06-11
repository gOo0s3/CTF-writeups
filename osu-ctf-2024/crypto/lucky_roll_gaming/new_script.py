from Crypto.Util.number import getPrime, inverse
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from random import randrange
from math import floor

def lcg(s, a, b, p):
    return (a * s + b) % p

def seed_recovery(numbers, p, a, b):
    s = numbers[-1]
    for i in reversed(numbers):
        s = (inverse(a, p) * (s - b + p) % p)
    return s

p = 4420073644184861649599
a = 1144993629389611207194
b = 3504184699413397958941
out = [39, 47, 95, 1, 77, 89, 77, 70, 99, 23, 44, 38, 87, 34, 99, 42, 10, 67, 24, 3, 2, 80, 26, 87, 91, 86, 1, 71, 59, 97, 69, 31, 17, 91, 73, 78, 43, 18, 15, 46, 22, 68, 98, 60, 98, 17, 53, 13, 6, 13, 19, 50, 73, 44, 7, 44, 3, 5, 80, 26, 10, 55, 27, 47, 72, 80, 53, 2, 40, 64, 55, 6]

# Calculate the number of times `get_roll()` was called to generate out
out_calls = len(out)

# Calculate the seed after generating `out`
seed = seed_recovery(out, p, a, b)

# Calculate the number of times `get_roll()` was called to generate the key and IV
key_iv_calls = 103 - out_calls

# Calculate the seed used for the key
key_seed = lcg(seed, a, b, p) % (2**32)

# Generate the key and IV
key = bytes([lcg(key_seed, a, b, p) % 256 for _ in range(16)])
iv = bytes([lcg(key_seed, a, b, p) % 256 for _ in range(16)])

# Initialize AES cipher with the recovered key and IV
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt the ciphertext
ciphertext = bytes.fromhex('34daaa9f7773d7ea4d5f96ef3dab1bbf5584ecec9f0542bbee0c92130721d925f40b175e50587196874e14332460257b')
plaintext = cipher.decrypt(ciphertext)

print(plaintext)
