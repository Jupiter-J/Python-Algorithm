
# 최솟값 구하기_선수지식
    #코드를 다 짜고 난뒤 최종적인 배열에서 최솟값 구할때
arr = [5,3,7,9,2,5,2,6]

#1. 가장 큰값(무한대 infinity)으로 초기화를 시킨다
    #무한 수는 float형에만 적용가능하다. int형에는 적용 불가능
    #무한대로 넣는 이유는 첫번째 값이 true가 되도록 하기 위해서
arrMin=float('inf')
#arrMin= arr[0] 대신 사용 가능

#2. 전체를 순회시킨다
   #i:인덱스번호 #len(arr) = 8개
for i in range(len(arr)):  
    if arr[i]< arrMin: #3. 작은 값이 발견되면 저장
        arrMin=arr[i] #인덱스 0기준으로 전체 비교가 된다 
print(arrMin)

'''
range를 사용하지 않는 다른 방법

for x in arr:
    if x<arrMin:
        arrMin=x
print(arrMin)

'''