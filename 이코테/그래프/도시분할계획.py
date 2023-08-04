

"""
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
"""

def find(parent, x):
    if parent[x]!=x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, b)
    b = find(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v, e = map(int, input().split())
parent = [0] *(v+1)

edges = []
answer = 0

for i in range(1, v+1):
    parent[i]=i
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
last = 0

for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer += cost
        last = cost
print(answer - last)


n, m = map(int, input().split())

