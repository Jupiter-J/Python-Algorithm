

"""
침몰하는 타이타닉
list-sort를 하게되면 매번 자료가 앞으로 당겨진다(비효율적임)
deque는 양방향으로 자료에 접근이 가능하다

[list]- pop(0) //O(N)
[deque] - popleft() //O(1)
"""

# from collections import deque
# n, m = map(int, input().split())
# member=list(map(int,input().split()))
# member.sort()
# member=deque(member)
# cnt=0
#
# # 리스트가 비어있지 않으면 참 / 비어있으면 F 탈출
# while member:
#     if len(member)==1: #한명만 남을 경우
#         cnt+=1
#         break
#     if member[0] + member[-1] > m:
#         member.pop() #가장 끝 탈출
#         cnt+=1
#     else:
#         member.popleft()
#         member.pop() #가장 끝 탈출
#         cnt+=1
# print(cnt)

from collections import deque
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = deque(a)
cnt=0

while a:
    if len(a)==1:
        cnt+=1
        break
    if a[0] + a[-1] > m:
        a.pop()
        cnt+=1
    else:
        a.pop()
        a.popleft()
        cnt+=1

print(cnt)
