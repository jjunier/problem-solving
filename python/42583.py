from collections import deque
from typing import List

def solution(bridge_length: int, weight: int, truck_weights: List[int]) -> int:
    """
    Args:
        bridge_width(Int): 다리의 길이
        weight(Int): 무게를 견딜 수 있는 다리의 하중
        truck_weights[List]: 각 트럭별 무게가 기록된 리스트

    Returns:
        (Int): 모든 트럭이 다리를 건너는 데에 걸리는 최소 시간(초)
    """
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    current_weight = 0
    time = 0
    
    while bridge:
        time += 1
        current_weight -= bridge.popleft()
        
        if trucks:
            if current_weight + trucks[0] <= weight:
                truck = trucks.popleft()
                bridge.append(truck)
                current_weight += truck
            
            else:
                bridge.append(0)
                
        if not trucks and current_weight == 0:
            break
            
    return time
            

