

"""
BFS - 넒이 우선 탐색
큐를 사용한다
"""

from collections import deque
MAX=10000
dis = [0]*(MAX+1)
ch = [0]*(MAX+1)
n, m = map(int, input().split())
ch[n]=1 #n체크
dis[n]=0 #출발지점~ 몇번만에 갔는가
dQ= deque()
dQ.append(n) #출발점 추가

while dQ: #안에 들어있으면 무한~~
    now=dQ.popleft() #오른쪽에서 하나 꺼냄
    if now==m:
        break
    for next in(now-1, now+1, now+5):
        if 0<next<=MAX:
            if ch[next]==0:
                dQ.append(next)
                ch[next]=1
                dis[next]=dis[now]+1
print(dis[m])