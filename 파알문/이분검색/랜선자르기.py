
"""
4 11
802
743
457
539

k, n = map(int, input().split())
#1. 방법 - for문 [802, 743, 457, 539]
arr = []
for _ in range(k):
    s = int(input())
    arr.append(s)
#2. 방법 - 리스트 컨프리헨션 [[802], [743], [457], [539]]
arr2 = [list(map(int, input().split())) for _ in range(4)]

print(arr) # [802, 743, 457, 539]
print(arr2) # [[802], [743], [457], [539]]
"""

k, n = map(int, input().split())
# arr = []
# for _ in range(k):
#     s = int(input())
#     arr.append(s)

array = [int(input()) for _ in range(k)]

print(array)