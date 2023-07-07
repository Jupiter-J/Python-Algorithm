

"""
이진탐색 - 트럭찾기
"""
# def solution(nums, weight):
#     answer = -1
#     for x in nums:
#         if x==weight or x>=weight:
#             return nums.index(x)
#     return answer

"""
이진탐색 = lowbound
"""
# def solution(nums, weight):
#     lt=0
#     rt=len(nums)
#     while lt<rt:
#         mid = (lt+rt)//2
#         if nums[mid]>weight:
#             rt=mid
#         else:
#             lt=mid+1
#     return -1 if rt == len(nums) else rt

"""
row bound search
"""
from bisect import bisect_left
# def solution(nums, weight):
#     answer = bisect_left(nums, weight)
#
#     return -1 if answer == len(nums) else answer
#
#
# print(solution([100, 120, 150, 160, 165, 170, 175, 180, 190, 200], 170))
# print(solution([200, 250, 260, 265, 275, 290, 300, 325, 350, 370], 270))
# print(solution([50, 55, 60, 65, 70, 80, 80, 80, 80, 90, 90, 90], 80))
# print(solution([20, 30, 40, 50, 60, 70], 90))
# print(solution([10, 30, 50, 70, 80, 90, 100, 110, 120], 115))


"""
고정된 숫자
"""
# def solution(nums):
#     answer = -1
#     for x in nums:
#         if x==nums.index(x):
#             return x
#     return answer

"""
효율성
nlogn > n > logn(이분탐색)
"""




# print(solution([-3, -2, 0, 1, 3, 5, 8, 9, 12]))
# print(solution([-10, -5, -2, 3, 4, 6, 7, 8]))
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(solution([-5, -3, 0, 1, 2, 3, 4, 7]))
# print(solution([0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))