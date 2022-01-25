# 프로그래머스 동적계획법 정수 삼각형

def preOrder(triangle, sum_list, row, col):
    if len(triangle) == row: return 0
    if sum_list[row][col] > 0: return sum_list[row][col]
    sum_list[row][col] = triangle[row][col] + max(preOrder(triangle, sum_list, row + 1, col), preOrder(triangle, sum_list, row + 1, col + 1))
    return sum_list[row][col]

def solution(triangle):
    sum_list = [[0] * len(triangle[i]) for i in range(len(triangle))] 
    return preOrder(triangle, sum_list, 0, 0)