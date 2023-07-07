def solution(i, j, k):
    answer = 0

    for c in range(i, j + 1):
        for find in str(c):
            if str(k) == find:
                answer += 1
    return answer

print(solution(1,13,1))

"""
리펙토링
"""
def solution(i, j, k):
    return sum(str(x).count(str(k)) for x in range(i, j+1))