import pwn

conn = pwn.remote("9a674f166e971b02.247ctf.com", 50328)

for _ in range(500):
	a = conn.recvuntil("?").decode().split()
	num1 = int(a[-3])
	num2 = int(a[-1][0:-1])
	print(f"addition#{_} {num1=}, {num2=}, sum={num1+num2}", end="\r")
	conn.send(f"{num1 + num2}\r\n".encode())

flag = "247CTF" + conn.recvuntil("}").decode().split("247CTF")[1]

print(f"the flag is: {flag}")
conn.close()
