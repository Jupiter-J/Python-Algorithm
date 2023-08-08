

"""
8
5 3 4 0 2 1 1 0
"""

n = int(input())
arr = list(map(int, input().split()))
answer = [0]*n

for i in range(n):
    for j in range(n):
        # 0자리 확보,빈자리인지 확인
        if arr[i]==0 and answer[j]==0:
            answer[j]=i+1
            break
        elif answer[j]==0: # 내 앞공간의 0을 찾아서 위치 파악
            arr[i]-=1

print(' '.join(map(str, answer)))
