"""
문제: 정보 왕국의 왕자가 N명이 있는데, 서로 공주를 구하러 가겠다고 한다. 
정보 왕국의 왕은 다음과 같은 방법으로 공주를 구하러 갈 왕자를 결정하기 했다.
왕은 왕자들을 나이 순으로 1번부터 N번까지 차례로 번호를 매긴다.
그리고 1번 왕자부터 N번 왕자까지 순서대로 시계방향으로 돌아가며 동그랗게 앉게 한다.
그리고 1번 왕자부터 시계방향으로 돌아가며 1부터 시작하여 번호를 외치게 한다.
한 왕자가 K를 외치면 그 왕자는 공주를 구하여 가는데서 제외되고 원 밖으로 나오게 된다.
그리고 다음 왕자부터 다시 1부터 시작하여 번호를 외쳐 K번째가 되면 원 밖으로 나오게 된다.
이렇게 해서 마지막까지 남은 왕자가 공주를 구하러 갈 수 있고 공주를 구하러 갈 왕자의 번호를 출력

8 3
"""

# 큐 -> deque 
import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
n, k = map(int, input().split())
dq = list(range(1, n+1))
dq = deque(dq)
while dq:
    for _ in range(k-1): # k번째 수 보다 앞애 있는 수 빼서 뒤에 넣기
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft() # k번째 수 제거
    if len(dq) == 1:
        print(dq[0])
        dq.popleft() # 하나 남은 수가 사라지기 때문에 while문 종료 -> break로 대체 