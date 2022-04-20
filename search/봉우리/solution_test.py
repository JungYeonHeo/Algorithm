"""
문제: 지도 정보가 N * N 격자판에 주어지는데, 각 격자에는 그 지역의 높이가 쓰여있다. 
각 격자판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역이다.
봉우리 지역이 몇 개인지 알아내서 출력

5
5 3 7 2 3
3 7 1 6 1
7 2 5 3 4
4 3 6 4 1
8 7 3 5 2
"""

import sys
#sys.stdin = open("input.txt", 'r')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 입력받은 2차원 리스트의 테두리에 0값을 추가 => 테두리 값에도 상하좌우 비교를 할 수 있게 됨
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)

# 상하좌우 값 비교
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)): # all(): 조건이 모두 참일때 참
            cnt += 1
print(cnt)