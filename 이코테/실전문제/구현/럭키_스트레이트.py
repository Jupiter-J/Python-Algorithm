"""
123402
"""

n = int(input())
n= list(map(int, str(n)))
s= len(n)

if sum(n[:s//2]) == sum(n[s//2:]):
    print("LUCKY")
else:
    print("READY")
