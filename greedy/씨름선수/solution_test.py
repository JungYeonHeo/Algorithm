"""
문제: 씨름감독이 씨름 선수 선발공고를 냈고, N명의 지원자가 지원을 했다.
씨름감독은 각 지원자의 키와 몸무게를 알고 있을때, 다음과 같은 원칙으로 선수를 선발하기로 정했습니다.
다른 모든 지원자와 비교하여 키와 몸무게 중 적어도 하나는 다른 지원자보다 키가 크거나 
몸무게가 많이 나가는 지원자만 뽑기로 했다.

첫째 줄에 지원자의 수가 주어진다.
둘째 줄부터 N명의 키와 몸무게 정보가 차례로 주어진다.
선수로 뽑히는 최대 인원을 출력

5
172 67
183 65
180 70
170 72
181 60
"""

# 그리디
import sys
# sys.stdin = open("input.txt", "r")
n = int(input())
body = []
for i in range(n):
    a, b = map(int, input().split())
    body.append((a, b))
body.sort(reverse=True) # 키 순으로 내림차순으로 정렬
largest = 0 # 몸무게가 가장 큰 사람의 무게
cnt = 0
for x, y in body:
    if y > largest: # 첫번째사람은 무조건 카운팅 됨
        largest = y
        cnt += 1
print(cnt)