

"""
5
level
moon
abcba
soon
gooG
"""
# n = int(input())
# word = []
# for i in range(n):
#     s = input()
#     word.append(s.upper())
# cnt=0
# for check in word:
#     cnt+=1
#     if check == check[::-1]:
#         print("#%d YES" %cnt)
#     else:
#         print("#%d NO" %cnt)

n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size//2):
        if s[j]!=s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))






