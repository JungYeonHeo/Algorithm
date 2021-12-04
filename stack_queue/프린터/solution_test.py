def solution(priorities, location):
    answer = 1
    
    for i in range(0, len(priorities)):
        maxValue = priorities.index(max(priorities))
        
        if location == maxValue:
            break
        else:
            answer = answer + 1 
            priorities.pop(maxValue)

            for i in range(0, maxValue):
                priorities.append(priorities.pop(0))
            print(priorities)
                
            if location < maxValue:
                location = location + len(priorities) - maxValue
            else:
                location = location - 1 - maxValue

    return answer