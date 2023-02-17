# n = int(input())
# a = list(map(int, input().split()))
# def digit_sum(x):
#     sum=0
#     while x>0:
#         sum+=x%10
#         x=x//10
#     return sum
#
# max=-2147000000
# for x in a:
#     tot=digit_sum(x)
#     if tot>max:
#         max=tot
#         res=x
# print(res)
#
#

"""
더 간단한 방법 - 문자열을 사용
str(x): x라는 정수를 문자로 바꾼다
자릿수 -> 10 나눈 나머지를 sum에 누적, 다시 10을 나눈 몫을 x에 저장해서 돌린다
"""
n = int(input())
a = list(map(int, input().split()))
def digit_sum(x):
    sum=0
    for i in str(x): #문자로 변경
        sum+=int(i) #정수화로 변경
    return sum

max=-2147000000

for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x
print(res)
