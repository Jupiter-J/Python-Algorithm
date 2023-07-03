

def solution(n):
    if n==1 or n==2:
        return 1
    else:
        return solution(n-2) + solution(n-1)

print(solution(5))