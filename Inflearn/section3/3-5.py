
"""
5. 수들의 합
"""
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# lt=0
# rt=1
# tot=a[0] #lt부터 rt앞까지의 합
# cnt=0 #경우의 수
#
# while True:
#     if tot<m:#m보다 작으면
#         if rt<n: #rt가 n보다 작다면
#             tot+= a[rt] #rt값을 tot에 추가
#             rt+=1 #rt증가
#         else: #n 범위 밖을 벗어나면 멈춤
#             break
#     elif tot==m:
#         cnt+=1
#         tot-=a[lt] #경우의 수를 구했으니 같으면 해당 값 없애기
#         lt+=1   #lt 앞으로 1 증가
#     else: #m보다 작을 경우 -> lt와 rt의 값 차이를 없앤다
#         tot-=a[lt]
#         lt+=1
# print(cnt)

n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt=0
tot=a[0]
lt=0
rt=1

while True:
    if tot < m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot == m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        rt+=1
print(cnt)


