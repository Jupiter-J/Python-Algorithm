

"""
문자열 뒤집기
0001100
000110011000
"""

data = input()
cn0 = 0 #전부0로 바뀌는 경우
cn1 = 0 #전부1로 바뀌는 경우
# 첫번째 원소
if data[0] =='1':
    cn0 +=1
else:
    cn1 +=1

# 두번째 원소부터 모든 원소 확인
for i in range(len(data) -1):
    if data[i] != data[i+1]:  #현재값[i] 다음값[i+1] 달라질 때
        #1로 바뀌는 경우
        if data[i+1] == '1':
            cn0 +=1
        else:
            cn1 +=1
print(min(cn0, cn1))


# s = input()
# zero = s.count('0')
# one = s.count('1')
#
# # 더 작은 값을 변경
# if zero >= one:
#     s=s.replace('0','1')
# else:
#     s=s.replace('1','0')
# print(s)