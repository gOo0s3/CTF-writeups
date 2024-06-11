with open("suspicious_caesar_cipher.out") as f:
	data = [l.strip() for l in f.readlines()]

e, n, encrypted = int(data[1]), int(data[2]), eval(data[4].replace("L", ""))

charset = '0123456789abcdefABCDEFT{}'

dec = ""
for enc in encrypted:
	for c in charset:
		if pow(ord(c), e, n) == enc:
			dec += c
			break

print(dec)
