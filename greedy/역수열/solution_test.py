"""
문제: 1부터 n까지의 수를 한 번씩만 사용하여 이루어진 수열이 있을 때, 
1부터 n까지 각각의 수 앞에 놓여 있는 자신보다 큰 수들의 개수를 수열로 표현한 것을 역수열이라고 한다.
역수열을 보고 원래의 수열을 출력

첫 번째 줄에 자연수 N이 주어지고, 
두 번째 줄에는 역수열이 숫자 사이에 한 칸의 공백을 두고 주어진다.
 
8
5 3 4 0 2 1 1 0
"""

# 그리디
import sys
# sys.stdin = open("input.txt", "r")
n = int(input())
a = list(map(int, input().split())) # 역수열
seq = [0] * n
for i in range(n):
    for j in range(n):
        if a[i] == 0 and seq[j] == 0:
            seq[j] = i + 1
            break
        elif seq[j] == 0:
            a[i] -= 1
for x in seq:
    print(x, end=' ')
