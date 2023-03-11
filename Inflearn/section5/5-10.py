
"""
최소힙
최소힙 : 부모 노드 값이 왼쪽 자식과 오른쪽 자식 노드의 값보다 작게 트리를 구성 하는 것
"""

import heapq as hq
a=[]
while True:
    n = int(input())
    if n==-1:
        break
    if n==0: #쵯솟값 출력
        if len(a)==0: #비어 있을경우
            print(-1)
        else:
            print(hq.heappop(a)) #루트 노드값(최솟값 출력)
    else:
        hq.heappush(a, n) #a라는 리스트에 n값을 최소힙의 형태로 넣는다