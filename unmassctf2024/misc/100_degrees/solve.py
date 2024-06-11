with open("journal.txt", "r") as points_file:
	point_data = [line.strip() for line in points_file.readlines()][2:103]

points = [(i, int(pd.split()[-1])) for i, pd in enumerate(point_data)]

values = [point[1] for point in points]

def lagrange_basis(i, x):
	numerator, denomenator = 1, 1
	for m in range(101):
		if m != i:
			numerator *= x - m
			denomenator *= i - m
	return numerator//denomenator

def lagrange_interpolating_polynomial(x):
	sum = 0
	for i in range(101):
		sum += values[i] * lagrange_basis(i, x)
	return sum

for i in range(101, 133):
	print(lagrange_interpolating_polynomial(i), end=" ")
