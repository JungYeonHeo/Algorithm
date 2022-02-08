# 프로그래머스 배달

import math
def solution(N, road, K):
    answer = 0
    roads = [[math.inf for i in range(N)] for j in range(N)]
    for r in road:
        if roads[r[1] - 1][r[0] - 1] > r[2]:
            roads[r[1] - 1][r[0] - 1] = r[2]
            roads[r[0] - 1][r[1] - 1] = r[2]

    for i in range(N):
        roads[i][i] = 0

    for path in range(N):
        for i in range(N):
            for j in range(N):
                if roads[i][j] > roads[i][path] + roads[path][j]:
                    roads[i][j] = roads[i][path] + roads[path][j]

    for i in range(N):
        if roads[0][i] <= K:
            answer += 1

    return answer