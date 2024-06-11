from Crypto.Util.number import inverse, long_to_bytes

e = 876603837240112836821145245971528442417
p = 99132954671935298039
q = 59644326261100157131

phi = (p-1)*(q-1)

d = inverse(e, phi)

print("priv key is: ", d)
