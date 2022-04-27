"""
문제: 중위표기식이 입력되면 후위표기식으로 변환하는 프로그램 작성

3+5*2/(7-2)
"""

# 스택
import sys
# sys.stdin = open("input.txt", "r")
a = input()
stack = []
res = ''
for x in a: 
    if x.isdecimal(): # 피연산자 
        res += x
    else: # 연산자
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-': 
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == '(':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()
print(res)
