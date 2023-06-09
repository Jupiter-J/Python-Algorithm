
n = 10

for i in range(1,n):
    if n*i%6==0:
        piece=i*n
        answer = piece//6
        print(answer)
        break


def solution(n):
    pizza = 1
    while (6 * pizza) % n != 0:
        pizza += 1
    return pizza