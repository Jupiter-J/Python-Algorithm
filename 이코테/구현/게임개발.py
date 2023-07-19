
"""
게임 개발

dir = [0,1,2,3] 상하좌우
map_list = [0,1] 육지,바다

4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""
# 입력
n, m = map(int, input().split())
d = [[0]*m for _ in range(n)]
x, y, direction = map(int, input().split())
array=[]
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
d[x][y] = 1 #최초 시작값 방문체크하기

# 왼쪽 회전
def turn_left():
    global direction
    direction -=1 #-1을 줌으로써 왼쪽 회전이 됨
    if direction == -1: #음수일경우 [0,1,2,3]위치에서 제일 마지막 3으로 이동
        direction = 3

# 시뮬레이션
cnt=1
turn_time=0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 안가본곳[0]일 경우
    if d[nx][ny]==0 and array[nx][ny]==0:
        d[nx][ny]=1 #1체크
        x = nx
        y = ny
        cnt +=1 #카운트
        turn_time = 0
        continue
    else: #가본곳[1]일 경우
        turn_time +=1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny]==0:
            x = nx
            y = ny
        else:
            break
        turn_time=0
print(cnt)
