
"""
아나그램
"""

# a = input()
# b = input()
# str1= dict()
# str2= dict()
#
# for x in a:
#     str1[x]=str1.get(x, 0)+1
#                 #x라는 key값이 없으면 0리턴, 있으면 value리턴
# for x in b:
#     str2[x]=str2.get(x, 0)+1
#
# #key값만 순환
# for i in str1.keys(): #str1 key값 돌면서 str2 key값 비교
#     if i in str2.keys():
#         if str1[i] != str2[i]:
#             print("NO")
#             break
#     else:
#         print("NO")
#         break
# else:
#     print("YES")


# a = input()
# b = input()
#
# a1 = dict()
# b2 = dict()
#
# for x in a:
#     a1[x] = a1.get(x, 0)+1
# for x in b:
#     b2[x] = b2.get(x, 0)+1
#
# for i in a1.keys():
#     if i in b2.keys():
#         if a1[i]!=b2[i]:
#             print("NO")
#             break
#     else:
#         print("NO")
#         break
# else:
#     print("YES")


"""
코드 개선
딕셔너리 두개를 사용하지 않고 한개만 사용하는 방법
"""

# a = input()
# b = input()
# sh = dict()
#
# for x in a:
#     sh[x]=sh.get(x, 0)+1
# for x in b:
#     sh[x]=sh.get(x, 0)-1
# for x in a:
#     if sh.get(x) > 0:
#         print("NO")
#         break
# else:
#     print("YES")


"""
코드 개선2 - 리스트 사용하기 (아스키 번호)
# ord(문자) : 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환
# chr(정수) : 하나의 정수를 인자로 받고 해당 정수에 해당하는 유니코드 문자를 반환
"""
a = input()
b = input()
str1=[0]*52
str2=[0]*52

for x in a:
    if x.isupper():
        str1[ord(x)-65]+=1
    else:
        str1[ord(x)-71]+=1
for x in b:
    if x.isupper():
        str2[ord(x)-65]+=1
    else:
        str2[ord(x)-71]+=1

for i in range(52):
    if str1[i]!=str2[i]:
        print("NO")
        break
else:
    print("YES")