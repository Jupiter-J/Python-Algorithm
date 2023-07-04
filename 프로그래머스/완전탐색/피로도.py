
"""
check부분을 생각하지 못함.
cnt로 카운트 하는 부분에서 에러
"""

cnt=0
def DFS(k, dungeons, ch, n):
    global cnt
    cnt = max(cnt, n) #전체16이 나오기 때문에 비교
    for i in range(len(dungeons)):
        if ch[i]==0 and k>=dungeons[i][0]:
            ch[i]=1
            DFS(k-dungeons[i][1], dungeons, ch, n+1)
            ch[i]=0

def solution(k, dungeons):
    global cnt
    cnt=0
    ch=[0]*(len(dungeons))
    DFS(k, dungeons, ch, 0)
    return cnt

print(solution(80, [[80,20],[50,40],[30,10]]))