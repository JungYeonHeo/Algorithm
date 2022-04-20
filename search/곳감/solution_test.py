"""
문제: N * N 수와 M * M의 수를 격자판 형태로 입력받는다. 
M * M 2차원 리스트의 첫 번째 수는 행번호, 두 번째 수는 방향인데 0이면 왼쪽, 1이면 오른쪽이고, 세 번째 수는 회전하는 격자의 수이다. 
이런 규칙을 통해 N * N 행렬을 회전시키고 이렇게 회전시킨 격자판에서 모래시계 모양에 해당하는 부분의 수의 합을 출력  

5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
3
2 0 3
5 1 2
3 1 4
"""

import sys
# sys.stdin = open("input.txt", 'r')
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)] # 2차원 리스트 입력받기
m = int(input())
for i in range(m):
    h, t, k = map(int, input().split()) # 한줄씩 읽어서 처리 
    if t == 0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0)) # 맨 앞값을 빼서 맨 뒤에 넣기 
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop()) # 맨 뒤값을 빼서 맨 앞에 넣기

# 모래시계 모양에 있는 칸의 수들의 합
res = 0
s = 0 # 시작 index
e = n-1 # 끝 index 
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)