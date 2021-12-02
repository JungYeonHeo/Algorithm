import math 

def solution(progresses, speeds):
    answer = []
    days = []
    num = 1
    i = 0
    for p in range(0, len(progresses)):
        days.append(math.ceil((100 - progresses[p]) / speeds[p]))
    print(days)
    while i <= len(days) - 1:
        for j in range(i+1, len(days)):
            if days[i] >= days[j]:
                num = num + 1
            else:
                break
        answer.append(num)
        i = i + num
        num = 1
    
    return answer