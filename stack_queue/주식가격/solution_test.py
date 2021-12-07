def solution(prices):
    answer = []
    num = 0
    for i in range(len(prices)-1):
        num = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                num = num + 1 
            else:
                num = j - i 
                break
        answer.append(num)            
    answer.append(0)
                
    return answer