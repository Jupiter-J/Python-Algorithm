# k번째 수
'''
[입력]
 2 - 테스트 케이스 총 갯수
 6 2 5 3 -테스트 케이스 1 {6:입력받는값 갯수, 2:5 인덱스값, 오름차순 정렬했을때 3번째 }
 5 2 7 3 8 9 
 15 3 10 3 - 테스트케이스 2
 4 15 8 16 6 6 17 3 0 11 18 7 14 7 15 

 [출력]
 #1 7 {케이스#1번 답 7}
 #2 6 
'''


# 테스트 입력받기
Case = int (input())
for i in range(Case):
    n, s, e, k = map(int, input().split())
    len = list(map(int, input().split()))
    sorted_list = len[s-1:e]
    sorted_list.sort()
    result = sorted_list[k-1]
    print("#%d %d" %(i+1, result))