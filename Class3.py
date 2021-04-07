
# CSE 4256 Homework 3
# Sooyoung Jeon

# Question 2
# Determine rather a list includes the unique elements or not
def is_unique(list):
  return len(list) is len(set(list))


# Question 3
# Check rather a string contains all the voewls
def contains(s):
  s = s.lower()
  return all(vowel in s for vowel in 'aeiou')