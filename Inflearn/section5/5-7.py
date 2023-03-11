
"""
교육과정 설계

break 생각하기, 결과에 따른 답 전부 생각하기
"""

# from collections import deque
# subject = input()
# n = int(input())
#
# for i in range(n):
#     plan = input()
#     dq = deque(subject)
#     for x in plan: #시간표 과목 전체 탐색 X
#         if x in dq: #전필에 있는지 확인
#             if x != dq.popleft(): #순서가 맞는지 확인
#                 print("#%d NO" %(i+1))
#                 break
#     else:
#         if len(dq)==0:
#             print("#%d YES" %(i+1))
#         else:
#             print("#%d NO" % (i + 1))



from collections import deque
require = input()
n = int(input())

for i in range(n):
    plan = input()
    deq = deque(require)
    for x in plan:
        if x in deq:
            if x != deq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(deq)==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))

