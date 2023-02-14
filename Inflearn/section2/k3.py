
# N, K = map(int, input().split())
# a = list(map(int, input().split()))
# res=set()
#
# for i in range(N):
#     for j in range(i+1, N):
#         for m in range(j+1, N):
#             res.add(a[i]+a[j]+a[m])
# res=list(res) #set에는 sort기능이 없음으로 list화 시킨다
# res.sort(reverse=True)
# print(res[K-1])

"""
3. K번째 큰 수
중복 제거 : set() - 집합 자료형, 중복을 허용 하지 않음, 순서가 없다 
- add() : 값 추가
- update() : 여러개 추가
- remove() : 특정 값 제거 
set() 순서 정렬 : list() 변경 후 ,sort() 사용하기
내림차 순 정렬 : sort(reverse=True)
3중 for 문 : i/n, j/i+1~n, m/j+1~n 하나씩 뒤로 범위를 잡아서 겹치지 않게 회전  
"""

N, K = map(int, input().split())
a = list(map(int, input().split()))
res = set()

for i in range(N):
    for j in range(i+1, N):
        for m in range(j+1, N):
            res.add(a[i]+a[j]+a[m])
res = list(res)
res.sort(reverse=True)
print(res[K-1])
