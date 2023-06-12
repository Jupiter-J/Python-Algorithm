# def solution(nums, target):
#     answer=[]
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if target== nums[i]+nums[j]:
#                 answer.append(nums[i])
#                 answer.append(nums[j])
#     if len(answer)==0:
#         answer=[0,0]
#     answer.sort()
#     return answer

"""
정답코드 - 리펙토링
"""
def solution(nums, target):
    answer=[0]*2 #처음부터 0,0 초기화를 해서 코드를 줄임
    for i in range(len(nums)-1):  #마지막은 겹치니까 굳이 필요 없다
        for j in range(i+1, len(nums)):
            if target== nums[i]+nums[j]:
                return sorted([nums[i], nums[j]]) #sorted와 동시에 리턴 (굳이 answer 들어갈 필요 없음)
    return answer

print(solution([7, 9, 2, 13, 3, 15, 8, 11], 12))
print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
print(solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
print(solution([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
print(solution([7, 5, 12, 20], 15))