
"""
부분집합
상태트리 구성하기
"""
# def DFS(x):
#     if x==n+1:
#         # for i in range(1, n+1):
#         #     if ch[i]==1:
#         #         print(i, end=' ')
#         # print()
#     else:
#         ch[x]=1
#         DFS(x+1)
#         ch[x]=0
#         DFS(x+1)
#
# n = int(input())
# ch=[0]*(n+1)
# DFS(1)


# def DFS(v):
#     if v==n+1: #n=3까지는 가능, 4부터 안 됨으로 n+1
#         for i in range(1, n+1):
#             if ch[i]==1:
#                 print(i, end=' ')
#         print()
#     else:
#         ch[v]=1 #사용한다
#         DFS(v+1) #다음 D생성
#         ch[v]=0
#         DFS(v+1)
#
# n = int(input())
# ch=[0]*(n+1)
# DFS(1)

"""
다시 복습
"""

# def DFS(L):
#     if L==n+1: #4까지임으로
#         for i in range(1,n+1): #출력을 위해
#             if ch[i]==1:
#                 print(i, end=' ')
#         print()
#     else:
#         ch[L]=1 #사용한다
#         DFS(L+1)
#         ch[L]=0 #사용하지 않는다
#         DFS(L+1)
# n = int(input())
# ch=[0]*(n+1)
# DFS(1)


def DFS(v):
    if v==n+1:
        for j in range(1, n+1):
            if ch[j]==1:
                print(j, end=' ')
        print()
    else:
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)



n = int(input())
ch=[0]*(n+1)
DFS(1)