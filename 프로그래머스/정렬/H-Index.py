def solution(citations):
    arr = sorted(citations)
    l = len(citations)

    for i in range(len(citations)):
        if arr[i] >= l - i:
            return l - i
    return 0