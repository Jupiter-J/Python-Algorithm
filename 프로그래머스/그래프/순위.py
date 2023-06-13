

results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
n = 5

from collections import defaultdict
def solution(n, results):
    answer = 0
    # 중복제거
    win_list = defaultdict(set)
    lose_list = defaultdict(set)

    # [4,3], [4,2] winner, loser로 넣기
    for winner, loser in results:
        win_list[winner].add(loser) # win_list = {4: {2, 3}, 3: {2}, 1: {2}, 2: {5}}
        lose_list[loser].add(winner) # lose_list = {3: {4}, 2: {1, 3, 4}, 5: {2}}

    # A > B 라면 A는 항상 B를 이긴다 { 1,3,4 > 2 > 5 }
    """
    i = 2일경우 lose_list[2] = {2: {1,3,4}}
    win_list[{1,2,3}] 각각의 value 값에 win_list[2: {5}]의 {5}를 추가시킨다  
    """
    for i in range(1, n+1):
        for loser in lose_list[i]: #
            win_list[loser].update(win_list[i])  # win_list = {4: {2, 3, 5}, 3: {2, 5}, 1: {2, 5}, 2: {5}, 5: set()}
        for winner in win_list[i]: #
            lose_list[winner].update(lose_list[i])  # lose_list = {3: {4}, 2: {1, 3, 4}, 5: {1, 2, 3, 4}, 1: set(), 4: set()}

    # 승+패 == (n-1) 확인
    for i in range(1, n+1):
        if len(win_list[i]) + len(lose_list[i]) == n-1:
            answer +=1
    return answer

print(solution(n,results))