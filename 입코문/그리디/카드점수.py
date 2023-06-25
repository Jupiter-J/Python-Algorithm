
"""
효율성, O(N), 슬라이싱
"""
def solution(nums,k):
    total = sum(nums)
    m = len(nums) - k
    score = 0
    for i in range(m):
        score += nums[i]
    minS=score
    left = 0
    for right in range(m, len(nums)):
        score += (nums[right] - nums[left])
        left +=1
        minS = min(minS, score)
    return total - minS

"""
정확성 , N^2, 완전탐색
"""
def solution(nums,k):
    answer=0
    n = len(nums)
    for i in range(k+1):
        sumN = 0
        for j in range(i): #앞문자1 합
            sumN += nums[j]
        for j in range(n-k+i, n): #뒤쪽3 합
            sumN += nums[j]
        answer = max(answer, sumN)
    return answer

print(solution([2, 3, 7, 1, 2, 1, 5], 4))
print(solution([1, 2, 3, 5, 6, 7, 1, 3, 9], 5))
# print(solution([1, 30, 3, 5, 6, 7], 3))
# print(solution([1, 2, 15, 3, 6, 7, 8, 9], 5))
# print(solution([12, 5, 6, 12, 34, 35, 13, 3, 7, 8, 9], 7))