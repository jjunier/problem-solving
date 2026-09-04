def solution(n, times):
    """
    Args:
        n(Int): 입국 심사를 기다리는 사람의 수
        times(List): 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 리스트

    Returns:
        (Int): 모든 사람이 입국 심사를 받는 데에 걸리는 최소 시간
    """
    left = 1
    right = max(times) * n
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        people = 0
        
        for time in times:
            people += mid // time
            
        if people >= n:
            answer = mid
            right = mid - 1
            
        else:
            left = mid + 1
            
    return answer