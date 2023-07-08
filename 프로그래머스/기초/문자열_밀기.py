
from collections import deque
def solution(A, B):
    qA =deque(A)
    qB =deque(B)

    if qA==qB:
        return 0
    for _ in range(len(A)):
        qA.append(qA.pop())
        if qA==qB:
            return 1
    return -1

print(solution("hello","ohell"))


