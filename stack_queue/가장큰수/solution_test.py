"""
문제: 선생님은 현수에게 숫자 하나를 주고, 헤당 숫자의 자릿수들 중 m개의 숫자를 제거하여 가장 큰 수를 만들라고 했다.
단, 숫자의 순서는 유지해야 한다.
만약 5276823이 주어지고 3개의 자릿수를 제거한다면 7823이 가장 큰 숫자가 된다.

첫째 줄에 숫자와 제거해야 할 자릿수의 개수가 주어진다.
가장 큰 수를 출력

5276823 3
"""

# 스택
import sys
# sys.stdin = open("input.txt", "r")
num, m = map(int, input().split())
num = list(map(int, str(num)))
stack = []
for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:
    stack = stack[:-m]
res = ''.join(map(str, stack))
print(res)

