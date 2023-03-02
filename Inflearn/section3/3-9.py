

"""
9. 봉우리
all() : all()안의 조건, 요소가 모두 True일때
"""

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
# 가장 자리 0 초기화
a.insert(0, [0]*n) #상단
a.append([0]*n) #하단
for x in a: #각행 오른쪽, 왼쪽
    x.insert(0,0)
    x.append(0)

# 상하좌우 팀지 방법
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

cnt=0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)
