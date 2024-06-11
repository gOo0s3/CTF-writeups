def main():
	with open("output.txt", "r") as f:
		text = [l.strip() for l in f.readlines()]
		n = int(text[1][3:])
		enc_nums = [int(num) for num in text[3].split()]

	flag = ""
	for num in enc_nums:
		flag += chr(1 + int(pow(num, 1/3)))

	print(flag)

if __name__ == "__main__":
	main()
