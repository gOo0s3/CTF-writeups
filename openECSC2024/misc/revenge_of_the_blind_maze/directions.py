import requests

with open("paths.txt", "r") as f:
	directions = [line.split("=")[1].strip() for line in f.readlines()]

for direction in directions:
	print(direction, end=" ")

"""base_url = "http://blindmazerevenge.challs.open.ecsc2024.it/maze"
start_url = f"{base_url}?direction=start"
session = requests.Session()

response = session.get(start_url)

cookies = response.cookies

for direction in directions:
	url = f"{base_url}?direction={direction}"
	response = session.get(url, cookies=cookies)
	while "FAILED" in response.text:
		response = session.get(url, cookies=cookies)
		print(f"Response text: {response.text}")"""
