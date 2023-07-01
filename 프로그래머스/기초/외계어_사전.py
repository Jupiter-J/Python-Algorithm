

#존재 = 1 , 존재 안함=2
def solution1(spell, dic):
    for word in dic:
        ch = 0
        check = list(word) #리스트화
        for x in spell:
            if x in check:
                ch+=1
        if ch == len(spell):
            return 1
    return 2


"""
리펙토링
"""

def solution2(spell, dic):
    answer=0
    for word in dic:
        ch = 0
        for x in spell:
            if x in word:
                ch+=1
        if ch == len(spell):
            return 1
    return 2

print(solution1(["s", "o", "m", "d"],["sod", "eocd", "qixm", "adio", "soo"] ))

print(solution2(["s", "o", "m", "d"],["sod", "eocd", "qixm", "adio", "soo"] ))