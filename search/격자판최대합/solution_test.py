# 문제: N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각성의 합 중 가장 큰 합을 출력

import sys
# sys.stdin = open('input.txt', 'r')
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)] # 2차원 리스트로 값 받기

largest = -2147000000

# 가로, 세로
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j] # 행 더하기
        sum2 += a[j][i] # 열 더하기
        
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
        
# 대각선
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i] # 왼 -> 오 대각선
    sum2 += a[i][n-i-1] # 오 -> 왼 대각선
    
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2
    
print(largest)