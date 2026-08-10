import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    valid = [False] * len(operations)
    
    for index, operation in enumerate(operations):
        command, value = operation.split()
        value = int(value)
        
        if command == "I":
            heapq.heappush(min_heap, (value, index))
            heapq.heappush(max_heap, (-value, index))
            valid[index] = True
            
        else:
            if value == 1:
                # 최대 힙에서 이미 삭제된 원소를 제거
                while max_heap and not valid[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                    
                if max_heap:
                    _, target_index = heapq.heappop(max_heap)
                    valid[target_index] = False
                    
            else:
                # 최소 힙에서 이미 삭제된 원소를 제거
                while min_heap and not valid[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                    
                if min_heap:
                    _, target_index = heapq.heappop(min_heap)
                    valid[target_index] = False
                    
    # 마지막으로 무효 원소를 정리
    while min_heap and not valid[min_heap[0][1]]:
        heapq.heappop(min_heap)
        
    while max_heap and not valid[max_heap[0][1]]:
        heapq.heappop(max_heap)
        
    if not min_heap:
        return [0, 0]
    
    return [-max_heap[0][0], min_heap[0][0]]
                    