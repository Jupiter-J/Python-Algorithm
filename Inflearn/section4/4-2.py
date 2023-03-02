
"""
결정 알고리즘
찾고자 하는 답이 특정 범위 안에 있을 경우 이분검색을 사용한다
"""
k, n = map(int, input().split())
Line=[]
res=0 #최댓값
largest=0

#함수 생성: 몇개가 만들어지는지
def Count(len): #한개의 랜선 길이를 받는다
    cnt=0
    for x in Line:
        cnt+=(x//len) #나눈 몫을 구한다
    return cnt

# 줄바꿈 입력일 경우
for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest=max(largest, tmp) #기존값, 새값을 비교하여 더 큰값을 저장한다
lt=1
rt=largest

# 이분검색
while lt<=rt:
    mid=(lt+rt)//2 #mid=랜선의 길이
    if Count(mid)>=n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)


"""
"""

n , k = map(int, input().split())
List=[]
lt=1
res=0

# 2. 함수생성
def Count(len):
    cnt = 0
    for x in Line:
        cnt += (x // len)  # 나눈 몫을 구한다
    return cnt

# 1. 입력받기
for i in range(k):
    tmp=int(input())
    List.append(tmp)
    largest=max(tmp, largest)

lt=1
rt=largest
# 3. 이분검색
while lt >= rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
    print(res)

