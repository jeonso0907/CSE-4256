from collections import deque
from collections import defaultdict

# CSE 4256 Homework 5
# Sooyoung Jeon

# Question 1
# Check rather the given string brackets is balanced or not
def is_balanced(s):
  stack = deque()
  for paren in s:
    if paren == '(':
      stack.append(paren)
    else:
      if stack:
        stack.pop()
      else:
        return False
  if len(stack) != 0:
    return False
  return True

# Question 2
# Use the BFS to record the each node's distance from the starting node
def bfs(graph, start):
  l = defaultdict(int)
  queue = deque([start])
  while queue:
    n = queue.popleft()
    for v in graph[n]:
      if v not in l:
        queue.append(v)
        l[v] += l[n] + 1
  return l