
"""
주어진 크기 100,000 = 효율성범위 (O(N) ~ O(nlogn)) // 정확성 N^2
1. 정확성 n^2 방식
"""
# def solution(nums):
#     minN=2147000000
#     answer=[]
#
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             minN= min(minN, abs(nums[i]-nums[j]))
#
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             tmp = abs(nums[i] - nums[j])
#             if tmp == minN:
#                 answer.append(sorted([nums[i], nums[j]]))
#     return answer

"""
2. 효율성 nlogn방식
- (전체탐색을 할 필요없이) 오름차순 정렬을 할 경우 시간 복잡도를 줄이는데 효과적이다 
- 이진검색이 대표적 -> 반복문을 한번만 사용하여 선형탐색을한다 
"""
def solution(nums):
    answer=[]
    n = len(nums)
    minN = 1000000000
    ## O(nlogn)
    nums.sort()
    #앞[1]에서부터 앞뒤 비교보다 [1]에서부터 앞을 하나씩 빼서 비교하면 됨
    ## O(N)
    for i in range(1, n):
        diff = nums[i] - nums[i-1]
        minN = min(minN, diff)

    ## O(N)
    for i in range(1, n):
        diff = nums[i] - nums[i-1]
        if diff == minN:
            answer.append([nums[i-1], nums[i]])
    return answer

print(solution([3, 8, 1, 5, 12]))
print(solution([2, 1, 3, 5, 4]))
print(solution([5, 10, 15, 20, 25, 11]))
print(solution([2, 4, 3, 1, 5, 7, 8, 12, 13, 15, 23]))
print(solution([100, 200, 300, 400, 120, 130, 135, 132, 121]))
