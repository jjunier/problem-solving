import heapq

def solution(scoville, K):
    """
    Args:
        scoville(List): 모든 음식의 스코빌 지수가 담긴 정수형 리스트
        K(Int): 음식의 목표 스코빌 지수

    Returns:
        count(Int): 모든 음식을 목표 스코빌 지수(K) 이상으로 만들기 위한 음식 섞기 최소 횟수 
    """
    heapq.heapify(scoville)
    count = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        mixed = first + (second * 2)
        
        heapq.heappush(scoville, mixed)
        count += 1
        
    return count