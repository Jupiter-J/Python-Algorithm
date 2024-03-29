
"""
O(n^2) - n제한이 만일 경우
"""
# def solution(nums, target):
#     answer = [0,0]
#     for i in range(len(nums)-1):
#         for j in range(i+1, len(nums)):
#             if target == nums[i]+nums[j]:
#                 answer= [nums[i],nums[j]]
#     answer.sort()
#     return answer


"""
O(n) - n제한이 20만일 경우 타임리밋 걸림 
"""
from collections import defaultdict
def solution(nums, target):
    answer = [0,0]
    nH = defaultdict(int)
    for x in nums:
        y = target - x
        if y in nH: #O(1)
            return sorted([x,y])
        nH[x]=1
    return answer


print(solution([3, 7, 2, 12, 9, 15, 8], 12))
# print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
# print(solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
# print(solution([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
# print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
# print(solution([7, 5, 12, 20], 15))

