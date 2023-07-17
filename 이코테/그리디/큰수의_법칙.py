
"""
큰수의 법칙
666,5,666
"""

# def solution(num, m, k):
#     answer=0
#     num.sort(reverse=True)
#
#     while True:
#         for i in range(k):
#             if m==0:
#                 break
#             answer += num[0]
#             m-=1
#         if m == 0:
#             break
#         answer += num[1]
#         m-=1
#     return answer
#
# print(solution([2,4,5,4,6],8, 3))


"""
복습
"""
# n, m, k = map(int, input().split())
# num = list(map(int, input().split()))
#
# num.sort(reverse=True)
# answer=0
#
# while True:
#     for i in range(k):
#         if m==0:
#             break
#         answer+=num[0]
#         m-=1
#     if m==0:
#         break
#     answer+=num[1]
#     m-=1
#
# print(answer)

"""
ver2
"""
n,m, k = map(int, input().split())
num = list(map(int, input().split()))
num.sort(reverse=True)

cnt = m//(k+1)*k
cnt += m%(k+1)
answer = 0
answer += cnt * num[0]
answer += (m-cnt)*num[1]
print(answer)

