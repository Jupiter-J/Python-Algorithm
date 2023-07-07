
"""
BFS - 최소점프
같은값 제외
"""
# from collections import deque
# def BFS(home):
#     Q = deque()
#     Q.append(0)
#     ch=[0]*10001
#     ch[0]=1
#     L=0
#     while Q:
#         n = len(Q)
#         for i in range(n):
#             x = Q.popleft()
#             if x==home:
#                 return L
#             for nx in [x-1, x+1, x+5]:
#                 if nx>=0 and nx<10001 and ch[nx]==0:
#                     Q.append(nx)
#                     ch[nx]=1
#         L+=1
# def solution(home):
#     answer = BFS(home)
#     return answer
#
# print(solution(10))
# print(solution(14))
# print(solution(25))
# print(solution(24))
# print(solution(345))

"""
BFS - 검정색 영역 구하기
"""
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def BFS(x, y, board):
    Q = deque()
    Q.append([x, y])
    L = 0
    board[x][y]=0
    while Q:
        n = len(Q)
        for i in range(n):
            x, y = Q.popleft()
            for k in range(4):
                nx = x+dx[k]
                ny = y+dy[k]
                if nx>=0 and ny>=0 and nx<5 and ny<5 and board[nx][ny]==1:
                    Q.append([nx,ny])
                    board[nx][ny]=0
        L+=1
def solution(board):
    answer=0
    for i in range(5):
        for j in range(5):
            if board[i][j]==1:
                answer+=1
                BFS(i, j, board)
    return answer

print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))