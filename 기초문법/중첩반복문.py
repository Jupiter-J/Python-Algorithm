
# 중첩 반복문(2중 for문)
for i in range(5):
    for j in range(5):
        print(j, end='') #i가 0일때 j가 0~5 순회
    print()


for n in range(5):
    print('n:', n, sep='', end='') #
    for m in range(5):
        print(' m:', m, sep='', end=' ')
    print()

