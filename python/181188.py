def solution(targets):
    """
    Args:
        targets(Matrix): 각 폭격 미사일의 x좌표 범위 (s, e)가 담긴 이차원 리스트

    Returns:
        (Int): 모든 폭격 미사일을 요격하기 위해 필요한 최소한의 요격 미사일 수
    """
    targets.sort(key=lambda x: x[1])
    
    answer = 0 
    last_end = -1
    
    for start, end in targets:
        if start >= last_end:
            answer += 1
            last_end = end
            
    return answer