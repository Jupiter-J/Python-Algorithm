

"""
1차시도
"""

# def solution(people, limit):
#     answer = 0
#     people.sort()
#     cnt = 0
#     sum_weight = 0
#
#     for weight in people:
#         if weight < limit:
#             sum_weight += weight
#             if sum_weight < limit:
#                 cnt += 1
#             elif sum_weight == limit:
#                 answer += 1
#                 cnt = 0
#                 sum_weight = 0
#             elif sum_weight > limit:
#                 answer += cnt
#                 answer += 1
#                 cnt = 0
#                 sum_weight = 0
#     if cnt != 0:
#         answer += cnt
#     return answer

from collections import deque


def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse=True))
    while len(people) > 1:
        if people[0] + people[-1] <= limit:  # 최대,최소값 보트추가
            answer += 1
            people.pop()  # 최소뺌
            people.popleft()  # 최댓값뺌
        else:
            answer += 1
            people.popleft()  # 최댓값빼기

    if people:  # 1명 남아있는 경우
        answer += 1

    return answer
