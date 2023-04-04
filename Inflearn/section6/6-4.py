

"""
합이 같은 부분집합
"""
import sys


def DFS(L, sum): #L:인덱스
    if L==n:
        if sum==(total-sum): #반대편 부분집합
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)

n = int(input())
a = list(map(int, input().split()))
total=sum(a)
DFS(0,0)
print("NO")

