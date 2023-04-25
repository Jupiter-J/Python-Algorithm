
"""
뒤집은 소수
"""

# n= int(input())
# a= list(map(int, input().split()))
#
# def reverse(x):
#     res=0
#     while x>0:
#         t=x%10
#         x=x//10
#         res=res*10+t
#     return res
#
# def isPrime(x):
#     if x==1: #100 -> 001로 넘어올 경우
#         return False
#     for i in range(2, x//2+1): #절반까지만 돌리기
#         if x%i==0:
#             return False
#     else:
#         return True
#
# for i in a:
#     answer=reverse(i)
#     if isPrime(answer):
#         print(answer, end=' ')

n= int(input())
a= list(map(int, input().split()))

def reverse(x):
    res=0
    while x>0:
        t=x%10
        x=x//10
        res=res*10+t
    return res

def isPrime(x):
    if x==0:
        return False
    for i in range(2, x//2+1):
        if x%i==0:
            return False
    else:
        return True

for i in a:
    answer = reverse(i)
    if isPrime(answer):
        print(answer, end=' ')
