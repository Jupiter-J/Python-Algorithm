def solution(rows, columns, queries):
    # 행렬 초기화
    answer = []
    board = [[columns * j + (i + 1) for i in range(columns)] for j in range(rows)]


    for query in queries:
        #위치값 받아오기 (-1)
        a, b, c, d = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1

        #가로 데이터
        row1, row2 = board[a][b:d], board[c][b + 1:d + 1]
        _min = min(row1 + row2)

        #세로 데이터
        for i in range(c, a, -1):
            board[i][d] = board[i - 1][d]
            if board[i][d] < _min: _min = board[i][d]

        for i in range(a, c):
            board[i][b] = board[i + 1][b]
            if board[i][b] < _min: _min = board[i][b]

        board[a][b + 1:d + 1], board[c][b:d] = row1, row2

        answer.append(_min)

    return answer