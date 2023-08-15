
"""
5
big
good
sky
blue
mouse
sky
good
mouse
big
"""
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
p = dict()

# 입력받은 단어들을 key값으로 사용하고 value값은 1로 지정 {'big\n': 1, 'good\n': 1, 'sky\n': 1, 'blue\n': 1, 'mouse\n': 1}
for i in range(n):
    word=input()
    p[word]=1

for i in range(n-1):
    word=input()
    p[word]=0
for key, value in p.items(): #key, values값들을 접근
    if value == 1:
        print(key)
        break



# n = int(input())
# word = [input() for _ in range(n)]
# # word = deque(word)
# poem = [input() for _ in range(n-1)]
#
# for c in poem:
#     if c in word:
#         word.pop(word.index(c))
#
# print(''.join(word))

