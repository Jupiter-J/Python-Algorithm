
# s = input()
# stringNum = ""
# answer = 0
# # 숫자- 문자열
# for i in range(len(s)):
#     if not s[i].isalpha():
#         stringNum +=s[i]
# # 앞의 0 제거
# num = int(stringNum)
#
# # 약수 개수
# for i in range(1, num+1):
#     if num%i==0:
#         answer +=1
#
# print(num)
# print(answer)


s = input()
res = 0
for x in s:
    if x.isdecimal():
        res=res*10+int(x) # 앞자리 0을 제거 하고 숫자화 시키는 방법
print(res)
cnt =0
for i in range(1, res+1):
    if res%i==0:
        cnt+=1
print(cnt)