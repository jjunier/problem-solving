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
    waiting_trucks = deque(truck_weights)
    bridge_on_trucks = deque()
    
    time = 0
    current_weight = 0
    
    while waiting_trucks or bridge_on_trucks:
        time += 1
        
        # 다리를 모두 건넌 트럭 제거하기
        if bridge_on_trucks and time - bridge_on_trucks[0][1] == bridge_length:
            truck_weight, entered_time = bridge_on_trucks.popleft()
            current_weight -= truck_weight
            
        # 다음 트럭이 다리에 진입할 수 있는지 검사하기
        if waiting_trucks:
            next_truck = waiting_trucks[0]
            
            if(
                len(bridge_on_trucks) < bridge_length 
               and current_weight + next_truck <= weight
              ):
                next_truck = waiting_trucks.popleft()
                bridge_on_trucks.append((next_truck, time))
                current_weight += next_truck
                
    return time