def solution(my_string):
    answer = []
    for x in my_string:
        if x.isdigit():
            answer.append(int(x))
    answer.sort()
    return answer


"""
리펙토링
"""
def solution(my_string):
    return sorted(int(x) for x in my_string if x.isdigit())



print(solution("hi12392"))