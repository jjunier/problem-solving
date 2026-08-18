def solution(routes):
    """
    Args:
        routes(Matrix): 차량의 이동 경로가 '진입 시점, 나간 시점' 쌍으로 존재하는 이차원 리스트

    Returns:
        (Int): 모든 차량이 최소 한 번은 단속 카메라를 만나기 위해 필요한 최소한의 카메라 갯수

    """
    routes.sort(key=lambda x: x[1])
    
    camera = None
    answer = 0
    
    for start, end in routes:
        if camera is None or start > camera:
            camera = end
            answer += 1
    
    return answer