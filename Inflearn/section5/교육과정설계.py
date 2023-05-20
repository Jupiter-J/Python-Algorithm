
"""
교육과정 설계
"""

from collections import deque
a= input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(a)
    for x in plan:
        if x in dq:
            if x!=dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq)==0:
            print("#%d YES" %(i+1))
