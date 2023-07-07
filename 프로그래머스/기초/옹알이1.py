
# from itertools import permutations
# arr = ['a','b','c']
# for x in permutations(arr,2):
#     print(x)
#     """
#     ('a', 'b')
#     ('a', 'c')
#     ('b', 'a')
#     ('b', 'c')
#     ('c', 'a')
#     ('c', 'b')
#     """


# from itertools import combinations
# arr = ['a','b','c']
# for y in combinations(arr,2):
#     print(y)
#     """
#     ('a', 'b')
#     ('a', 'c')
#     ('b', 'c')
#     """


from itertools import permutations
def solution(babbling):
    answer = 0
    speek = ["aya","ye","woo","ma"]
    word = []

    for i in range(1, len(speek)+1): #1,2,3,4개를 사용한 모든 경우의 수 생성
        for j in permutations(speek, i):
            word.append(''.join(j)) # 문자열로 합치기

    for i in babbling:
        if i in word:
            answer += 1
    return answer

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))