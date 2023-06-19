
def find_parent(n, parents):
    if parents[n] == n: #특정 부모의 노드 찾기
        return n    # 부모가 자신이면, 자신을 반환
    return find_parent(parents[n], parents)

def union_parent(a, b, parents):
    a = find_parent(a, parents) #각각의 부모를 찾고, 더 작은 부모를 가질 수 있게 한다
    b = find_parent(b, parents)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def solution(n, costs):
    answer = 0
    parents = [i for i in range(n)]
    graph = sorted(costs, key=lambda x :x[2])

    for a, b, c in graph: #같은 부모를 가지는지 비교
        if find_parent(a, parents) == find_parent(b, parents):
            continue
        else:
            union_parent(a, b, parents)
            answer += c
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))