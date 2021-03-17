from collections import defaultdict

# CSE 4256 Homework 7
# Sooyoung Jeon

# Question 1
def complement_1(m):
	result = []
	for i in range(len(m)):
		result.append([0] * len(m))

	for x in range(len(m)):
		row = m[x]
		for y in range(len(row)):
			if x != y and row[y] != 1:
				result[x][y] = 1
	
	return result

# Question 2
def complement_2(g):
	result = defaultdict(list)
	l = g.keys()
	for key, value in g.items():
		for number in l:
			if number not in value and number != key:
				result[key].append(number)
	return result

# Question 3
def transpose_1(m):
	result = []
	for i in range(len(m)):
		result.append([0] * len(m))

	for x in range(len(m)):
		row = m[x]
		for y in range(len(row)):
			print(x, y, m[x][y], m[y][x])
			if x != y and (m[x][y] == 0 and m[y][x] == 1) or (m[x][y] == 1 and m[y][x] == 1):
				result[x][y] = 1
	
	return result

# Question 4
def transpose_2(g):
	result = defaultdict(list)
	l = g.keys()
	for key, value in g.items():
		for number in l:
			if number != key and key in g[number]:
				result[key].append(number)
	return result

# Test
m = [[0, 1, 0, 0],
	 [1, 0, 0, 1],
	 [0, 0, 0, 1],
	 [0, 1, 1, 0]]

g =  {0: [1, 2, 4],
	  1: [0, 2, 4],
	  2: [0, 1, 3],
	  3: [2, 4],
	  4: [1, 3]}

m2 = [[0, 1, 0, 1],
	  [0, 0, 1, 0],
	  [1, 1, 0, 1],
	  [0, 1, 1, 0]]

result = transpose_2(g)
print(result)
