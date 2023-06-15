

def DFS(numbers, step, total, target):
    if step == len(numbers):
        if total == target:
            return 1  # 숫자를 만듬
        else:
            return 0 # 못 만듬
    ret = 0
    ret += DFS(numbers, step +1, total + numbers[step], target) # 다음 숫자를 더한다 (왼쪽 노드)
    ret += DFS(numbers, step +1, total - numbers[step], target) # 다음 숫자를 뺀다 (오른쪽 노드)
    return ret
def solution(numbers, target):
    return DFS(numbers, 0, 0, target)

print(solution([1, 1, 1, 1, 1],3))