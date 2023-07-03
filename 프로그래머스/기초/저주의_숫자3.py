


def solution(n):
    answer = []
    i=1
    while len(answer)!=n:
        if i%3!=0 and str(i).find('3')==-1:
            answer.append(i)
            i+=1
        else:
            i+=1
    return answer[-1]