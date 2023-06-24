num=[1,2,3,4,5]


def solution(nums):
    dx = [-1, 0, 1, 0] #행
    dy = [0, 1, 0, -1] #열

    for i in range(5):
        for j in range(5):
            for k in range(4): #4방향
                nx = i + dx[k]
                ny = j + dy[k]
                #테두리 - nx,ny 음수가 되면 안됨/ 격자밖 nx, ny 길이 미만으로
                if nx>=0 and nx <5 and ny >=0 and ny<5:
                    if nums[nx][ny] <= nums[i][j]:
                        #nums[nx][ny]는 nums[i][j](현재위치)의 4방향이다
                        #대각선일 경우 dx, dy에 대각선 위치를 추가
                        flag = False
    return nums


print(solution([[10, 20, 50, 30, 20], [20, 30, 50, 70, 90], [10, 15, 25, 80, 35], [25, 35, 40, 55, 80], [30, 20, 35, 40, 90]]))
