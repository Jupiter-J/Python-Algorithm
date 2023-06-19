
"""
자기 분열수
"""

# from collections import defaultdict, Counter
# def solution(nums):
#     answer = 2147000000
#     dF = Counter(nums)
#     for key in dF:
#         if key == dF[key]:
#             answer = min(answer, key)
#     return -1 if answer == 2147000000 else answer


from collections import defaultdict, Counter
def solution(nums):
    answer = 2147000000
    dF = defaultdict(int)
    for x in nums:
        dF[x]+=1
    for key in dF:
        if key == dF[key]:
            answer = min(answer, key)
    return -1 if answer == 2147000000 else answer




print(solution([1, 2, 3, 1, 3, 3, 2, 4]))
print(solution([1, 2, 3, 3, 3, 2, 4, 5, 5, 5]))
print(solution([1, 1, 2, 5, 5, 5, 5, 5, 3, 3, 3, 3, 5]))
print(solution([7, 6, 7, 7, 8, 8, 8, 8, 7, 5, 7, 7, 7, 8, 8]))
print(solution([11, 12, 5, 5, 3, 11, 7, 12, 15, 12, 12, 11, 12, 12, 7, 8, 12, 11, 12, 7, 12, 5, 15, 20, 15, 12, 15, 12, 15, 14, 12]))