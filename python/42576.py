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