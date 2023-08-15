
"""
AbaAeCe
baeeACA
"""
a = input()
b = input()
find=dict()
for c in a:
    find[c]=find.get(c,0)+1
for c in b:
    find[c]=find.get(c,0)-1

for c in a:
    if find.get(c)>0:
        print("NO")
        break
else:
    print("YES")


