def solution(n):
    """
    Args:
        n(Int): 타일링을 위한 타일의 가로 길이

    Returns:
        (Int): n * 3의 판을 타일링하는 모든 경우의 수
    """
    MOD = 1_000_000_007
    
    tiling_count = [1, 1, 3, 10] + [0] * (n - 3)
    special_cases  = [12, 2, 4]
    
    if n <= 3:
        return tiling_count[n]
    
    for width in range(4, n + 1):
        cycle = width % 3
        
        tiling_count[width] = (special_cases[cycle] + tiling_count[width - 1] + 2 * tiling_count[width - 2] + 5 * tiling_count[width - 3])
        
        special_cases[cycle] += (2 * tiling_count[width - 1] + 2 * tiling_count[width - 2] + 4 * tiling_count[width - 3])
        
    return tiling_count[n] % MOD