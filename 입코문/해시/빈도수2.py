
"""
from collections import defaultdict
  nH = defaultdict(int)
defaultdict 숫자, 문자나 빈도수를 카운트 할때 유용하다
key 탐색 = key , value탐색 = nH[key]
"""

# from collections import defaultdict
# def solution(nums):
#     answer= -1
#     nH = defaultdict(int)
#     for x in nums:
#         nH[x] +=1
#     for key in nH:
#         if nH[key]==1:
#             answer = max(answer, key)
#     return answer


from collections import defaultdict, Counter
def solution(nums):
    answer= -1
    nH = Counter(nums) #Counter를 사용
    for key in nH:
        if nH[key]==1:
            answer = max(answer, key)
    return answer




print(solution([3, 9, 2, 12, 9, 12, 8, 7, 9, 12]))
# print(solution([2, 1, 3, 2, 1, 3, 4, 5, 4, 5, 6, 7, 6 ,7, 8, 8]))
# print(solution([23, 56, 11, 67, 120, 560, 812, 960, 560, 777, 888, 960]))
# print(solution([11, 73, 156, 789, 345, 156, 789, 345, 678, 555, 678]))
# print(solution([1, 3, 1, 5, 7, 2, 3, 1, 5]))