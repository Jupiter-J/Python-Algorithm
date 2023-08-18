

"""
259 5
81
58
42
33
61
"""
# def DFS(v, sum):
#     global minw
#     if sum>c: #sum 값이 c보다 더 크면 종료
#         return
#     if v==n: #sum 값이 c보다 작으면서 전체경우
#         if sum>minw:
#             minw=sum
#     else:
#         DFS(v+1, sum+dogs[v])
#         DFS(v+1, sum)
#
# c, n = map(int, input().split())
# dogs = [int(input()) for _ in range(n)]
# minw = -1e9
# #가장 근접한 무게를 구해야함
# DFS(0, 0)
# print(minw)

def DFS(v, sum, tsum):
    global minw
    if sum+(total-tsum)<minw: # 추가
        return
    if sum>c: #sum 값이 c보다 더 크면 종료
        return
    if v==n: #sum 값이 c보다 작으면서 전체경우
        if sum>minw:
            minw=sum
    else:
        DFS(v+1, sum+dogs[v], tsum+dogs[v])
        DFS(v+1, sum, tsum+dogs[v])

c, n = map(int, input().split())
dogs = [int(input()) for _ in range(n)]
minw = -1e9
total = sum(dogs)
#가장 근접한 무게를 구해야함
DFS(0, 0, 0)
print(minw)