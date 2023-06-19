
from collections import deque
# def solution(numbers, direction):
#     answer = []
#     if direction == "right":
#         answer.append(numbers.pop())
#         for x in numbers:
#             answer.append(x)
#     else:
#         a = numbers.pop(0)
#         for x in numbers:
#             answer.append(x)
#         answer.append(a)
#     return answer
# print(solution([4, 455, 6, 4, -1, 45, 6], "left"))


"""
리펙토링1
"""

# def solution(numbers, direction):
#     if direction == "right":
#         answer = [numbers[-1]] + numbers[:len(numbers)-1]
#     else:
#         answer = numbers[1:] + [numbers[0]]
#     return answer
# print(solution([4, 455, 6, 4, -1, 45, 6], "left"))

"""
리펙토링2
"""
from collections import deque
def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == "right":
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)