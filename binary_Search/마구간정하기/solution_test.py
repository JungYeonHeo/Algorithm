"""
문제: N개의 마구간이 수직선상에 있다. 
각 마구간은 X1, x2, x3, ......, xN의 좌표를 가지며, 
마구간간에 좌표가 중복되는 일은 없다.
각 마구간에는 한마리의 말만 넣을 수 있고, 가장 가까운 두 말의 거리가 최대가 되게 말을 마구간에 배치하고 싶다.
C마리의 말을 N개의 마구간에 배치했을 때 가장 가까운 두 말의 거리가 최대가 되는 그 최댓값을 출력

첫 줄에 N과 C가 공백을 사이에 두고 주어진다.
둘째 줄부터 N개의 줄에 걸쳐 마구간의 좌표가 한 줄에 하나씩 주어진다.

5 3
1
2
8
4
9
"""

import sys
# sys.stdin = open("input.txt", "r")

def Count(len):
    cnt = 1 
    ep = Line[0]
    for i in range(1, n):
        if Line[i] - ep >= len:
            cnt += 1 
            ep = Line[i]
    return cnt

n, c = map(int, input().split())
Line = []

for _ in range(n):
    tmp = int(input())
    Line.append(tmp)

Line.sort()
lt = 1
rt = Line[n-1]
while lt <= rt:
    mid = (lt + rt) // 2 # mid값이 가장 가까운 두 말의 거리 
    if Count(mid) >= c:
        res = mid 
        lt = mid + 1
    else: 
        rt = mid - 1

print(res)
