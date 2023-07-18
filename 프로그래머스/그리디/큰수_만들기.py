
def solution(number, k):
    answer = ''
    stack = []

    for x in number:
        while stack and x > stack[-1]:
            if k> 0:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(x)

    if k > 0:
        for x in range(k):
            stack.pop()

    answer = ''.join(stack)
    return answer

print(solution("1924", 2))