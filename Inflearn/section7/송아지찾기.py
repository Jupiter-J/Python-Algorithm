

"""
BFS - 넒이 우선 탐색
큐를 사용한다
"""

# from collections import deque
# n,m =map(int, input().split())
# MAX=10000
# dis = [0]*(MAX+1)
# ch = [0]*(MAX+1)
# ch[n]=1
# dis[n]=0
# dQ = deque()
# dQ.append(n)
#
# while dQ:
#     now=dQ.popleft() #앞에 출력
#     if now==m:
#         break
#     for next in(now-1, now+1, now+5):
#         if 0<next<=MAX:
#             if ch[next]==0: #방문을 안했을때
#                 dQ.append(next)
#                 ch[next]=1 #중복 제거
#                 dis[next]=dis[now]+1 #노드를 입력
# print(dis[m])

from collections import deque
MAX=100000
s, e = map(int, input().split())
ch=[0]*(MAX+1)
dis=[0]*(MAX+1)
ch[s]=1
dis[s]=0
dQ = deque()
dQ.append(s)

while dQ:
    now = dQ.popleft()
    if now == e:
        break
    for x in (now-1, now+1, now+5):
        if 0<x<=MAX:
            if ch[x]==0:
                dQ.append(x)
                ch[x]=1
                dis[x]=dis[now]+1
print(dis[e])
