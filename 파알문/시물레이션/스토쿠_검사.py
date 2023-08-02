
"""
1 4 3 6 2 8 5 7 9
5 7 2 1 3 9 4 6 8
9 8 6 7 5 4 2 3 1
3 9 1 5 4 2 7 8 6
4 6 8 9 1 7 3 5 2
7 2 5 8 6 3 9 1 4
2 3 7 4 8 1 6 9 5
6 1 9 2 7 5 8 4 3
8 5 4 3 9 6 1 2 7
"""



#3X3 탐색
#전체 행 탐색
#전체 열 탐색

def check(a):
    # 그래프 전체 행열 탐색
    for i in range(9):
        ch1=[0]*10 #행 체크
        ch2=[0]*10 #열 체크
        for j in range(9):
            ch1[a[i][j]]=1
            ch2[a[i][j]]=1
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False

    # 3X3 그룹 탐색
    for i in range(3):
        for j in range(3):
            ch3=[0]*10
            # 선택된 그룹의 갯수 탐색
            for k in range(3):
                for s in range(3):
                    # i*3[행] j*3[열] 점점 늘어남
                    # 늘어난 값을 기준으로 k[행], s[열]이 갯수 탐색
                    ch3[a[i*3+k][j*3+s]]=1
                if sum(ch3)!=9:
                    return False
    return True

graph = [list(map(int, input().split())) for _ in range(9)]
if check(graph):
    print("YES")
else:
    print("NO")