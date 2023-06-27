
"""
의상
1. 같은 옷끼리 정렬
2.
"""
def solution(clothes):
    answer = 1
    dic = dict()

    #1. 같은 옷끼리 정렬 => {'headgear': ['yellow_hat', 'green_turban'], 'eyewear': ['blue_sunglasses']}
    for cloth in clothes:
        if cloth[1] not in dic.keys():
            dic[cloth[1]] = [cloth[0]]
        else:
            dic[cloth[1]].append(cloth[0])

    print(dic)
    #2. 경우의 수 => 각각입는경우 + 입지않는경우 1
    for value in dic.values():
        answer *= len(value)+1
        print(answer)
    return answer-1 #모두 입지 않는 경우를 제외

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))