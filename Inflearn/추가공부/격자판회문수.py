
"""
격자판회문수
2 4 1 5 3 2 6
3 5 1 8 7 1 7
8 3 2 7 1 3 8
6 1 2 3 2 1 1
1 3 1 3 5 3 2
1 1 2 5 6 5 2
1 2 2 2 2 1 5
"""
#
# board = [list(map(int, input().split())) for _ in range(7)]
# cnt=0
#
# #3중 for 문 사용
# for i in range(3): #열
#     for j in range(7):
#         #행 탐색
#         tmp=board[j][i:i+5]
#         if tmp==tmp[::-1]: #리버스
#             cnt+=1
#         #열 탐색/ 반만 나눠서
#         for k in range(2):
#             if board[i+k][j]!=board[i+5-k-1][j]:
#                 break
#         else:
#             cnt+=1
# print(cnt)

a = [list(map(int, input().split())) for _ in range(7)]
cnt=0

for i in range(3):
    for j in range(7):
        tmp=a[j][i:i+5]
        if tmp==tmp[::-1]:
            cnt+=1
        for k in range(2):
            if a[i+k][j]!=a[i+5-k-1][j]:
                break
        else:
            cnt+=1
print(cnt)



