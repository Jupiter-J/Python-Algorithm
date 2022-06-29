
# 람다함수 = 익명함수
def plus_one(x):
    return x+1
print(plus_one(1)) 

plus_two = lambda x: x+2
print(plus_two(1))


#내장함수의 인자로 사용할때 효과적이다
a = [1,2,3]
print(list(map(plus_one, a)))
print(list(map(lambda x: x+1, a))) # 익명함수로 주로 사용 lambda 