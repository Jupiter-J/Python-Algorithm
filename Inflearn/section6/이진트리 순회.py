


"""
재귀 - 깊이우선탐색
"""

def DFS(v):
    if v>7:
        return
    else:
        #전위-대표적인 DFS
        DFS(v*2)
        print(v, end=' ')  #중위
        DFS(v*2+1)
        #후위-병합정렬


DFS(1)