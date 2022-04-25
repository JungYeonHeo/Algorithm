"""
문제: 1부터 N까지의 모든 자연수로 구성된 N의 수열이 주어진다.
이 수열의 왼쪽 맨 끝 숫자 또는 오른쪽 멘 끝 숫자 중 하나를 가져와 나열하여 가장 긴 증가 수열을 만든다.
이 때 수열에서 가져온 숫자는 그 수열에서 제거된다.

첫째 줄에 자연수 N이 주어진다.
두 번째 줄에 N개로 구성된 수열이 주어진다.

첫째 줄에 최대 증가수열의 길이를 출력
두 번째 줄에 가져간 순서대로 왼쪽 끝에서 가져갔으면 'L', 오른쪽 끝에서 가져갔으면 'R'를 써간 문자열을 출력
(단, 마지막 남은 값은 왼쪽 끝이라고 생각한다.)

5
2 4 5 1 3
"""

# 그리디 
import sys
# sys.stdin = open("input.txt", "r")
n = int(input())
a = list(map(int, input().split()))

lt = 0 
rt = n - 1
last = 0 # 마지막으로 가져온 값
res = ""
tmp = []

while lt <= rt:
    if a[lt] > last:
        tmp.append((a[lt], 'L'))
    if a[rt] > last:  
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0: # 가져올 수 있는 값이 없을 때
        break
    else:
        res = res + tmp[0][1] 
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt += 1
    tmp.clear()
        
print(len(res))
print(res)

