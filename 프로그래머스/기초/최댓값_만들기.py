


def solution(numbers):
    answer = -2147000000
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            answer = max(answer, numbers[i]*numbers[j])
    return answer


print(solution([1, 2, 3, 4, 5]))

"""
리펙토링
굳이 이중 for문을 상용해 시간복잡도를 크게 만들지 않고 
내림차순/ 오름차순 정렬로 큰 값만 곱하게 하면 됨...
"""
def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]
