import string

ciphertext = "i GUEss YOu CANnot apPReciaTe THE faCt tHAT i Was rEAlly tRyINg TO MakE the wHOlE fLaG acqUisiTIon THINg EAsY FOR yoU. buT I guess YOU jUsT cAn'T SAY YeS. For oNCe. YOu do kNoW WhAT The POInT of tHiS CTF Is RIghT? YOu SHouLd Be DOInG eveRyTHING yOU CaN TO gET aS many POints As POSsIble, As SOON As POSSibLe. tHEre is oNLY oNe FiRsT PLACe WINnER. YoU SimplY cANnOT Win WIThOut aNY FLAgS."

cipher_words = ciphertext.split()

def foo(word):
	binout = ""
	for char in word:
		if char in string.ascii_uppercase:
			binout += "1"
		elif char in string.ascii_lowercase:
			binout += "0"
	return binout

bin_decoded = [foo(cipher_word) for cipher_word in cipher_words]

for b in bin_decoded:
	print(b, end="")
