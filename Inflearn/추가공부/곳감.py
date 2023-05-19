
"""
곳감
insert(x,y)는 리스트의 x번째 위치에 y를 삽입
기존에 x번재 위치에 있던 원소와 그 뒤의 원소들은 한칸씩 밀린다

pop()
리스트의 맨 마지막 원소를 리턴하고 해단 원소는 삭제

5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
3
2 0 3
5 1 2
3 1 4
"""

# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# m = int(input())
# # 조건문 입력 - 방향이동
# for i in range(m):
#     h, t, k = map(int, input().split())
#     if t==0:
#         for _ in range(k):
#             a[h-1].append(a[h-1].pop(0)) #pop(0)이 빠지고 전부 당겨짐-> 다시 저장
#     else:
#         for _ in range(k):
#             a[h-1].insert(0, a[h-1].pop())
# # 모래시계 합
# s=0
# e=n-1
# res=0
# for i in range(n):
#     for j in range(s,e+1):
#         res+=a[i][j]
#     if i<n//2:
#         s+=1
#         e-=1
#     else:
#         s-=1
#         e+=1
# print(res)



n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    h,w,t = map(int, input().split())
    if w==0:
        for _ in range(w):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(w):
            a[h-1].insert(0,a[h-1].pop())

res=0
s=0
e=n-1
for i in range(n):
    for j in range(s,e+1):
        res+=a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)