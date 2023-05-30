

"""
행렬 테두리 회전
x1(행), y1(열), x2, y2
row(열), columns(행), queries(위치값들 4개의 2차원 배열)
"""

"""
2. 회전함수 rotate()

"""
def rotate(x1, y1, x2, y2, tmp):
    first=tmp[x1][y1]
    min_value= first

    #왼쪽->아래 열고정 행 아래로+1
    for m in range(x1, x2):
        tmp[m][y1]=tmp[m+1][y1]
        min_value = min(min_value, tmp[m+1][y1])

    #아래->오른쪽  x행 고정
    for m in range(y1, y2):
        tmp[x2][m]=tmp[x2][m+1]
        min_value= min(min_value, tmp[x2][m+1])

    #(오)위->아래 y열 고정
    for m in range(x2, x1, -1):
        tmp[m][y2]=tmp[m-1][y2]
        min_value=min(min_value, tmp[m-1][y2])

    # 오+1칸
    for m in range(y2, y1+1, -1):
        tmp[x1][m] = tmp[x1][m-1]
        min_value = min(min_value, tmp[x1][m-1])

    tmp[x1][y1+1] = first
    return min_value

"""
1.
전체 배열의 크기를 받아 1씩 증가하는 행렬을 생성,
위치값을 받아서 회전해야 하는 부분을 추출하기 -> rotate 회전함수 만들기 
"""

# 1. 1씩 증가하는 행렬 생성
def solution(rows, columns, queries):
    tmp = [[(i)*columns+(j+1) for j in range(columns)] for i in range(rows)]
    result = []

# 2. 위치값을 받아 회전해야 하는 부분 추출
    # -1을 해야 실제 좌표에 도달
    for x1, y1, x2, y2 in queries:
        result.append(rotate(x1-1, y1-1, x2-1, y2-1, tmp))

    return result