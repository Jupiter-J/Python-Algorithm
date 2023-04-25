

"""
k번째 약수 구하기 - 리스트로 위치 출력
"""

# import time
# start = time.time()
# import sys
# input = sys.stdin.readline
#
# n, k = map(int, input().split())
# answer = []
# # 약수 구하기
# for i in range(1, n+1):
#     if n%i==0:
#         answer.append(i)
# print(answer[2])
#
#
# print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간


"""
정답 for-else문
"""

n, k = map(int, input().split())
cnt=0
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break #k가 계속 만족되기 때문에 i가 자동출력됨
else: #break 없이 정상적으로 끝났을 경우 사용하는게 for-else문
    print(-1)
