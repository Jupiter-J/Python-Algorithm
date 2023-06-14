
hp = 23
# def solution(hp):
#     answer = 0
#     while hp > 0:
#         if hp%5 !=0:
#             answer += hp//5
#             hp = hp%5
#             if hp%3 !=0:
#                 answer += hp//3
#                 hp = hp%3
#             else:
#                 answer += hp//3
#                 hp = 0
#         else:
#             answer += hp//5
#             hp = 0
#         answer +=hp
#         hp=0
#     return answer
# print(solution(hp))

"""
리펙토링
"""

# def solution(hp):
#     answer = 0
#     ant = [5,3,1]
#
#     for x in ant:
#         if hp==0:
#             break
#         answer += hp//x
#         hp = hp%x
#     return answer


def solution(hp):
    return hp//5