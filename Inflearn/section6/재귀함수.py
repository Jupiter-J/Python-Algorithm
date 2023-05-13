

# n = int(input())
# t = []
#
# while n>0:
#     t.append(n%2)
#     n=n//2
#
# t.reverse()
# print(t)

# def DFS(x):
#     if x>0:
#         DFS(x-1)
#         print(x)
#
# n= int(input())
# DFS(n)

"""
재귀를 할때는 if - else 문 사용
"""
# def DFS(x):
#     if x==0:
#         return
#     else:
#         DFS(x//2)
#         print(x % 2, end=' ')
#
# n = int(input())
# DFS(n)


def DFS(x):
    if x==0:
        return
    else:
        DFS(x//2)
        print(x%2, end=' ')

n = int(input())
DFS(n)