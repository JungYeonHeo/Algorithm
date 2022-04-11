# 문제: 앞으로 읽을 때나 뒤로 읽을 때나 같은 경우 YES, 같지 않은 경우 NO출력
# 1번 방식
import sys
# sys.stdin = open('input.txt', 'rt')
n = int(input())
for i in range(n):
    s = input()
    s = s.upper() # s를 대문자화
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print('#%d NO' %(i + 1))
            break
    else: # break를 안 당하고 정상종료시 실행
        print('#%d YES' %(i + 1))
        

# 2번 방식        
import sys
# sys.stdin = open('input.txt', 'rt')
n = int(input())
for i in range(n):
    s = input()
    s = s.upper() # s를 대문자화
    if s == s[::-1]:
        print('#%d YES' %(i + 1))
    else:
        print('#%d NO' %(i + 1))