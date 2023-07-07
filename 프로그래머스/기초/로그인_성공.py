def solution(id_pw, db):
    for x, y in db:
        if x == id_pw[0]:
            if y == id_pw[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"



print(solution(["meosseugi", "1234"],[["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))