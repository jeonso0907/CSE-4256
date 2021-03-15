
# CSE 4256 Homework 2
# Sooyoung Jeon

# Question 1
# "This", "list", "words" should be omitted
s = ["This", "is", "a", "list", "of", "words"]

strings = [word for word in s if len(word) < 4]
print(strings)

# Question 2
# 4, 5, 6 should be omitted
i = [1, 2, 3, 4, 5, 6, 7, 8]

ints = [(num**2 + 10) for num in i if ((num**2 + 10) % 10 != 5 and (num**2 + 10) % 10 != 6)]
print(ints)

# Question 3
# Should print 95 (100 - 5)
d_list = [30, 5, 32, 28, 39, 100, 7]

def diff(list):
  min = list[0]
  max = list[0]
  for i in range(1, len(list)):
    number = list[i]
    if (number > max):
      max = number
    if (number < min):
      min = number
  return max - min

# Qeustion 4
# Should print true (5 + 2 + 6 = 9 + 4 = 13)
s_list = [5, 2, 6, 9, 4]

def splitable(list):
  front = 0
  for i in range(0, len(list)):
    front += list[i]
    back = 0
    for j in range(i + 1, len(list)):
      back += list[j]

    if (front == back):
      return True
  return False

print (diff(d_list))
print (splitable(s_list))