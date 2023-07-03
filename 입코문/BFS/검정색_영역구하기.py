# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# def DFS(x, y, board):
#     #최초1로 발견된 지점을 0으로 변경
#     board[x][y] = 0
#     #격자밖인지 판별/ 상화좌우가 1이면 DFS호출
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if nx >=0 and nx<5 and ny>=0 and ny<5 and board[nx][ny]==1:
#             DFS(nx, ny, board)
# def solution(board):
#     answer=0
#     for i in range(5):
#         for j in range(5):
#             #1이 발견되면 DFS 호출 (0,1)
#             if board[i][j]==1:
#                 answer += 1
#                 DFS(i, j, board)
#     return answer


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def DFS(i, j, board):
    board[i][j]=0

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if nx>=0 and ny>=0 and nx<5 and ny<5 and board[nx][ny]==1:
            DFS(nx, ny, board)
def solution(board):
    answer =0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==1:
                answer+=1
                DFS(i, j, board)

    return answer



print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
# print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
# print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
# print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))
