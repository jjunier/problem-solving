def solution(triangle):
    """
    Args:
        triangle(Matrix): 상각형의 정보가 담긴 이차원 리스트

    Returns:
        (Int): 꼭대기에서 바닥으로 오른쪽 또는 왼쪽 대각선의 방향으로 거쳐 가는데 만들 수 있는 최댓값
    """
    triangle_info = [row[:] for row in triangle]
    
    for i in range(1, len(triangle_info)):
        for j in range(len(triangle_info[i])):
            if j == 0:
                triangle_info[i][j] += triangle_info[i - 1][j]
                
            elif j == i:
                triangle_info[i][j] += triangle_info[i - 1][j - 1]
                
            else:
                triangle_info[i][j] += max(triangle_info[i - 1][j], triangle_info[i - 1][j - 1])
                
    return max(triangle_info[-1])