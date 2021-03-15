from collections import defaultdict

# CSE 4256 Homework 6
# Sooyoung Jeon

# Question 1
def dict_to_matrix(d):
	result = []
	for i in range(len(d)):
		result.append([0] * len(d))

	for key, value in d.items():
		for number in value:
			result[key][number] = 1
	return result

# Question 2
def dict_to_list(d):
	result = []
	for key, value in d.items():
		for number in value:
			if [number, key] not in result:
				result.append([key, number])
	return result

# Question 3
def list_to_dict(l):
	result = defaultdict(list)
	for edge in l:
		result[edge[0]].append(edge[1])
		result[edge[1]].append(edge[0])
	return result

# Question 4
def list_to_matrix(l):
	result = []
	for i in range(len(l)):
		result.append([0] * len(l))

	for edge in l:
		result[edge[0]][edge[1]] = 1
		result[edge[1]][edge[0]] = 1
	return result

# Question 5
def matrix_to_dict(m):
	result = defaultdict(list)
	for x in range(len(m)):
		row = m[x]
		for y in range(len(row)):
			if row[y] == 1:
				result[x].append(y)

	return result

# Question 6
def matrix_to_list(m):
	result = []
	for x in range(len(m)):
		row = m[x]
		for y in range(len(row)):
			if row[y] == 1 and [y, x] not in result:
				result.append([x, y])
	return result


# Test
d = {0: [1, 2],
		 1: [0, 2, 4],
		 2: [0, 1, 3],
		 3: [2, 4],
		 4: [1, 3]}

l = [(0, 1), (0, 2), (1, 2), (1, 4), (2, 3), (3, 4)]

m = [[0, 1, 1, 0, 0],
		 [1, 0, 1, 0, 1],
	   [1, 1, 0, 1, 0],
		 [0, 0, 1, 0, 1],
		 [0, 1, 0, 1, 0]]	

result = matrix_to_list(m)
print(result)
for row in result:
	print(row)