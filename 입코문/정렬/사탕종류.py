
"""
내코드
"""
# def solution(nums):
#     answer =0
#     can = len(nums)/2
#     nums = len(set(nums))
#     answer = min(can, nums)
#     return int(answer)

"""
정답코드 O(nlogn)
"""
def solution(nums):
    answer =1
    n = len(nums)
    nums.sort()
    for x in range(1, n):
        if nums[x-1] != nums[x]:
            answer+=1
    return answer if answer<n//2 else n//2

print(solution([2, 1, 1, 3, 2, 3, 1, 2]))
print(solution([1, 3, 5, 7, 2, 3, 7, 5, 3, 2, 5, 7, 9, 12]))
print(solution([5, 5, 5, 5, 5, 5]))
print(solution([12, 23, 11, 3, 5, 23, 23, 23, 23, 23, 23, 23]))
print(solution([100, 200, 300, 400, 500, 600, 700, 800]))
