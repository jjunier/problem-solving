def solution(triangle):
    """
    Args:
        triangle(Matrix): 상각형의 정보가 담긴 이차원 리스트

    Returns:
        (Int): 꼭대기에서 바닥으로 오른쪽 또는 왼쪽 대각선으 방향으로 거쳐 가는데 만들 수 있는 최댓값
    """
    dp = [row[:] for row in triangle]

    for i in range(1, len(dp)):
        for j in range(len(dp[i])):
            if j == 0:
                dp[i][j] += dp[i - 1][j]
            elif j == len(dp[i]) - 1:
                dp[i][j] += dp[i - 1][j - 1]
            else:
                dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

    return max(dp[-1])