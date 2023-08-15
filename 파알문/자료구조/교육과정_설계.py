
"""
CBA
3
CBDAGE
FGCDAB
CTSBDEA
"""

# from collections import deque
# s = input()
# n = int(input())

# q = deque(s)
# for i in range(n):
#     subject = input()
#     for c in subject:
#         if c==q[0]:
#             q.popleft()
#     if len(q)==0:
#         print("#%d YES", i+1)
#     else:
#         print("#%d NO", i+1)

from collections import deque
s = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(s)
    for x in plan:
        if x in dq:
            if x!=dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq)==0:
            print("#%d YES" %(i+1))
        else:
            print("#d NO" %(i+1))
