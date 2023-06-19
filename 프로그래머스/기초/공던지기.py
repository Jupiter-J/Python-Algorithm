

def solution(numbers, k):
    answer = numbers[2*(k-1) % len(numbers)]
    return answer

print(solution([1, 2, 3, 4], 2))