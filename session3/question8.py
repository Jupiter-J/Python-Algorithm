

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    h, t, k=map(int, input().split()) #h:행 t:방향 k:회전
    if t==0: #t:0왼쪽 회전
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0)) #append: 리스트의 마지막에 추가됨
    else: #t:1오른쪽 회전
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop()) #h행 -1이 인덱스
res=0
s=0
e=n-1
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)