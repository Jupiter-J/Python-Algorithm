

def solution(N, number):
    answer = -1
    if number== N:
        return 1
    # 전체 크기 : 최솟값이 8보다 크면 -1 return [set(), set(), set(), set(), set(), set(), set(), set()]
    li = [set() for i in range(8)]

    # set에 N값 경우의 수 모두 집어 넣기 [{5}, {55}, {555}, {5555}, {55555}, {555555}, {5555555}, {55555555}]
    for i in range(len(li)):
        li[i].add(int(str(N)*(i+1)))

    # 연산자 계산 // 0번째는 연산자가 필요 없음
    for i in range(1,8): #1 /2
        for j in range(i):  #0
            for op1 in li[j]: #li[0]={5}
                for op2 in li[i-j-1]: #li[1-0-1]={5}
                    li[i].add(op1 + op2) #{5}+{5}
                    li[i].add(op1 - op2) #{5}-{5}
                    li[i].add(op1 * op2) #{5}*{5}
                    if op2 != 0: #뒤의 숫자가 0이면 나눗셈 불가능
                        li[i].add(op1//op2)
    #찾는 숫자가 현재 op에 있다면 +1 (i=0일때 5가 하나씩 이미 들어가있기 때문에)
        if number in li[i]:
            answer = i+1
            break
    print(li)
    return answer

print(solution(5, 12))