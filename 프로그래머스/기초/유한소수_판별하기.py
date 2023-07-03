def solution(a, b):
    # 기약분수인지 판별 // 기약분수로 만들기
    for i in range(2, a + 1):
        if a % i == 0 and b % i == 0:
            a = a // i
            b = b // i
    # 소인수 분해
    num = []  # 소인수 저장
    i = 2
    while i <= b:  # 소인수 구하기
        if b % i == 0:
            b //= i #나눈값의 몫을 대입
            num.append(i)
        else:
            i += 1

    if all(i in [2, 5] for i in num):
        # 소인수가 2와 5만 존재하면 유한소수 그렇징 않으면 무한소수
        return 1
    return 2

print(solution(13,14))