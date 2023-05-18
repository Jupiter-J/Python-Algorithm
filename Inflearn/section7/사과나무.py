
"""
사과나무
"""

from collections import deque
# 방향 탐색
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

# 입력
n = int(input())
a=[list(map(int, input().split())) for _ in range(n)]
# 방문 여부 check
ch=[[0]*n for _ in range(n)]
sum=0
#큐사용
Q=deque()
# 중간지점부터 체크하고 출발
ch[n//2][n//2]=1
sum+=a[n//2][n//2]
Q.append((n//2, n//2))
L=0
while True:
    if L==n//2:
        break
    size=len(Q)
    for i in range(size):
        tmp=Q.popleft()
        for j in range(4):
            x=tmp[0]+dx[j]
            y=tmp[1]+dy[j]
            if ch[x][y]==0:
                sum+=a[x][y]
                ch[x][y]=1
                Q.append((x,y))
    L+=1
print(sum)


