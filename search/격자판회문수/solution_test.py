# 문제: 1-9까지의 자연수로 채워진 7*7 격자판이 주어지면 격자판 위에서 가로 방향 또는 세로 방향으로 길이 5자리 회문수(거꾸로 읽어도 똑같은 수)가 몇 개 있는지 출력하는 프로그램

import sys
# sys.stdin = open("input.txt", "r")
board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):
    for j in range(7): 
        # 행
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]: # 거꾸로 변경한 것과 비교
            cnt += 1
        # 열 
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else: # 정상적으로 for문이 종료되었을 때
            cnt += 1
        
print(cnt)


# <회문의 길이가 가변적일 때 코드>
import sys
# sys.stdin = open("input.txt", "r")
board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
len = 5
for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+len]
        if tmp == tmp[::-1]:
            cnt += 1
        # tmp = board[i:i+5][j] 앞 행은 리스트가 아니라서 슬라이스가 안된다.
        for k in range(len//2):
            if board[i+k][j] != board[len-k+i-1][j]:
                break
        else:
            cnt += 1
        
print(cnt)