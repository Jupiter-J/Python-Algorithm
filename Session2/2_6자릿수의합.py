
# 자릿수의 합 


n = int(input())
arr = list(map(int, input().split()))

#함수를 만든다 - 매개변수 x
def digit_sum(x):
    sum = 0

    while x >0:
        sum += x%10  #자릿수를 구하기 위해 10으로 나눈 나머지
        x =x//10  # 10으로나눴을때 몫

for x in arr:
    total=digit_sum(x)