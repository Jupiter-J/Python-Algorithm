

"""
그리디 - 버스
"""
# def solution(weight,limit):
#     answer=0
#     people=0
#     weight.sort()
#
#     for x in weight:
#         if people<limit:
#             people+=x
#             answer+=1
#
#     return answer-1
#
# print(solution([300, 100, 230, 120, 90, 150, 60], 700))
# print(solution([50, 90, 70, 120, 300, 200, 150, 180, 190], 1000))
# print(solution([70, 90, 100, 80, 60, 75, 73, 85, 120, 110, 200], 800))
# print(solution([50, 90, 100, 130, 140, 120, 130, 120, 150, 160, 140, 170], 1000))
# print(solution([100, 110, 50, 50, 60, 70, 50, 55, 57], 350))

"""
최대 사과의 개수
"""

# def solution(box, limit):
#     answer=0
#     box.sort(key=lambda x:-x[1])
#     for x in box:
#         cnt = min(limit, x[0])
#         answer += (cnt*x[1])
#         limit -= cnt
#         if limit ==0:
#             break
#     return answer
#
#
# print(solution([[2, 20], [2, 10], [3, 15], [2, 30]], 5))
# # print(solution([[1, 50], [2, 20], [3, 30], [2, 31], [5, 25]], 10))
# # print(solution([[3, 40], [5, 20], [5, 70], [1, 80], [5, 30], [3, 35]], 15))
# # print(solution([[2, 70], [5, 100], [3, 90], [1, 95]], 8))
# # print(solution([[80, 20], [50, 10], [70, 15], [70, 30], [80, 70], [90, 88], [70, 75]], 500))

"""
선긋기
"""
def solution(m, nums):
    answer=0
    nums.sort(key=lambda x:x[0])
    start = end = i = 0
    m= len(nums)
    while i<m:
        while i <m and nums[i][0]<=start:
            end= max(end, nums[i][1])
            i+=1
        answer+=1
        if end ==m:
            return answer
    return answer

print(solution(12, [[5, 10], [1, 8], [0, 2], [0, 3], [2, 5], [2, 6], [10, 12], [7, 12]]))
# print(solution(15, [[1, 10], [0, 8], [0, 7], [0, 10], [12, 5], [0, 12], [8, 15], [5, 14]]))
# print(solution(20, [[3, 7], [5, 8], [15, 20], [0, 5], [7, 14], [3, 10], [0, 8], [13, 18], [5, 9]]))
# print(solution(30, [[5, 7], [3, 9], [2, 7], [0, 1], [0, 2], [0, 3], [19, 30], [8, 15], [7, 12], [13, 20]]))
# print(solution(25, [[10, 15], [15, 20], [5, 15], [3, 16], [0, 5], [0, 3], [12, 25]]))