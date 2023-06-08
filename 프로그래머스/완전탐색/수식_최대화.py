"""
수식 최대화
1. 문자열 분리
2. 연산자 우선순위
3. 숫자계산
4. 가장 큰 결과값 반환

import itertools - permutations : 순열
import itertools - combinations : 조합
"""


expression="100-200*300-500+20"
a = expression.split('[0-9]')
print(a)



from itertools import permutations
import re



