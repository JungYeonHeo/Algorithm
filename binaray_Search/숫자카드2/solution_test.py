# 백준 10816번 숫자카드 2

from collections import Counter
from sys import stdin

n = stdin.readline()
N = sorted(list(map(int,stdin.readline().split())))
m = stdin.readline()
M = list(map(int, stdin.readline().split()))        

count = Counter(N) # 리스트에 있는 각각의 요소가 몇개씩 있는지 {요소: 개수} 형태로 저장

for i in range(len(M)):
    if M[i] in count:
        print(count[M[i]], end=' ') # 키가 M[i]에 해당하는 값(개수)를 공백을 두어 출력
    else:
        print(0, end=' ') # 없으면 0으로 출력