"""
문제: 후위 연산이 주어지면 연산한 결과를 출력하는 프로그램을 작성
"""

# 스택
import sys
# sys.stdin = open("input.txt", "r")
a = input()
stack = []
for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        n1 = stack.pop()
        n2 = stack.pop()
        if x == '+':
            stack.append(n2 + n1)
        elif x == '-':
            stack.append(n2 - n1)
        elif x == '*':
            stack.append(n2 * n1)
        else:
            stack.append(n2 / n1)
print(stack[0])