from itertools import permutations

def solution(k, dungeons):
    """
    Args:
        k(int): 게임 내 한 유저의 피로도 잔여량
        dungeons(Matrix): 각 던전 별 '최소 필요 피로도, 소요 피로도'가 담긴 이차원 리스트

    Returns:
        max_count(Int): 유저가 탐험 가능한 최대 던전의 갯수
    """
    max_count = 0
    
    for order in permutations(dungeons):
        current_fatigue = k
        count = 0
        
        for required, cost in order:
            if current_fatigue >= required:
                current_fatigue -= cost
                count += 1
                
            else:
                break
                
        max_count = max(max_count, count)
        
    return max_count