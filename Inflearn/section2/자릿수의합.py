
"""
자릿수의 합
3
125 15232 97
"""
# def digit_sum(x):
#     answer = 0
#     for i in x:
#         answer+=int(i)
#     return answer
#
# n = int(input())
# a = list(map(int, input().split()))
# max= -2147000000
#
# for i in a:
#     addnum= digit_sum(str(i))
#     if addnum > max:
#         max=addnum
#         res=i
# print(res)


"""
정답
"""

n= list(input())
a=list(map(int, input().split()))
def digit_sum(x):
   sum=0
   while x>0:
       sum+=x%10
       x=x//10
       
max= -2147000000
for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x
print(res)