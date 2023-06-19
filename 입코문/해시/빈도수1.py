"""
enumerate를 써야하나 고민했는데 값 자체를 인덱스로 비교하는 방식,
max로 비교하여 다시 저장하는 형태를 기억해두자
"""
def solution(nums):
    answer = -1 #없으면 반환을 위해
    save =[0]*1001
    for i in nums:
        save[i]+=1

    for x in range(1, 1001):
        if save[x] ==1:
            answer = max(answer, x) #비교하고 저장
    return answer

print(solution([3, 9, 2, 12, 9, 12, 8, 7, 9, 12]))
# print(solution([2, 1, 3, 2, 1, 3, 4, 5, 4, 5, 6, 7, 6 ,7, 8, 8]))
# print(solution([23, 56, 11, 67, 120, 560, 812, 960, 560, 777, 888, 960]))
# print(solution([11, 73, 156, 789, 345, 156, 789, 345, 678, 555, 678]))
# print(solution([1, 3, 1, 5, 7, 2, 3, 1, 5]))