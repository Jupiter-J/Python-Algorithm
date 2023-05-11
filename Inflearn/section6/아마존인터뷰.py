
"""
아마존인터뷰
"""

import sys
#sys.stdin=open("input.txt", "rt")  # read text

def DFS(L, sum):    # a 리스트의 인덱스 번호(Level), 부분집합의 합
    if sum > total//2:
        return
    if L == n:
        if sum == (total - sum):  # 두개의 부분집합으로 나누었을때 각각의 합이 같은 경우
            print("YES")
            sys.exit(0)           # 함수가 아닌 프로그램 종료
    else:
        DFS(L+1, sum+a[L])    # 부분집합에 자기자신 포함
        DFS(L+1, sum)         # 부분집합에 자기자신 미포함

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")