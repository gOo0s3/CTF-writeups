import string
import random
import sys

def generate_key(entrypoint):
    random.seed(entrypoint)
    letters = list(string.ascii_lowercase)
    key = list(letters)
    random.shuffle(key)
    return dict(zip(letters, key))

entrypoint = "YP.295C710119D9179B67A2B4CBA20414D5"
key = generate_key(entrypoint)

with open("encrypted.txt", "r") as f:
	cipher = f.read().strip()

decrypted = ""
for c in cipher:
        if c in key.values():
                decrypted += (list(key.keys())[list(key.values()).index(c)])
        else:
                decrypted += c

print(key)
#print(decrypted)
