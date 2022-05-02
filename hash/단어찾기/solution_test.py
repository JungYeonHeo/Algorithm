"""
문제: 현수는 영어로 시를 쓰는 것을 좋아한다.
현수는 시를 쓰기 전에 쓰일 단어를 미리 노트에 적어둔다.
이버에는 N개의 단어를 노트에 적었는데 시에 쓰지 않은 단어가 하나 있었다고 하는데 
이 단어를 찾아 출력

첫 번째 줄에 자연수가 주어진다.
두 번째 줄부터 노트에 미리 적어 놓은 N개의 단어가 주어지고, 
이어 바로 다음 줄부터 시에 쓰인 N-1개의 단어가 주어진다.

<입력>
5
big
good
sky
blue
mouse
sky
good
mouse
big

<출력>
blue
"""

# 해쉬 -> 딕셔너리형 사용
import sys
# sys.stdin = open("input.txt", "r")
n = int(input())
p = dict() 
for i in range(n): # 모든 단어 값 1로 초기화
    word = input()
    p[word] = 1
for i in range(n-1): # 쓰인 단어 겂 0으로 초기화
    word = input()
    p[word] = 0
for key, val in p.items(): 
    if val == 1: # 안 쓰인 단어 
        print(key)
        break
