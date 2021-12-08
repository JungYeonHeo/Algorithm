import heapq

def solution(scoville, K):
    answer = 0
    
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)
    
    for i in range(len(scoville)-1):
        if heap[0] >= K:
            break
        else:
            heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
            answer += 1
    
    if heap[0] < K:
        return -1 
    
    return answer