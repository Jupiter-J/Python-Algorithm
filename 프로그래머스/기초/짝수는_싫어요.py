

"""
나의 풀이
"""
def solution(n):
    answer = [1]
    for i in range(2, n+1):
        if i%2 !=0:
            answer.append(i)
    return answer


"""
다른 풀이
"""
def solution(n):
    return [i for i in range(1, n+1, 2)]