'''
문제: 길이가 제각각인 K개의 랜선이 있다. 
이 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다.
편의를 위해 랜선을 자를 때 손실되는 길이는 없다고 가정하며,
기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정한다.
그리고 자를 때 항상 센티미터 단위로 정수 길이만큼 자르고 N개 보다 많이 만드는 것도 N개를 만드는 것에 포함된다.
이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성

첫째 줄에 이미 가자고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력
그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위로 주어진다.

4 11
802
743
457
539
'''

# 결정 알고리즘: 특정 범위에 있는 조건에 맞는 무엇가를 찾는 문제에서 사용 -> 이분 검색 사용 
import sys
sys.stdin = open("input.txt", "r")
def Count(len): # 랜선 한개의 길이를 매개변수로 받음
    cnt = 0
    for x in Line:
        cnt += (x // len)
    return cnt

k, n = map(int, input().split())
Line = []
res = 0
largest = 0
for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp)
lt = 1
rt = largest
while lt <= rt: # 이분검색이 끝날때까지
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)








