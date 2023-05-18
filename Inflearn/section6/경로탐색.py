

"""
경로 탐색
한번 방문한 노드는 다시 방문하지 않는다
"""
#
# def DFS(v):
#     global cnt
#     if v==n:
#         cnt+=1
#         for x in path:
#             print(x, end=' ')
#         print()
#     else:
#         for i in range(1, n+1):
#             if g[v][i]==1 and ch[i]==0:
#                 ch[i]=1
#                 path.append(i)
#                 DFS(i)
#                 path.pop()
#                 ch[i]=0
#
# n, m = map(int, input().split())
# g = [[0]*(n+1) for _ in range(n+1)]
# ch = [0]*(n+1)
# for i in range(m):
#     a, b = map(int, input().split())
#     g[a][b]=1
#
# cnt=0
# path=[]
# path.append(1)
#
# ch[1]=1
# DFS(1)
# print(cnt)
#
#

"""
복습

반복 불가, 
"""

def DFS(L):
    global cnt
    if L==n:
        cnt+=1
    else:
        for i in range(1, n+1): #방문 노드 번호
            if g[L][i]==1 and ch[i]==0:
                ch[i]=1
                DFS(i)
                ch[i]=0

n, m = map(int ,input().split())
g = [[0]*(n+1) for _ in range(n+1)]
ch = [0]*(n+1)
for i in range(m):
    a,b = map(int, input().split())
    g[a][b]=1
cnt=0
ch[1]=1 #1번 노드 방문
DFS(1)
print(cnt)