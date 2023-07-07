
def solution(before, after):
    cnt=0
    answer=0
    for x in before:
        if before.count(x)==after.count(x):
            cnt+=1
        if cnt == len(before):
            answer=1
    return answer


print(solution("olleh","hello"))