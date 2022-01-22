# 백준 10829 이진수 변환 

def DFS(x):
    if x == 0:
        return #함수 종료
    else:
        DFS(x//2)
        print(x%2, end='')

n = int(input())
DFS(n)