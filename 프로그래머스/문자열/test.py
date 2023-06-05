

def solution(s):
    result = [] # 쪼갠 문자열의 길이를 담는다
    if len(s) == 1:
        return 1
    for i in range(1, (len(s) // 2) + 1):
        b = ''
        cnt = 1 #문자열이 연속 반복되는지 체크 확인
        tmp = s[:i] # 문자열을 쪼갤때 처음부분은 tmp에 저장
        for j in range(i, len(s), i):
            if tmp == s[j:i + j]:
                cnt += 1
            else:
                if cnt != 1:
                    b = b + str(cnt) + tmp
                else:
                    b = b + tmp
                tmp = s[j:j + i]
                cnt = 1
        if cnt != 1:
            b = b + str(cnt) + tmp
        else:
            b = b + tmp
        result.append(len(b))
    return min(result)