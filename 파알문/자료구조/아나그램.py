
"""
AbaAeCe
baeeACA
"""
a = input()
b = input()
word1 = dict()
word2 = dict()

for c in a:
    word1[c]=word1.get(c,0)+1
for c in b:
    word2[c]=word2.get(c,0)+1

for i in word1.keys():
    if i in word2.keys():
        if word1[i]!=word2[i]: #value값 비교로 확인
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")

