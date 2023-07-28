# def solution(weight, limit):
#     weight.sort()
#     answer=0
#     bus=0
#
#     for x in weight:
#         bus += x
#         if bus<limit:
#             answer+=1
#         else:
#             return answer
#     return answer

# def solution(weight, limit):
#     weight.sort()
#     bus=0
#     answer = 0
#     for x in weight:
#         if bus+x > limit:
#             break
#         bus += x
#         answer +=1
#     return answer
#
# print(solution([300, 100, 230, 120, 90, 150, 60], 700))
# print(solution([50, 90, 70, 120, 300, 200, 150, 180, 190], 1000))
# print(solution([70, 90, 100, 80, 60, 75, 73, 85, 120, 110, 200], 800))
# print(solution([50, 90, 100, 130, 140, 120, 130, 120, 150, 160, 140, 170], 1000))
# print(solution([100, 110, 50, 50, 60, 70, 50, 55, 57], 350))

# def solution(box, limit):
#     answer = 0
#     box.sort( key=lambda b:-b[1]) #value[1]를 내림차순 정렬
#     cnt=0
#
#     for idx, value in box:
#         if cnt+idx > limit:
#             limit -= cnt
#             answer += limit * value
#             break
#         cnt +=idx
#         answer += idx*value
#     return answer


# def solution(box, limit):
#     answer = 0
#     box.sort(key=lambda b:-b[1])
#
#     for x in box:
#         cnt = min(limit, x[0])
#         answer += cnt * x[1]
#         limit -= cnt
#
#         if limit == 0:
#             return answer
#
#
# print(solution([[2, 20], [2, 10], [3, 15], [2, 30]], 5))
# print(solution([[1, 50], [2, 20], [3, 30], [2, 31], [5, 25]], 10))
# print(solution([[3, 40], [5, 20], [5, 70], [1, 80], [5, 30], [3, 35]], 15))
# print(solution([[2, 70], [5, 100], [3, 90], [1, 95]], 8))
# print(solution([[80, 20], [50, 10], [70, 15], [70, 30], [80, 70], [90, 88], [70, 75]], 500))

"""
선긋기
"""
# def solution(m, nums):
#     answer = 0
#     n = len(nums)
#     nums.sort(key=lambda v:v[0])
#     start=end=i=0
#
#     while i<n:
#         #끝점 탐색
#         while i<n and nums[i][0]<=start:
#             end = max(end, nums[i][1]) #기존의 선 vs 새로운 끝선
#             i +=1 #현재값 증가
#         answer +=1 #while 끝난 후 선긋기 종료임으로 1증가
#
#         if end ==m: #종료 조건
#             return answer
#         start = end
#     return answer
#
#
# print(solution(12, [[5, 10], [1, 8], [0, 2], [0, 3], [2, 5], [2, 6], [10, 12], [7, 12]]))
# print(solution(15, [[1, 10], [0, 8], [0, 7], [0, 10], [12, 5], [0, 12], [8, 15], [5, 14]]))
# print(solution(20, [[3, 7], [5, 8], [15, 20], [0, 5], [7, 14], [3, 10], [0, 8], [13, 18], [5, 9]]))
# print(solution(30, [[5, 7], [3, 9], [2, 7], [0, 1], [0, 2], [0, 3], [19, 30], [8, 15], [7, 12], [13, 20]]))
# print(solution(25, [[10, 15], [15, 20], [5, 15], [3, 16], [0, 5], [0, 3], [12, 25]]))

"""
카드점수
"""


# def solution(nums, k):
#     answer= 0
#     n= len(nums) #7
#     for i in range(k+1): #0-7 1
#         sumN=0
#         """
#         좌, 우로 각각의 for문을 생성
#         - 좌: 앞 ~ 현재위치(i)까지 합
#         - 우: [전체횟수(n) - 주어진횟수(k) + 현재위치(i)] ~ 끝위치까지
#         """
#         for j in range(i): # 1
#             sumN += nums[j]
#         for j in range(n-k+i, n): # 7-4+1 (4-6)
#             sumN += nums[j]
#         print(sumN)
#
#     return answer
#
# print(solution([2, 3, 7, 1, 2, 1, 5], 4))
# print(solution([1, 2, 3, 5, 6, 7, 1, 3, 9], 5))
# print(solution([1, 30, 3, 5, 6, 7], 3))
# print(solution([1, 2, 15, 3, 6, 7, 8, 9], 5))
# print(solution([12, 5, 6, 12, 34, 35, 13, 3, 7, 8, 9], 7))

"""
방식2
"""
def solution(nums, k):
    total = sum(nums)
    m = len(nums)-k
    score = 0

    for i in range(m):
        score += nums[i]
    mins = score
    left = 0
    for right in range(m, len(nums)):
        score +=(nums[right] - nums[left])
        left +=1
        mins= min(mins, score)

    return total - mins


print(solution([2, 3, 7, 1, 2, 1, 5], 4))
# print(solution([1, 2, 3, 5, 6, 7, 1, 3, 9], 5))
# print(solution([1, 30, 3, 5, 6, 7], 3))
# print(solution([1, 2, 15, 3, 6, 7, 8, 9], 5))
# print(solution([12, 5, 6, 12, 34, 35, 13, 3, 7, 8, 9], 7))