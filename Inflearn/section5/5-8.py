"""
8. 단어찾기
n개의 단어를 저장했다가 n+1번째부터 같은 단어가 있는지 탐색 -> 하나씩 제거후
남은 단어를 출력시켜야함

dectionary 자료구조
"""

# n = int(input())
# p = dict()
# for i in range(n):
#     word=input()
#     p[word]=1 #key:word , value:1로 담는다
# for i in range(n-1):
#     word=input()
#     p[word]=0
# for key, val in p.items():
#     if val==1:
#         print(key)
#         break


n = int(input())
d = dict()

for i in range(n):
    word = input()
    d[word] = 0
for i in range(n-1):
    word = input()
    d[word] = 1

for key, val in d.items():
    if val==0:
        print(key)
        break


