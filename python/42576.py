def solution(participant, completion):
    '''
    Args:
        participant: 마라톤 경기에 참여한 선수 리스트
        completion: 마라톤 경기를 완주한 선수 리스트
    
    Returns:
        마라톤 경기에 완주하지 못한 선수명    
    '''
        
    hash_map = {}
    
    for name in participant:
        hash_map[name] = hash_map.get(name, 0) + 1
    
    for name in completion:
        hash_map[name] -= 1
        
    for name in hash_map:
        if hash_map[name] != 0:
            return name
        

def solution(participant, completion):
    """
    Args:
        participant: 마라톤 참여자 명단 (List)
        completion: 마라톤 완주자 명단 (List)
    
    Returns:
        name: 단독 마라톤 미완주자 이름 (String)
    """
    counts = {}
    
    for name in participant:
        if name not in counts:
            counts[name] = 1
        else:
            counts[name] += 1
            
    for name in completion:
        counts[name] -= 1
        
    for name, count in counts.items():
        if count != 0:
            return name