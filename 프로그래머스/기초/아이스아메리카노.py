

def solution(money):
    answer = []
    cup = money//5500
    answer.append(cup)
    answer.append(money-cup*5500)
    return answer

"""
리펙토링
"""


money=31450
print(money%5500)
answer = [money//5500, money%5500]

print(answer)