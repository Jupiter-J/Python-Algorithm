
def solution(nums):
    answer=0
    compare=0
    for x in nums:
        if x==1:
            compare+=1
        else:
            answer = max(answer, compare)
            compare=0
    answer = max(answer,compare)
    return answer

print(solution([1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]))
print(solution([0, 0, 1, 0, 1, 0, 0]))
print(solution([1, 1, 1, 1, 1]))
print(solution([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]))
