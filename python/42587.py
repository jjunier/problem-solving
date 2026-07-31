from collections import deque

def solution(priorities, location):
    """
    Args:
        priorities(List): 실행 대기 큐에 위치한 프로세스 중요도를 담은 정수형 리스트
        location(Int): 몇 번째로 실행되는지 알고 싶은 프로세스(인덱스) 위치

    Returns:
        execution_order(Int): 해당 프로세스가 몇 번째로 실행되는 지에 대한 번호
    """
    queue = deque()
    
    for index, priority in enumerate(priorities):
        queue.append((priority, index))
    
    execution_order = 0
    
    while queue:
        current_priority, current_index = queue.popleft()
        
        if any(priority > current_priority for priority, index in queue):
            queue.append((current_priority, current_index))
        else:
            execution_order += 1
            
            if current_index == location:
                return execution_order