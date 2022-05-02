"""
문제: 현수는 1년 과정의 수업계획을 짜여한다. 
수업 중에는 필수 과목이 있는데 이 필수 과목은 반드시 이수해야 하며, 그 순서도 정해져 있다.
수업계획서상의 각 과목은 무조건 이수된다고 가정한다.
필수 과목순서가 주어지면 현수가 짠 N개의 수업 설계가 잘 된 것이면 "YES", 잘못된 것이면 "NO"를 출력

<입력>
CBA
3
CBDAGE
FGCDAB
CTSBDEA

<출력>
#1 YES
#2 NO
#3 YES
"""

# 큐
import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
need = input() # 필수과목
n = int(input()) # 플랜개수
for i in range(n):
    plan = input() # 플랜
    dq = deque(need)
    for x in plan: # 필수과목 순서 확인
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" %(i+1))
                break
    else: # 필수과목 모두를 수강했는지 확인
        if len(dq) == 0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))
