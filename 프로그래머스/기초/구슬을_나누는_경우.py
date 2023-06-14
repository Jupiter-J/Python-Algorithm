
from math import factorial as fac
def solution(balls, share):
    answer = 0
    n = fac(balls)
    m = fac(share)
    b = fac(balls - share ) *m

    return n/ b