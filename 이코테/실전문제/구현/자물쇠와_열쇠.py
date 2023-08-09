
def match(graph, key, rot, x, y):
    n = len(key)
    #key 90회전
    for i in range(n):
        for j in range(n):
            #회전이 없는 경우
            if rot == 0:
                # key값을 더해 안맞는 경우 누적합으로 겹치는 부분을 판별 (최종 전부 1인지 확인을 위해서)
                graph[x + i][y + j] += key[i][j]
            elif rot == 1: #시계방향으로 90도
                graph[x + i][y + j] += key[n-1 -j][i]
            elif rot == 2: #180도
                graph[x + i][y + j] += key[n-1 -i][n-1 -j]
            else:
                graph[x + i][y + j] += key[j][n-1 -i]

# lock이 모두 1인지 확인
def check(graph, temp, n):
    for i in range(n):
        for j in range(n):
            if graph[temp + i][temp +j] != 1:
                return False
    return True

def solution(key, lock):
    answer = True
    temp = len(key)-1 #key와 lock의 떨어진 거리

    #key위치 x:행, y:열
    for x in range(temp+len(lock)):
        for y in range(temp + len(lock)):
            #key 4방향 회전
            for rot in range(4):
                # 전체 도면 생성 (key_max=20, lock_max=20 20X3-2 : 1개씩 걸쳐 있어야 함으로)
                graph = [[0 for _ in range(58)] for _ in range(58)]
                # lock 복사
                for i in range(len(lock)):
                    for j in range(len(lock)):
                        #lock기준 temp길이만큼 떨어진곳에 복사
                        graph[temp+i][temp+j]=lock[i][j]
                match(graph, key, rot, x, y)

                #맞은 경우 lock 영역이 모두 1인지 확인
                if check(graph, temp, len(lock)):
                    return True
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))