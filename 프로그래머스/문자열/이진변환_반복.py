
"""
1. 0을 제거 -> 몇개 제거했는지 확인, 해당길이를 구함
2. 해당길이만큼 2진법으로 변환한다
3. 다시 반복
bin() : 10진수 -> 2진수 변환
** 2진변환시 Ob가 앞에 붙음으로 [2:]슬라이싱 적용
0을 찾지 않고 1을 찾음으로서 코드가 더 줄어듬(0일경우 replace를 사용해서 바꿔야함)
O(lg n)??
"""
def solution(s):
    #횟수 기록
    change, zero_cnt = 0, 0
    while s != '1':
        change += 1
        num = s.count('1')
        #1의 갯수를 확인하여 전체길이에서 빼 0의 갯수를 저장한다
        zero_cnt += len(s) - num
        s = bin(num)[2:]
    return [change, zero_cnt]