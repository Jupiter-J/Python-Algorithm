
"""
1. 문제풀이
약수를 오름차 순 나열 후 m번째 구하기 -> i가 1부터 시작함으로 어자피 오름차순이다
"""
# n, m = map(int, input().split())
# cnt=0
# # 약수 구하기
# for i in range(1, n+1):
#     if n%i==0:
#         cnt+=1
#     if cnt == m:
#         print(i)
#         break
# else:
#     print(-1)

"""
2. k번째 수 
# s-e번째 값 뽑기
리스트 슬라이스 기능 : a=a[s-1:e]
정수 출력 : print("%d" %(t+1))
"""
# T = int(input())
# for t in range(T):
#     n, s, e, k = map(int, input().split())
#     n_list = list(map(int, input().split()))
#     n_list = n_list[s-1:e]
#     n_list.sort()
#     print("#%d %d" %(t+1, n_list[k-1]))


"""
3. k번째 큰수
set()- 집합자료형 사용 // 중복허용 안함
list-> sort(reverse=True) //내림차 순 정렬 reverse=True
"""
# n, k = map(int, input())
# a = list(map(int, input().split()))
# res = set()
#
# for i in range(a):
#     for j in range(i+1, a):
#         for m in range(j+1, a):
#             res.add(a[i]+a[j]+a[m])
# res=list(res)
# res.sort(reverse=True)
# print(res[k-1])

"""
4.대표값
"""
# n=int(input())
# test=list(map(int, input().split()))
# avg = round(sum(test)/n)
# avg = avg+0.5
# avg= int(avg)
# min=21747000000
#
# for idx, x in enumerate(test):
#     tmp=abs(x-avg)
#     if tmp<min:
#         min=tmp #비교할 최솟값
#         score=x #실제값
#         res=idx+1 #학생번호
#     elif tmp==min:
#         if x>score:
#             score=x
#             res=idx+1
# print(avg, res)

"""
5. 정다면체 
"""
# n, m = map(int, input().split())
# cnt=[0]*(n+m+3) #경우의 수를 구할 배열
# max=-2147000000
#
# # 경우의 수를 전부 리스트에 저장
# for i in (1,n+1):
#     for j in (1, m+1):
#         cnt[i+j]+=1
# # 리스트의 max값을 구한다(최대빈도)
# for i in range(n+m+1):
#     if cnt[i]>max:
#         max=cnt[i]
# # 최대값을 가지고 있는 인덱스를 찾는다
# for i in range(n+m+1):
#     if cnt[i]==max:
#         print(i, end=' ')

"""
6. 자릿수의 합
"""
# n= int(input())
# n_list = list(map(int, input().split()))
# max=-2147000000
# def digit_sum(x):
#     sum=0
#     while x>0:  #숫자 뒤집기
#         sum+= x%10
#         x=x//10
#     return sum
#
# for x in n_list:
#     tot = digit_sum(x)
#     if tot > max:
#         max= tot
#         res= x
# print(res)

"""
7. 소수
리스트의 인덱스가 소수
소수일 경우 0으로 체크하여 카운트
소수가 아닐경우 1로 체크하여 제외시킨다 
"""
# n=int(input())
# arr=[0]*(n+1)
# cnt=0
# for i in range(2, n+1):
#     if arr[i]==0:
#         cnt+=1
#         for j in range(i, n+1, i):
#             arr[j]=1
# print(cnt)


"""
8. 뒤집은 소수 
"""
# n= int(input())
# n_list = list(map(int, input().split()))
#
# def reverse(x):
#     res=0
#     while x>0:
#         t=x%10 #나머지인 일의자리 t에 저장
#         res=res*10+t #첫째자리로 변경
#         x=x//10 #몫을 x에 저장
#     return res
#
# def isPrime(x):
#     if x==1: #1의경우 F
#         return False
#     for i in range(2, x//2+1): #2부터 소수값의 절반
#         if x%i==0:
#             return False
#     else:
#         return True
#
# for x in n_list:
#     tnt = reverse(x)
#     if isPrime(tnt):
#         print(tnt, end=' ')

