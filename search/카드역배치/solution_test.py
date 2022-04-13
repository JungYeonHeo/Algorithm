# 문제: 1-20사이의 숫자가 하나씩 적인 20장의 숫자카드에서 구간이 주어지면 구간의 숫자를 역순으로 정렬하여 전체출력
import sys
# sys.stdin = open('input.txt', 'rt')
a = list(range(21)) # 0-20
for _ in range(10): # _를 사용하면 변수 없이 반복함 
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i] # swap 
   
a.pop(0)
for x in a:
    print(x, end=' ')

    
    


