from collections import deque
import random

# CSE 4256 Homework 8
# Sooyoung Jeon

# Question 1
# Calculate the number of dots in pantagonal form with recursion
def pentagonal_number(num):
	if num == 0:
		return 1
	else:
		return pentagonal_number(num - 1) + 5 * (num - 1)

# Question 2
# Encode the given string by its count and letter
def encode(s):
	result = ''
	count = 1
	for i in range(1, len(s)):
		if s[i - 1] == s[i]:
			count += 1
		else:
			result += str(count) + s[i - 1]
			count = 1
	result += str(count) + s[i]
	return result

# Decode the given string by its count and letter
def decode(s):
	result = ''
	for i in range(len(s) - 1):
		if i % 2 == 0:
			result += (int(s[i]) * s[i + 1])
	return result

# Question 3
# Use stack to check rahter the given string brackets are balanced or not
def is_balanced(s):
	stack = deque()
	for paren in s:
		if paren == '(' or paren == '{' or paren == '[':
			stack.append(paren)
		else:
			if len(stack) == 0:
				return False
			lastParen = stack.pop()
			result = False
			if (lastParen == '(' and paren == ')') or (lastParen == '{' and paren == '}') or (lastParen == '[' and paren == ']'):
				result = True
			if not result:
				return False
	if len(stack) != 0:
		return False
	return True

# Question 4
# Use random number to generate both x and y coordinate, fill the square, and calculate the percentage of the dots in the circle to get the pi value
def get_pi(n):
	in_circle = 0
	all = 0
	while n:
		x = random.uniform(-1, 1)
		y = random.uniform(-1, 1)
		if (x ** 2 + y ** 2) <= 1:
			in_circle += 1
		all += 1
		n -= 1
	return 4 * (in_circle / all)
