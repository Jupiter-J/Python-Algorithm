
"""
5. 정다면체
4면체와 6면체의 모든 경우의 수를 이중 for문을 사용해서 구한다
리스트 정의 = [0]*N -> 0으로 초기화하면서 N길이만큼 만든다
리스트의 인덱스 자체가 최대값
"""
N,M = map(int, input().split())
cnt=[0]*(N+M+3)
max=0

for i in range(1, N+1):
    for j in range(1, M+1):
        cnt[i+j] += 1
for i in range(N+M+1):
    if cnt[i]>max:
        max=cnt[i]
for i in range(N+M+1):
    if cnt[i]==max:
        print(i, end=' ')
