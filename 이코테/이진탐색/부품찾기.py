

"""
5
8 3 7 9 2
3
5 7 9
"""
n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

answer =[]

for check in m_arr:
    if check in n_arr:
        answer.append("YES")
    else:
        answer.append("NO")
print(' '.join(answer))


"""
DFS
"""

def binary_serach


