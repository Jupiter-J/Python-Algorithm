
'''
n = int(input())
a = list(map(int, input().split()))

def digit_sum(x): #함수를 만들때는 def
    sum=0
    while x>0:
        sum += x%10 #(%)나머지 일의 자리를 sum에 합하기
        x = x//10 #(//)몫을 다시 저장
    return sum

max=-2147000000
for x in a:
    tot=digit_sum(x) #sum을 리턴받는다 tot에 저장
    if tot>max:
        max=tot #합의 값이 큰게 max에 저장
        res=x
print(res)
'''

n = int(input())
a = list(map(int, input().split()))

def digit_sum(x): #함수를 만들때는 def
    sum=0
    for i in str(x): #str()문자열화 - 문자 하나하나를 접근하게 됨
        sum+=int(i)
    return sum

max=-2147000000
for x in a:
    tot=digit_sum(x) #sum을 리턴받는다 tot에 저장
    if tot>max:
        max=tot #합의 값이 큰게 max에 저장
        res=x
print(res)