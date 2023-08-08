
"""
5 140
90 50 70 100 60
"""
from collections import deque
n, m = map(int, input().split())
people = list(map(int, input().split()))
people.sort()
people=deque(people)
answer=0
while people:
    if len(people)==1:
        answer+=1
        break
    if people[0]+ people[-1]>m:
        people.pop()
        answer+=1
    else:
        people.popleft()
        people.pop()
        answer+=1
print(answer)

# n, m = map(int, input().split())
# people = list(map(int, input().split()))
# people.sort()
# print(people)
# sumw = 0
# answer=0
# for x in people:
#     if sumw+x>m:
#         answer+=1
#         sumw=x
#     else:
#         sumw+=x
# if sumw!=0:
#     answer+=1
# print(answer)