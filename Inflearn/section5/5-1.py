
"""
5-1. 가장 큰수 (스택)
스택은 LIFO - 나중에 들어간게 먼저 나온다 (구덩이)

# 조건식
AND 조건 - A AND B : A와 B 둘다 참이어야 조건 성립
OR 조건 - A OR B : A와 B 둘중 하나라도 참이면 조건 성립
NOT 조건 - A NOT B : A와 B 둘다 아니어야 조건 성립

# 공백 없이 출력
''.join(map(str,stack))

# 정수를 리스트화
list(map(int, str(num)))

# while문 조건
while stack = stack이 비어있으면 F, 비어있지 않으면 T

# 슬라이싱 a {0,1,2,3,4,5,6,7,8,9}
a[3:] = 3위치 포함 하고 뒤까지 {3,4,5,6,7~}
a[:3] = 3위치 포함 하지 않고 앞까지 {0,1,2}
a[3:6] = 3위치 부터 5까지 {3,4,5}
a[:-3] = 끝에서 3위치 포함 하고 앞까지 {0,1,2,3,4,5,6}
a[-3:] = 끝에서 3위치 포함하지 않고 뒤까지 {7,8,9}
a[-6:-3] = 끝에서 6위치 포함하지 않고 끝에서 3위치 까지 {4,5,6}

"""

# num, m = map(int, input().split())
# # 정수를 분리 - string처리를 먼저 -> int로 변경하여 하나씩 접근하기 -> 리스트화
# num=list(map(int, str(num)))
# stack=[]
# for x in num:
#     while stack and m>0 and stack[-1]<x: #스택이 비어있지 않을때, 뺄 횟수가 남아 있을때, 마지막 수가 현재 나보다 작을때
#         stack.pop()
#         m-=1
#     stack.append(x)
# # 횟수가 모두 끝나면 뒷 값을 날린다
# if m!=0:
#     stack=stack[:-m]
# res=''.join(map(str,stack))
#
# print(res)


num, n = map(int, input().split())
num = list(map(int, str(num)))
stack=[]

for x in num:
    while stack and n>0 and stack[-1] < x:
        stack.pop()
        n-=1
    stack.append(x)
if n!=0:
    stack=stack[:-n]
for x in stack:
    print(x, end='')

