
"""
Stack & Queue - 1.올바른 괄호

"""
# def solution(s):
#     answer = "NO"
#     stack = []
#     for x in s:
#         if x ==')':
#             if len(stack)==0:
#                 return "NO"
#             stack.pop()
#         else:
#             stack.append(x)
#     if len(stack)==0:
#         return "YES"
#     return answer
#
# print(solution("((()))()"))
# print(solution("(()(()"))
# print(solution("()())"))
# print(solution("())("))
# print(solution("((())))()("))

"""
2. backspace
"""

# def solution(s):
#     stack=[]
#     for c in s:
#         if c=='#':
#             if stack: #스택에 값이 있으면
#                 stack.pop()
#         else:
#             stack.append(c)
#
#     return ''.join(stack)
#
# print(solution("abc##ec#ab"))
# print(solution("##abc##ec#ab"))
# print(solution("kefd#ef##s##"))
# print(solution("teac#cher##er"))
# print(solution("englitk##shabcde##ff##ef##ashe####"))
# print(solution("itistime####gold"))

"""
연속된 문자 지우기
"""
# def solution(s):
#     stack=[]
#     for x in s:
#         if stack:
#             if stack[-1]==x:
#                 stack.pop()
#             else:
#                 stack.append(x)
#         else:
#             stack.append(x)
#     return ''.join(stack)

"""
연속된 문자 지우기 - 리펙토링
"""
# def solution(s):
#     stack=[]
#     for x in s:
#         if stack and stack[-1]==x:
#             stack.pop()
#         else:
#             stack.append(x)
#     return ''.join(stack)
#
#
# print(solution("acbbcaa"))
# print(solution("bacccaba"))
# print(solution("aabaababbaa"))
# print(solution("bcaacccbaabccabbaa"))
# print(solution("cacaabbc"))

"""
샌드위치
"""
# from collections import deque
# def solution(nums):
#     answer=0
#     stack=[]
#     for x in nums:
#         if len(stack)>=2:
#             if stack[-2]==1 and stack[-1]==2 and x==1:
#                 answer+=1
#                 stack.pop()
#                 stack.pop()
#             else:
#                 stack.append(x)
#         else:
#             stack.append(x)
#     return answer
#
#
# print(solution([1, 1, 1, 2, 1, 1, 2, 1, 2, 1]))
# print(solution([2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1]))
# print(solution([1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1]))
# print(solution([2, 1, 1, 1, 2, 1, 2]))
# print(solution([1, 1, 1, 1, 1, 1, 1]))

"""
고장난 프린터
"""
from collections import deque
def solution(nums):
    nums = deque(nums)
    while nums:
        if len(nums)==2:
            nums.popleft()
            if len(nums)==1:
                nums = list(nums)
                return nums[0]
        if len(nums) == 1:
            nums = list(nums)
            return nums[0]
        nums.popleft()
        nums.popleft()
        nums.append(nums.popleft())

"""
고장난 프린터 - 리펙토링
- 리스트-> 0번째 출력 하지말고 큐 자체에서 인덱스 출력하기
- 단순 반복일 경우 for문 활용하기 (if문 막 쓰지 말기)
"""
from collections import deque
def solution(nums):
    queue = deque(nums)
    while queue:
        for _ in range(2): #단순 2번 반복
            if len(queue)>=2:
                queue.popleft()
        queue.append(queue.popleft())
        if len(queue)==1: #1개 남았을때 큐 출력
            return queue[0]





print(solution([3, 1, 4, 5, 2, 6, 7]))
print(solution([10, 8, 3, 1, 4, 5, 2, 6, 7, 9]))
print(solution([10, 8, 3, 11, 12, 1, 4, 5, 2, 6, 7, 9]))
print(solution([10, 8, 3, 1, 4, 5, 2, 11, 13, 6, 7, 12, 9, 14]))
print(solution([1, 8, 6, 10, 4, 7, 2, 5, 3, 9]))