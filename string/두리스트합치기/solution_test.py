# 문제: 오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로그램
# print(sorted(a+b))같이 sort를 사용하면 nlogn이 되는데 이미 정렬된 리스트를 입력받기 때문에 퀵정렬을 사용하면 n번으로 정렬할 수 있다.

import sys
# sys.stdin = open('input.txt', 'r')
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

p1 = p2 = 0
c = []
while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
        
# 남은 자료 
if p1 < n:
    c = c + a[p1:]
if p2 < m:
    c = c + b[p2:]
    
for x in c:
    print(x, end=' ')