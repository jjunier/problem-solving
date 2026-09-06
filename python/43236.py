def solution(distance, rocks, n):
    """
    Args:
        distance(Int): 출발 지점부터 도착 지점까지 떨어진 거리
        rocks(List): 도착 지점 내 위치한 바위 지점들이 담긴 리스트
        n(Int): 제거 가능한 바위의 갯수

    Returns:
        (Int): 임의의 바위 n개를 제거한 바위 사이의 거리 최소값 중 가장 큰 값 
    """
    rocks.sort()
    
    left = 1
    right = distance
    answer = 0
    
    while left <= right:
        mid = (left + right) //  2
        
        removed = 0
        previous = 0
        
        for rock in rocks:
            gap = rock - previous
            
            if gap < mid:
                removed += 1
                
            else:
                previous = rock
                
        if distance - previous < mid:
            removed += 1
            
        if removed <= n:
            answer = mid
            left = mid + 1
            
        else:
            right = mid - 1
            
    return answer