

"""
순열 추측하기
4 16
"""

import sys
input = sys.stdin.readline
def DFS(L, sum):
    if L==n and sum==f:
        for x in p:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                DFS(L+1, sum+(p[L]*b[L]))
                ch[i]=0


n, f = map(int, input().split())
p = [0]*n # 순열 저장
b = [1]*n # 초기화
ch = [0]*(n+1) # 중복 방지 체크
for i in range(1, n):
    b[i]=b[i-1]*(n-i)/i #DP아냐..? 점화식 중요
print(DFS(0, 0))







