
"""
내코드 N^2
"""
# def solution(nums, target):
#     answer = [0,0]
#     nums.sort()
#
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             tmp=nums[i]+nums[j]
#             if tmp == target:
#                 answer[0] = nums[i]
#                 answer[1] = nums[j]
#                 break
#     return answer

"""
1. 투 포인터 nlogn
양끝쪽에서 값을 좁혀감
- target값 보다 클 경우 가장 큰 쪽으로 정렬된 right를 줄인다
- target값 보다 작을 경우 가장 작은쪽인 left값을 키운다
"""
def solution(nums, target):
    answer = [0,0]
    nums.sort()
    rt = len(nums) - 1
    lt = 0
    for i in range(len(nums)):
        if nums[rt]+nums[lt]>target:
            rt-=1
        elif nums[rt]+nums[lt]<target:
            lt+=1
        elif nums[rt]+nums[lt]==target:
            answer[0]=nums[lt]
            answer[1]=nums[rt]
            break
    return answer

print(solution([3, 7, 2, 12, 9, 15, 8, 11], 12))
print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
print(solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
print(solution([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
print(solution([7, 5, 12, 20], 15))