


# def solution(s):
#     answer =0
#     num = list(s.split(" "))
#     for i in range(len(num)):
#         if num[i]!="Z":
#             answer+=int(num[i])
#         else:
#             answer-=int(num[i-1])
#     return answer

"""
리펙토링
"""
def solution(s):
    answer = []
    for x in s.split():
        if x != 'Z':
            answer.append(int(x))
        else:
            answer.pop()
    return sum(answer)

print(solution("10 20 30 40"))