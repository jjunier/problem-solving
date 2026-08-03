import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    
    while len(scoville) > 1 and scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        mixed = first + (second * 2)
        heapq.heappush(scoville, mixed)
        count += 1
        
    return count if scoville[0] >= K else - 1