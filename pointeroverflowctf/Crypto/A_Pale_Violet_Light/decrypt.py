C = "933969 15848125 24252056 5387227 5511551 10881790 3267174 14500698 28242580 933969 32093017 18035208 2594090 2594090 9122397 21290815 15930721 4502231 5173234 21290815 23241728 2594090 21290815 18035208 10891227 15930721 202434 202434 21290815 5511551 202434 4502231 5173234 25243036"
ords = C.split()
ords_of_encrypted_chars = [int(c) for c in ords]

# m = c^d mod(n)
def decrypt(character, n, d):
	return (character ** d) % n


N = 34034827
d = 202559

ords_of_decrypted_chars = [decrypt(char, 34034827, 202559) for char in ords_of_encrypted_chars]
print(ords_of_decrypted_chars)
flag_chars = [chr(x) for x in ords_of_decrypted_chars]
print(flag_chars)

dec_flag = ""
for x in flag_chars:
	dec_flag += x

print(dec_flag)
