
# CSE 4256 Homework 4
# Sooyoung Jeon

# Question 1
# Find a most commonly used letter in a string
def common_letter(s):
  lettersDict = {}
  for c in s.lower():
    if (c.islower()):
      if c in lettersDict:
        lettersDict[c] += 1
      else:
        lettersDict[c] = 1

  count = 0
  letter = 0
  for key, value in lettersDict.items():
    if value > count:
      count = value
      letter = key
  return letter

# Question 2
# Group two strings as a dictionary
def make_dict(str1, str2):
  dic = {}
  for sy1, sy2 in zip(str1, str2):
   dic[sy1] = sy2
  return dic