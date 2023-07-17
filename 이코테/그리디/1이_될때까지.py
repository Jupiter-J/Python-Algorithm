
"""
1이 될때 까지
"""

n, k = map(int, input().split())
cnt=0
while n!=1:
    if n%k==0:
        n=n//k
        cnt+=1
    else:
        n=n-1
        cnt+=1
print(cnt)

def solution(n, k):
    answer=0
    while n != 1:
        if n % k == 0:
            n = n // k
            answer += 1
        else:
            n = n - 1
            answer += 1

    return answer
print(solution(25, 5))