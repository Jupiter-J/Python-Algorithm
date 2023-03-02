
"""
8. 곶감
* 오른쪽 회전, 왼쪽 회전 방식
* pop(0) : 0번째 인덱스가 없어지고 한칸씩 앞으로 당겨진다
* pop() : 가장 마지막 인덱스가 없어진다
# 앞자리를 빼고 뒷자리에 넣어서 한칸씩 배열을 오른쪽 이동 방법
a[h-1].append(a[h-1].pop(0))
"""

n= int(input())
a= [list(map(int, input().split())) for _ in range(n)]
m= int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    if t==0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0)) #왼쪽 회전
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop()) #오른쪽 회전
# 모래시계구하기
s=0
e=n-1
res=0
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i < n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1

print(res)
