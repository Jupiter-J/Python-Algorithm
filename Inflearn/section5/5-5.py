"""
5-5. 큐
FIFO - Firs In First Out : 먼저 온사람이 먼저 빠져나간다
- push() : 맨뒤에 집어넣음
- pop() : 맨 앞부분 꺼내고 반환
- size(): 큐의 길이 반환
- empty(): 큐가 비어있는지 유무 반환
- front(): 큐의 맨앞 부분 원소 반환
- back(): 큐의 맨뒷부분 원소 반환

deque 자료구조
"""

# from collections import deque
# n, k =map(int, input().split())
# dq=list(range(1,n+1))
# dq=deque(dq)
#
# while dq:
#     for _ in range(k-1):
#         cur=dq.popleft() #가장 앞자료가 없어짐
#         dq.append(cur) #없앤 자료를 다시 뒤로 넣기
#     dq.popleft() # for 회전 끝나고 k번째 사람은 없앤다
#     if len(dq)==1:
#         print(dq[0])
#         dq.popleft()


from collections import deque
n, k= map(int, input().split())
prince = list(range(1,n+1))
prince = deque(prince)

while prince:
    for _ in range(k-1):
        res = prince.popleft()
        prince.append(res)
    prince.popleft()
    if len(prince)==1:
        print(prince[0])
        prince.popleft()
