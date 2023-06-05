




def DFS(n):
    global cnt

    if n==1:
        return cnt
    if n%2==0:
        DFS(n//2)
        cnt+=1
    else:
        DFS(n*3+1)
        cnt+=1

# n = 6
# cnt = 0
# # DFS(n)
# print(cnt)


# num=6
#
# def solution(num):
#     count(num)
#     return count(num)
#
# def count(num):
#     cnt=0
#     if num==500:
#         return -1
#     if num==1:
#         return cnt
#     if num%2==0:
#         count(num//2)
#         cnt+=1
#     else:
#         count(num*3+1)
#         cnt+=1
#
#
# print(solution(num))


num=6

def collatz(num, answer):
    if num==1:
        return answer
    if answer==500:
        return -1
    if num%2==0:
        return collatz(num//2, answer+1)
    else:
        return collatz(num*3+1, answer+1)
def solution(num):
    return collatz(num, 0)

print(solution(num))



"""
복습
"""

def solution(num):
    return coratz(num,0)

def coratz(num, cnt):
    if cnt==500:
        return -1
    if num==1:
        return cnt
    if num%2==0:
        return coratz(num//2, cnt+1)
    else:
        return coratz(num*3+1, cnt+1)