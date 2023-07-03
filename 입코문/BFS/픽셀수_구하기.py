

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
black=0
def DFS(i, j, board):
    global black
    board[i][j]=0
    black+=1
    for k in range(4):
        nx = i+dx[k]
        ny = j+dy[k]
        if nx>=0 and ny>=0 and nx<5 and ny<5 and board[nx][ny]==1:
            DFS(nx, ny, board)
def solution(board):
    global black
    answer=[]
    for i in range(5):
        for j in range(5):
            if board[i][j]==1:
                black=0
                DFS(i, j, board)
                #끝나는 지점
                answer.append(black)
    return answer


print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
# print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
# print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
# print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))
