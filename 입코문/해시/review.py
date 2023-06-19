
# from collections import defaultdict, Counter
# def solution(nums):
#     answer =-1
#     dF = Counter(nums)
#     for x in dF:
#         if dF[x]==1:
#             answer = max(answer, x)
#     return answer
#
#
# print(solution([3, 9, 2, 12, 9, 12, 8, 7, 9, 12]))
# print(solution([2, 1, 3, 2, 1, 3, 4, 5, 4, 5, 6, 7, 6 ,7, 8, 8]))
# print(solution([23, 56, 11, 67, 120, 560, 812, 960, 560, 777, 888, 960]))
# print(solution([11, 73, 156, 789, 345, 156, 789, 345, 678, 555, 678]))
# print(solution([1, 3, 1, 5, 7, 2, 3, 1, 5]))

"""
자기_분열수
"""
#from collections import defaultdict,Counter
# def solution(nums):
#     answer =2147000000
#     dF = Counter(nums)
#     for key in dF:
#         if dF[key]==key:
#             answer = min(answer, key)
#
#     return -1 if answer==2147000000 else answer
#
#
# print(solution([1, 2, 3, 1, 3, 3, 2, 4]))
# print(solution([1, 2, 3, 3, 3, 2, 4, 5, 5, 5]))
# print(solution([1, 1, 2, 5, 5, 5, 5, 5, 3, 3, 3, 3, 5]))
# print(solution([7, 6, 7, 7, 8, 8, 8, 8, 7, 5, 7, 7, 7, 8, 8]))
# print(solution([11, 12, 5, 5, 3, 11, 7, 12, 15, 12, 12, 11, 12, 12, 7, 8, 12, 11, 12, 7, 12, 5, 15, 20, 15, 12, 15, 12, 15, 14, 12]))

"""
팰린드롬_확인
"""
# from collections import defaultdict,Counter
# def solution(s):
#     answer =""
#     cnt=0
#     dF = Counter(s)
#     for key in dF:
#         if dF[key]%2!=0:
#             cnt+=1
#     return cnt<=1 #홀수 0개 거나 1개까지는 생성 가능
#
# print(solution("abacbaa"))
# print(solution("abaaceeffkckbaa"))
# print(solution("abcabbcc"))
# print(solution("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))
# print(solution("aabcefagcefbcabbcc"))

"""
팰린드롬 길이
"""

# from collections import defaultdict,Counter
#
# def solution(s):
#     answer=0
#     dF = Counter(s)
#     for key in dF:
#         if dF[key]%2!=0:
#             answer+=1
#     return len(s)-answer+1 if answer>0 else len(s)
#
# print(solution("abcbbbccaaeee"))

"""
두수의 합
"""
from collections import defaultdict, Counter
def solution(nums, target):
    answer = [0,0]
    dF = Counter(nums)
    for x in nums:
        y = target-x
        if y in dF:
            return sorted([x,y])
        dF[x]=1
    return answer

print(solution([3, 7, 2, 12, 9, 15, 8], 12))
# print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
# print(solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
# print(solution([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
# print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
# print(solution([7, 5, 12, 20], 15))
