def solution(sizes):
    """
    Args:
        sizes(List): 명함의 가로, 세로 길이가 한 쌍으로 담긴 이차원 리스트

    Returns:
        Result(Int): 모든 명함을 수납할 수 있는 가로 * 세로 크기의 정수
    """
    max_width = 0
    max_height = 0
    
    for w, h in sizes:
        if w < h:
            w, h = h, w
        
        max_width = max(max_width, w)
        max_height = max(max_height, h)
        
    return max_width * max_height