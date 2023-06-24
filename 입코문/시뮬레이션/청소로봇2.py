
def solution(n, moves):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    c = ['U','R','D','L']
    x=y=0

    for k in moves: #RRRDDDUUUUUUL
            for m in range(4):#0~4
                if k == c[m]:
                    nx = x+dx[m]
                    ny = y+dy[m]
            if nx<0 or nx >=n or ny <0 or ny>=n: #격자판 밖의 경우
                continue #스킵
            x = nx
            y = ny

    return [x,y]

print(solution(5,'RRRDDDUUUUUUL'))
# print(solution(7,'DDDRRRDDLL'))
# print(solution(5,'RRRRRDDDDDU'))
# print(solution(6,'RRRRDDDRRDDLLUU'))


