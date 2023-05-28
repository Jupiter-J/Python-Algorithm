
"""
사과나무
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
"""

# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# num = 0
# z=k=n//2
#
# for i in range(n):
#     for j in range(z, k+1):
#         num+=a[i][j]
#     if i<n//2:
#         z-=1
#         k+=1
#     else:
#         z+=1
#         k-=1
# print(num)


"""
큐로 풀기
"""
# from collections import deque
# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# dx = [-1, 0, 1, 0]
# dy= [0, 1, 0, -1]
# ch=[[0]*n for _ in range(n)]
# sum=0
# Q = deque()
#
# # 중앙체크
# ch[n//2][n//2]=1
# sum+=a[n//2][n//2]
# Q.append((n//2, n//2))
# L=0
# while True:
#     if L==n//2:
#         break
#     size=len(Q) #Q에들어간 값의 갯수
#     for i in range(size):
#         tmp=Q.popleft()
#         for j in range(4):
#             x=tmp[0]+dx[j] #tmp 앞[0]
#             y=tmp[1]+dy[j] #뒤[1]
#             if ch[x][y]==0: #탐색지점 중복 확인
#                 sum+=a[x][y]
#                 ch[x][y]=1
#                 Q.append((x,y))
#     L+=1
# print(sum)


from collections import deque
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ch=[[0]*n for _ in range(n)]
sum=0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
Q = deque()
Q.append((n//2,n//2))
ch[n//2][n//2]=1
sum+=a[n//2][n//2]
L=0

while True:
    if L==n//2:
        break
    h = len(Q)
    for i in range(h):
        tmp= Q.popleft()
        for j in range(4):
            x=tmp[0]+dx[j]
            y=tmp[1]+dy[j]
            if ch[x][y]==0:
                sum+=a[x][y]
                ch[x][y]=1
                Q.append((x,y))
    L+=1
print(sum)