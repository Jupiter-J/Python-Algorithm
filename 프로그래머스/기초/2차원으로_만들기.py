
num_list = [1, 2, 3, 4, 5, 6, 7, 8]
n = 2
tmp = 4
arr = [[ x for x in range(tmp)] for j in num_list]

print(arr)


def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i + n])

    return answer