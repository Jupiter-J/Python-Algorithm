"""
1회시도
- case2 에러
- set먼저 -> 리스트변환 -> 오름차순
"""
def solution(numbers):
    answer = []
    answer = set(answer)
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.add(numbers[i]+numbers[j])
    answer = list(answer)
    answer.sort
    return answer


"""
2회시도
- 문법오류()였다
"""
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
    answer = set(answer)
    answer = list(answer)
    answer.sort()
    return answer


"""
리펙토링
"""
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
    return sorted(list(set(answer)))