"""
최대 힙
- 최대힙 : 부모 노드값이 왼쪽자식과 오른 쪽 자식노드의 값보다 크게 트리를 구성하는 것
"""
# 기본적으로 최소힙을 사용한다

import heapq as hq
a=[]
while True:
    n = int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(-hq.heappop(a))
    else:
        hq.heappush(a, -n)

