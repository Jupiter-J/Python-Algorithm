emergency = [3, 76, 24]


# def solution(emergency):
#     answer = []
#     danger = sorted(emergency, reverse=True) # [76, 24, 3]
#     for x in emergency:
#         if danger.index(x):
#             answer.append(danger.index(x)+1)
#     answer.append(danger.index(emergency[-1]))
#     return answer
def solution(emergency):
    answer = []
    danger = sorted(emergency, reverse=True) # [76, 24, 3]

    for i in emergency:
        answer.append(danger.index(i)+1)

    return answer

print(solution(emergency))
