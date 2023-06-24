
"""
경계선 밖 판별 :: 4방향 나보다 작거나 같은게 존재하냐 -> 웅덩이x
"""
# def solution(nums):
#     n = len(nums)
#     answer=0
#     dx = [-1, 0, 1, 0] #행
#     dy = [0, 1, 0, -1] #열
#
#     for i in range(n):
#         for j in range(n):
#             #현재 격자지점에서 판별
#             flag = True #먼저 웅덩이라고 가정 True
#             for k in range(4):
#                 nx = i+dx[k]
#                 ny = j+dy[k]
#                 if nx >=0 and nx<n and ny>=0 and ny<n and nums[i][j] >= nums[nx][ny]:
#                     #nus[i][j] 현재지점 -같은값이 있음 안됨
#                     flag = False
#                     break
#             if flag == True:
#                 answer += 1
#     return answer

def solution(nums):
    answer=0
    s = len(nums)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(s):
        for j in range(s):
            flag = True
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                # 웅덩이가 아닐경우
                if nx>=0 and nx<s and ny>=0 and ny<s and nums[nx][ny]<=nums[i][j]:
                    flag = False
                    break
            if flag==True:
                answer+=1
    return answer

print(solution([[10, 20, 50, 30, 20], [20, 30, 50, 70, 90], [10, 15, 25, 80, 35], [25, 35, 40, 55, 80], [30, 20, 35, 40, 90]]))
# print(solution([[80, 25, 10, 65, 100], [20, 10, 32, 70, 33], [45, 10, 88, 9, 90], [10, 35, 10, 55, 66], [10, 84, 65, 88, 99]]))
# print(solution([[33, 22, 55, 65, 55], [55, 88, 99, 12, 19], [18, 33, 25, 57, 77], [46, 78, 54, 55, 99], [33, 25, 47, 85, 17]]))