"""
문제: 유럽에서 가장 유행하는 유람선 타이타닉이 침몰하고 있다.
유람선에는 N명의 승객이 타고 있다.
구명보트를 타고 탈출해야 하는데 타이타닉에 있는 구명보트는 2명 이하로만 탈 수 있으며, 
보트 한 개에 탈 수 있는 총 무게도 M kg이하로 제한되어 있습니다.

N명의 승객 몸무게가 주어졌을 때 승객 모두가 탈출하기 위한 구명보트의 최소 개수를 출력

첫째 줄에 자연수 N과 M이 주어진다.
두 번째 줄에 N개로 구성된 몸무게 수열이 주어진다. 
몸무게는 50이상 150이하이다.
각 승객의 몸무게는 M을 넘지는 않습니다.

5 140
90 50 70 100 60
"""

# 그리디
import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
p = deque(p) # 리스트의 pop를 사용하면 중간에 빈 index를 채우기 위해 앞으로 뒤에 값들을 앞으로 옮기는 연산을 하는 과정이 비효율적이기 때문에 deque를 사용
cnt = 0 
while p: # p가 비어있자 얺으면 참
    if len(p) == 1: # 마지막 한 명이 남았을 때
        cnt += 1
        break
    if p[0] + p[-1] > limit:
        p.pop() # 구명보트를 타고 탈출
        cnt += 1
    else:
        # p.pop(0) # 맨 앞 제거 - 리스트 사용
        p.popleft() # 맨 앞 제거 - deque 사용
        p.pop() # 맨 뒤 제거
        cnt += 1
print(cnt)