

"""
재귀
"""
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end)//2
#     if array[mid] == target:
#         return mid
#     elif array[mid]> target:
#         return binary_search(array, target, start, mid-1)
#     else:
#         return binary_search(array, target, mid+1, end)
#
# n, target = list(map(int, input().split()))
# array = list(map(int, input().split()))
#
# result = binary_search(array, target , 0, n-1)
# if result == None:
#     print("존재x")
# else:
#     print(result+1)
#
# """
# 라이브러리
# """
# from bisect import bisect_left, bisect_right
# def count_by_range(a, left_value, right_value):
#     right_index = bisect_right(a, right_value)
#     left_index = bisect_left(a, left_value)
#     return right_index - left_index
# a = [1,2,3,3,3,3,5,5,8,9]
#
# print(count_by_range(a, 4,4)) #값이 4인 데이터 개수 출력
# print(count_by_range(a, -1, 3)) # 값이 [-1, 3] 범위에 있는 데이터 개수 출력


"""
입코테 : 예제
"""

def solution(nums, target):
    answer = 0
    lt = 0
    rt = len(nums)-1

    while lt <= rt:
        mid = len(nums) // 2
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            lt = mid+1
        else:
            rt = mid-1
    return -1





    return answer

print(solution([2, 5, 7, 8, 10, 15, 20, 24, 25, 30], 8))
print(solution([-3, 0, 2, 5, 8, 9, 12, 15], 0))
print(solution([-5, -2, -1, 3, 8, 9, 12, 17, 23], 2))
print(solution([3, 6, 9, 12, 17, 29, 33], 3))
print(solution([1, 2, 3, 4, 5, 7, 9, 11, 12, 15, 16, 17, 18], 18))

