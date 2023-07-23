
"""
3
15
27
12
"""

n = int(input())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)
# arr.sort(reverse=True)
print(sorted(arr, reverse=True))

