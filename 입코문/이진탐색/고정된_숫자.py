
"""
백만~1억일 경우 이분탐색
O(nlogn) >O(N) > O(logN)
이분검색을 할경우는 logN

절반을 날려야 하기 때문에 조건을 잘 따지기
"""
def solution(nums):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == mid:
            return nums[mid]
        if nums[mid] < mid:
            left = mid +1
        else:
            right = mid -1
    return -1

print(solution([-3, -2, 0, 1, 3, 5, 8, 9, 12]))
# print(solution([-10, -5, -2, 3, 4, 6, 7, 8]))
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(solution([-5, -3, 0, 1, 2, 3, 4, 7]))
# print(solution([0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))