
"""
두 리스트 합치기
시간복잡도
이미 정렬이 되어있는 것을 nlogn으로 하는 방법

3
1 3 5
5
2 3 6 7 9
"""

# n = int(input())
# n_list = list(map(int, input().split()))
# m = int(input())
# m_list = list(map(int, input().split()))
#
# res = n_list + m_list
# res.sort()
# for x in res:
#     print(x, end=' ')

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

p1=p2=0
res=[]

while p1<n and p2<m:
    if n_list[p1] <= m_list[p2]:
        res.append(n_list[p1])
        p1+=1
    else:
        res.append(m_list[p2])
        p2+=1
if p1<n:
    res=res+n_list[p1:]
if p2<m:
    res=res+m_list[p2:]

print(res, end=' ')