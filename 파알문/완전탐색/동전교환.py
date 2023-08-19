
"""
3
1 2 5
15
"""
def DFS(v, sum):
    global answer
    if sum>m: # 거슬러 줄 금액보다 클 경우 종료시켜야함 !
        return
    if sum == m:
        answer = min(answer, v)
        return v
    else:
        for x in coin:
            DFS(v+1, sum+x)
            # DFS(v+1, sum) 1, 2, 5 번갈아가면서 사용하는 경우를 짰는데 O,X 여부는 맞지 않음

n = int(input())
coin = list(map(int, input().split()))
m = int(input())
answer = 1e9
coin.sort(reverse=True) # 큰 동전부터 적용시키기 위해 !
DFS(0,0)
print(answer)