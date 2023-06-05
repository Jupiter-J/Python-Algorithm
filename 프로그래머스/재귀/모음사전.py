def DFS(dic, wrd, tmp):
    diction = ['A', 'E', 'I', 'O', 'U']
    if tmp == 6: #5까지만
        return
    if wrd != '':
        dic.append(wrd)
    for x in diction:
        DFS(dic, ''.join([wrd, x]), tmp + 1)


word = "AAAAE"

answer = 0
dic = []
DFS(dic, '', 0)
for i in range(len(dic)):
    if dic[i] == word:
        answer = i + 1
        break
print(answer)


"""
DFS를 사용하면서 diccion[] 배열에서 메모리 낭비가 심함
바로 배열 인덱싱 하도록 하기 
"""
def DFS(dic, wrd, tmp):
    if tmp == 6: #5까지만
        return
    if wrd != '':
        dic.append(wrd)
    for x in ['A', 'E', 'I', 'O', 'U']:
        DFS(dic, ''.join([wrd, x]), tmp + 1)


word = "AAAAE"

answer = 0
dic = []
DFS(dic, '', 0)
for i in range(len(dic)):
    if dic[i] == word:
        answer = i + 1
        break
print(answer)
