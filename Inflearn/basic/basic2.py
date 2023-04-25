

"""
1 - N 홀수
"""
n = int(input())
# for i in range(1, n+1):
#     if i%2==1:
#         print(i)

"""
1-N 합 구하기
"""
answer=0
for j in range(1, n+1):
    answer+=j
print(answer) # 밖으로 빼면 for문이 끝나고 print실행

"""
1-N 약수 출력
"""
for k in range(1,n+1):
    if n%k==0:
        print(k, end=' ')

