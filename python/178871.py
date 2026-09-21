def solution(players, callings):
    """
    Args:
        players(List): 달리기 경주에 참여하는 선수들의 현재 등수대로 이름이 담긴 리스트
        callings(List): 추월에 성공해 해설진에게 호명된 선수 이름이 담긴 리스트

    Returns:
        (List): 경주가 끝난 후의 1등부터 등수 순서대로 선수 이름들이 담긴 리스트
    """
    positions = {
        player: index
        for index, player in enumerate(players)
    }
    
    for called_player in callings:
        current_index = positions[called_player]
        front_index = current_index - 1
        
        front_player = players[front_index]
        
        players[current_index], players[front_index] = (
            players[front_index],
            players[current_index],
        )
        
        positions[called_player] = front_index
        positions[front_player] = current_index
        
    return players