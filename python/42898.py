def solution(m, n, puddles):
    """
    Args:
        m(Int): 격자의 가로 크기
        n(Int): 격자의 세로 크기
        puddles(Matrix): 물에 잠긴 지역의 좌표값이 담긴 이차원 리스트

    Returns:    
        (Int): 오른쪽과 아래쪽으로만 움직여 집에서 학교로 갈 수 있는 최단 경로의 갯수
    """
    MOD = 1_000_000_007
    
    path_count = [[0] * (m + 1) for _ in range(n + 1)]
    path_count[1][1] = 1
    
    puddle_set = set((y, x) for x, y in puddles)
    
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if (y, x) in puddle_set:
                path_count[y][x] = 0
                continue
                
            if y == 1 and x == 1:
                continue
                
            path_count[y][x] = (path_count[y-1][x] + path_count[y][x-1]) % MOD
            
    return path_count[n][m]