

# from itertools import combinations
# n, m= map(int, input().split())
# arr = list(range(1, n+1))
# answer = list(combinations(arr, m))
#
# for x, y in answer:
#     print(x, y, end=' ')
#     print()
# print(len(answer))


# n, m= map(int, input().split())
# ch=[0]*m
# answer=0
# for i in range(1, n+1):
#     for j in range(i+1, n+1):
#         print(i, j, end=' ')
#         answer+=1
#         print()
# print(answer)

def DFS(L, s):
    global cnt
    if L==m:
        for j in range(m):
            print(ch[j], end=' ')
        cnt+=1
        print()
    else:
        for i in range(s, n+1):
            ch[L]=i
            DFS(L+1, i+1)

n, m= map(int, input().split())
ch=[0]*(n+1)
cnt=0
DFS(0,1)
print(cnt)