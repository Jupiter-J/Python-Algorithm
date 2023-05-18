
"""
순열 구하기
"""
# def DFS(L):
#     global cnt
#     if L==m:
#         for j in range(L):
#             print(res[j], end=' ')
#         print()
#         cnt+=1
#     else:
#         for i in range(1, n+1):
#             if ch[i]==0: #체크안되면
#                 ch[i]=1 #체크해주기
#                 res[L]=i #출력리스트 저장
#                 DFS(L+1) #다음 레벨
#                 ch[i]=0 #호출후 초기화
#
# n, m = map(int, input().split())
# cnt=0
# ch=[0]*(n+1)
# res=[0]*m
# DFS(0)
# print(cnt)
#
# def DFS(L):
#     global cnt
#     if L==m:
#         for j in range(m):
#             print(res[j], end=' ')
#         print()
#         cnt+=1
#     else:
#         for i in range(1, n+1):
#             if ch[i]==0:
#                 ch[i]=1
#                 res[L]=i
#                 DFS(L+1)
#                 ch[i]=0
#
# n, m = map(int, input().split())
# res=[0]*n
# ch=[0]*(n+1)
# DFS(0)
# print(cnt)


"""
복습
- 중복제거 필요

"""

def DFS(L):
    global cnt
    if L==m:
        for j in range(m):
            print(res[j], end=' ')
        cnt+=1
        print()
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                ch[i]=0

n, m = map(int, input().split())
res=[0]*m
ch=[0]*(n+1)
cnt=0
DFS(0)
print(cnt)