
"""
중복순열 구하기
"""
# import sys
# input=sys.stdin.readline()
# # 문자열 읽을때 s= input.rstrip()

def DFS(L):
    global cnt
    if L==m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            res[L]=i
            DFS(L+1)

n, m = map(int, input().split())
res=[0]*m
cnt=0
DFS(0)
print(cnt)