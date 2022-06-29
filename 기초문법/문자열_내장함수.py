
# 문자열과 내장함수
msg="It is Time"
print(msg.upper()) #upper 대문자화 시킨다
print(msg.lower()) #lower 소문자화 시킨다

tmp=msg.upper() #tmp에 대문자 시킨값을 담는다 
print(tmp)
print(tmp.find('T')) #T를 찾아서 인덱스 "번호"를 리턴한다
print(tmp.count('T')) #T가 몇개인지 확인 
print(msg)
print(msg[:2]) #슬라이스 기능(:2) 인덱스번호를 적어 0번부터1번 
                #인덱스 번호 전까지 부분 "문자열" 을 뽑아낸다 
print(msg[3:5]) #3부터 4번까지 "문자열을 뽑아낸다"

#문자열 길이 구하기
print(len(msg))

#문자열 길이만큼 회전 1 - 문자열 전체 접근하기 
for i in range(len(msg)):
    print(msg[i], end=' ')
print()

#문자열 길이만큼 회전 2
for x in msg:
    print(x, end=' ')
print()

#문자열이 섞여 있을때 대문자만 추출
for x in msg:
    if x.isupper(): #x가 대문자이면 true
        print(x, end=' ')
print()

#대문자인지 소문자인지 판별
for x in msg:
    if x.islower(): #참을 리턴 = 소문자면 리턴 
        print(x, end=' ')
print()

#공백제거 추출 isalpha
for x in msg:
    if x.isalpha(): #알파벳만 추출
        print(x, end='') #공백없이 
print()

#아스키넘버 추출 ord
tmp='AZ'
for x in tmp:
    print(ord(x)) #아스키넘버 출력 A(65) ~ Z(90)

#소문자 아스키넘버 추출 ord
tmp='az'
for x in tmp:
    print(ord(x)) 

#아스키넘버 문자로 추출 char()
tmp=65
print(chr(tmp))