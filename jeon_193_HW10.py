# CSE 4256 Homework 10
# Sooyoung Jeon

# Question 1
# Look and say n-th time
def look_and_say(n):

    if n == 1:
        return '1'
    if n == 2:
        return '11'

    s = '11'

    for i in range(2, n):
        l = len(s)
        count = 1
        temp = ''

        for j in range(1, l):
            if s[j] != s[j - 1]:
                temp += str(count)
                temp += s[j - 1]
                count = 1
            else:
                count += 1
        temp += str(count)
        temp += s[l - 1]
        s = temp

    return s

# Question 2
# Collapse the path to the shortest path
def shortest_path(s):

    temp = '/'
    a = s.split('/')
    new_path = []
    for i in range(0, len(a)):
        path = a[i]
        if path == '..':
            new_path.pop()
        elif path == '.':
            i += 1
        elif path:
            new_path.append(path)

    for path in new_path:
        temp += path
        if path != new_path[len(new_path) - 1]:
            temp += '/'

    if s[len(s) - 1] == '/':
        temp += '/'

    return temp

# Test Case
print(shortest_path('/usr/home/./ece/lab2/./../../cse/systems/../software/lab2'))
