

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

from collections import deque
def solution(progresses, speeds):
    answer = []
    remain = deque()
    # 남은 일수
    for i in range(len(progresses)):
        tmp=0
        if (100-progresses[i])%speeds[i] == 0:
            tmp = (100 - progresses[i]) // speeds[i]
        else:
            tmp = (100 - progresses[i]) // speeds[i]+1
        remain.append(tmp)

    # 남은 일수 크기 비교
    ## 맨앞의 값이 뒤의 값보다 크면 , 계속 cnt 증가
    while remain:
        tmp = remain.popleft()
        cnt = 1
        while remain and tmp >= remain[0]:
            remain.popleft()
            cnt +=1
        answer.append(cnt)
    return answer

print(solution(progresses, speeds))