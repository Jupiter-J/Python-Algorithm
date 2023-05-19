
"""
봉우리
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

all(조건이 모두 참일때 참)
"""

# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# # 봉우리탐색(시계방향)
# dx=[-1, 0 , 1, 0] #행
# dy=[0, 1, 0, -1] #열
#
# #가장자리 0으로 만들기
# a.insert(0, [0]*n) #위
# a.append([0]*n) #아래
# for x in a:
#     x.insert(0,0) #좌
#     x.append(0) #우
#
# cnt=0
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
#             cnt+=1
#
# print(cnt)


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
# 4방탐색
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
cnt=0
#0 초기화
a.append([0]*n)
a.insert(0, [0]*n)
for x in a:
    x.append(0)
    x.insert(0,0)

for i in range(n+1):
    for j in range(n+1):
        if all(a[i][j]> a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)


