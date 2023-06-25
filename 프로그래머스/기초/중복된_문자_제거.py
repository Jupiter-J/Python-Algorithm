
def solution(my_string):
    answer = []
    arr = list(my_string)

    for x in arr:
        if x not in answer:
            answer.append(x)
    return "".join(answer)

"""
리펙토링
"""
def solution(my_string):
    answer = ''
    for x in my_string:
        if x not in answer:
            answer+=x
    return answer

print(solution("people"))
