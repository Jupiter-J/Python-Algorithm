
"""
응급실
5 2
60 50 70 80 90

* 튜플사용 a[0]=idx값, a[1]=value값
    *
* all : 인자로 받는 모든 요소가 True면 T
* any : 인자로 받는 요소중 하나라도 T가 있으면 T, 모두가 F일경우 F
"""

from collections import deque
n, m = map(int, input().split())
a = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
a = deque(a)
cnt=0

while True:
    cur=a.popleft()
    #cur[1]=뽑은 value ,x[1]=두번째 value 비교
    if any(cur[1]<x[1] for x in a):
          a.append(cur)
    else:
        cnt+=1
        if cur[0]==m:
            break
print(cnt)
