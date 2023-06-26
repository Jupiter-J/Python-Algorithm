
"""
주어진 제한 길이가 1억개 이상의 큰수일 경우
선형탐색이 아닌 이분탐색을 떠올려야함

이분탐색 - 크거나 같은것/lower bound
"""
def solution(nums, weight):
    lt=0
    rt= len(nums)
    while lt<rt:
        mid = (lt+rt)//2
        if weight > nums[mid]:
            lt = mid+1
        else:
            rt = mid
    return -1 if rt==len(nums) else rt #해당값이 없을경우 rt초기값이 나오면 -1반환


"""
라이브러리
"""
from bisect import bisect_left
def solution(nums, weight):
    answer = bisect_left(nums, weight)
    return -1 if answer ==len(nums) else answer


print(solution([100, 120, 150, 160, 165, 170, 175, 180, 190, 200], 170))
# print(solution([200, 250, 260, 265, 275, 290, 300, 325, 350, 370], 270))
# print(solution([50, 55, 60, 65, 70, 80, 80, 80, 80, 90, 90, 90], 80))
# print(solution([20, 30, 40, 50, 60, 70], 90))
# print(solution([10, 30, 50, 70, 80, 90, 100, 110, 120], 115))
