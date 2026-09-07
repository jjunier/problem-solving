def solution(n, results):
    """
    Args:
        n(Int): 권투 대회에 참여하는 권투 선수의 수
        result(Matrix): 각 권투 선수의 번호로 표현해 승패가 담긴 이차원 리스트

    Returns:
        (Int): 정확하게 순위를 매길 수 있는 선수의 수
    """
    win = [[False] * (n + 1) for _ in range(n + 1)]
    
    for winner, loser in results:
        win[winner][loser] = True
        
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if win[i][k] and win[k][j]:
                    win[i][j] = True
                    
    answer = 0
    
    for player in range(1, n + 1):
        known = 0
        
        for other in range(1, n + 1):
            if player == other:
                continue
                
            if win[player][other] or win[other][player]:
                known += 1
                
        if known == n - 1:
            answer += 1
            
    return answer