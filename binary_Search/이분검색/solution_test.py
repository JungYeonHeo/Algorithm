"""
문제: 임의의 N개의 숫자가 입력으로 주어진다.
N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한 개의 수인 M이 주어지면 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 출력하는 프로그램
"""

import sys
sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort() # 오름차순 정렬(이분 검색은 정렬되어 있어야 함)
lt = 0
rt = n - 1
while lt <= rt:
    mid = (lt + rt) // 2 # 중간 index
    if a[mid] == m:
        print(mid + 1)
        break
    elif a[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1