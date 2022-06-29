
# 크기가 3인 1차원 리스트가 생성 
a=[0]*3
print(a)

#2차원 리스트 생성
b=[[0]*3 for _ in range(3)]
print(b)
b[0][1]=1 # 0행1열에 값을 넣는다
print(b)
b[1][1]=2
print(b)

# 표 형태 정렬
for x in b: #2차원 리스트를 표로 보기 위해 정렬 
    print(x) # x는 행을 의미

# 괄호없이 표 형태 정렬
for x in b:
    for y in x: # y는 하나하나의 원소값
        print(y, end=' ')
    print()