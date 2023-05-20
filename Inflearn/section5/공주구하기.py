
"""
공주 구하기
"""

# from collections import deque
# n, k = map(int, input().split())
# dq= list(range(1, n+1)) #원하는 범위값 리스트 초기화
# dq=deque(dq) #deque 자료구조 적용
#
# while dq:
#     for _ in range(k-1):
#         cur=dq.popleft() #앞의자료 pop
#         dq.append(cur)
#     dq.popleft() #k번째 사람은 빼기
#     if len(dq)==1:
#         print(dq[0])
#         dq.popleft() #break



from collections import deque
n, k = map(int, input().split())
a = list(range(1, n+1))
a = deque(a)

while a:
    for _ in range(k-1):
        cur = a.popleft()
        a.append(cur)
    a.popleft()
    if len(a)==1:
        print(a[0])
        break

