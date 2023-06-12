def solution(n, k):
    sheep = n*12000
    drink = (k-(n//10))*2000
    return sheep+drink

"""
리펙토링
"""
def solution(n, k):
    return 12000*n + 2000*(k-n//10)