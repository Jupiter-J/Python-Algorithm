

def solution(box, n):
    s=1
    for x in box:
        s*=(x//n)
    return s


print(solution([10, 8, 6],3))