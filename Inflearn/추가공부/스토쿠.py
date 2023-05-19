
"""
스토쿠
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

def check(x):
    for i in range(9):
        ch1=[0]*10
        ch2=[0]*10
        for j in range(9):
            ch1[a[i][j]]=1 #행 : 체크리스트 초기화
            ch2[a[j][i]]=1 #열
        if sum(ch1)!=9 or sum(ch2)!=9: # 둘중 하나라도 f면 f
            return False
    #3X3 그룹 탐색 - 4중 for문
    for i in range(3):
        for j in range(3):  #집합의 행열 탐색
            ch3=[0]*10
            for k in range(3): #집합의 원소 행열 탐색
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3)!=9:
                return False
    return True

a = [list(map(int, input().split())) for _ in range(9)]
ch = [0]*10

if check(a):
    print("YES")
else:
    print("NO")


def check(v):
    for i in range(9):
        ch1=[0]*10
        ch2=[0]*10
        for j in range(9):
            ch1[a[i][j]]=1
            ch2[a[j][i]]=1
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False

    for i in range(3):
        for j in range(3):
            ch3=[0]*10
            for x in range(3):
                for y in range(3):
                    ch3[a[i*3+x][j*3+y]]=1
            if sum(ch3)!=9:
                return False
    return True






a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")