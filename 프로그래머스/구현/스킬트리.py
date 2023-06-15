def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        s = ""
        for check in tree: #BACDE 회전
            if check in skill: #알파벳 하나씩[BACDE] skill[CBD]에 있는지 확인
                s += check     #있다면 해당 문자열을 s에 추가

        if skill[:len(s)] == s:
            answer += 1
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))