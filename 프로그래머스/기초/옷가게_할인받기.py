
price=1500000
answer = 0
if price >= 500000:
    answer = int(price - price * 0.2)
elif price >= 300000:
    answer = int(price - price * 0.1)
elif price >= 100000:
    answer = int(price - price * 0.05)

answer = answer//10*10

print(answer)

"""
리펙토링
"""
def solution(price):
    answer = 0
    if price >= 500000:
        answer = price - price * 0.2
    elif price >= 300000:
        answer = price - price * 0.1
    elif price >= 100000:
        answer = price - price * 0.05
    else:
        answer = price

    return int(answer)