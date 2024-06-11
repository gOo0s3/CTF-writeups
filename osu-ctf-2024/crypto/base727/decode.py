import binascii

def decode_base_727(encoded_string):
    base = 727
    decoded_value = 0

    for char in encoded_string:
        decoded_value = decoded_value * base + ord(char)

    decoded_string = ""
    while decoded_value > 0:
        decoded_string = chr(decoded_value % 256) + decoded_string
        decoded_value //= 256

    return decoded_string

# Input the hex string representing the encoded string
encoded_hex_string = input("Enter the hex string representing the encoded string: ")
encoded_string = binascii.unhexlify(encoded_hex_string).decode()

decoded_string = decode_base_727(encoded_string)
print(decoded_string)
