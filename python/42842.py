def solution(brown, yellow):
    """
    Args:
        brown(Int): 카펫의 테두리 타일의 갯수 (8개 이상 5,000개 이하)
        yellow(Int): 카펫의 내부 타일의 갯수 (1개 이상 2,000,000개 이하)

    Returns:
        (List): 카펫의 가로, 세로 타일의 갯수가 담긴 리스트
    """
    total_grid = brown + yellow
    
    for height in range(1, int(yellow ** 0.5) + 1):
        if yellow % height == 0:
            width = yellow // height
            
            carpet_width = width + 2
            carpet_height = height + 2
            
            if carpet_width * carpet_height == total_grid:
                return [carpet_width, carpet_height]