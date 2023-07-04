
"""
DFS - 팩토리얼
"""
# def DFS(n):
#     if n==1:
#         return 1
#     else:
#         return n*DFS(n-1)
#
# print(DFS(5))

"""
DFS - 피보나치 수열
"""
# def DFS(n):
#     answer = 1
#     if n==1 or n==2:
#         return 1
#     else:
#         return DFS(n-2)+DFS(n-1)
#     return answer
# print(DFS(5))

"""
DFS - 검정색 영역 구하기
"""

# nx = [-1, 0, 1, 0]
# ny = [0, 1, 0, -1]
# def DFS(board, i, j):
#     board[i][j] = 0
#     for k in range(4):
#         x = i+nx[k]
#         y = j+ny[k]
#         if x>=0 and y>=0 and x<5 and y<5 and board[x][y]==1:
#
#             DFS(board, x, y)
# def solution(board):
#     answer = 0
#     for i in range(5):
#         for j in range(5):
#             if board[i][j]==1:
#                 answer+=1
#                 DFS(board, i, j)
#     return answer
#
# print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
# print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
# print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
# print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))

"""
픽셀수 구하기
"""
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
def DFS(board, i, j):
    global cnt
    board[i][j]=0
    cnt +=1
    for k in range(4):
        nx = i+ dx[k]
        ny = j+ dy[k]
        if nx>=0 and ny>=0 and nx<5 and ny<5 and board[nx][ny]==1:
            DFS(board, nx, ny)
def solution(board):
    global cnt
    answer = []
    for i in range(5):
        for j in range(5):
            if board[i][j]==1:
                cnt = 0 #새로운 영역 초기화
                DFS(board, i, j)
                answer.append(cnt)
    return answer

print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
# print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
# print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
# print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))
