from collections import deque

# Question 1
def pentagonal_number(num):
	if num == 0:
		return 1
	else:
		return pentagonal_number(num - 1) + 5 * (num - 1)

# Question 2
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

def decode(s):
	result = ''
	for i in range(len(s) - 1):
		if i % 2 == 0:
			result += (int(s[i]) * s[i + 1])
	return result

# Question 3
def is_balanced(s):
  stack = deque()
  for paren in s:
    if paren == '(' or paren == '{' or paren == '[':
      stack.append(paren)
    else:
      if stack:
        stack.pop()
      else:
        return False
  if len(stack) != 0:
    return False
  return True


print(is_balanced('({(()}))'))