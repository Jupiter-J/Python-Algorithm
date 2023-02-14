
# N, K = map(int, input().split())
# cnt=0
#
# for i in range(1,N+1):
#     if N%i==0:
#         cnt+=1
#     if cnt==K:
#         print(i)
#         break
# else:
#     print(-1)


"""
[K번째 약수]
map(int, input().split())
    map () : 줄바꿈이 아닌 일렬로 받기 위해 사용
    int : 내장함수, 정수화 시킨다
    split(): 분리
for-else 문: 정상적으로 for문이 돌지 않았을 경우      
"""

C,J = map(int, input().split())
cnt =0
for i in range(1, C+1):
    if C%i==0:
        cnt+=1
    if J==cnt:
        print(i)
        break
else:
    print(-1)