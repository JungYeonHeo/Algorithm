# 문제: 수들이 주어지는데 연속적인 수를 더했을 때 입력받은 값이 되는 경우의 수 출력

import sys
# sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0
while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1

print(cnt)