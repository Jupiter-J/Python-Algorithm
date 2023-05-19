

# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# res=0
# s=e=n//2
# for i in range(n):
#     for j in range(s, e+1): #세로열을 제어 (펼쳤다가 좁히기)
#         res+=a[i][j] #중앙선
#         print(a[i][j], end=' ')
#     if i<n//2:
#         s-=1
#         e+=1
#     else:
#         s+=1
#         e-=1
# print(res)

"""
사과나무
"""

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
s=e=n//2
res=0
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1

print(res)


