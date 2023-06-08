


def solution(triangle):
    for i in range(1, len(triangle)): #삼격형의 길이만큼
        for j in range(i+1): # 주란의 인덱스
            if j ==0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    return max(triangle[-1])


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
for i in range(1, len(triangle)):  # 삼격형의 길이만큼
    for j in range(i + 1):  # 줄 안의 인덱스
        if j == 0:
            triangle[i][j] += triangle[i - 1][j]
        elif j == i:
            triangle[i][j] += triangle[i - 1][-1]
        else:
            triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

print(max(triangle[-1]))
