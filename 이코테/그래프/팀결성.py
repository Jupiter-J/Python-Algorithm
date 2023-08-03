"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n, m = map(int, input().split())
parent = [0]*(n+1)

# 자기자신으로 초기화
for i in range(0, n+1):
    parent[i]=i

# 연산을 하나씩 확인
for i in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(parent, a, b)
    elif op == 1:
        if find(parent, a) == find(parent, b):
            print('YES')
        else:
            print('NO')
