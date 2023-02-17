
"""
8. 뒤집은 소수

"""

n = int(input())
num = list(map(int, input().split()))

def reverse(x):
   res=0
   while x>0:
       t=x%10
       res=res*10+t
       x=x//10
   return res
def isPrime(x):
    if x==1:
        return False
    for i in range(2, x//2+1): #전부 다 돌 필요없이 반까지만 돌면 됨
        if x%i==0:
            return False
    else: #정상 종료되었을 경우 - for-else
        return True

for x in num:
    tmp=reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')
