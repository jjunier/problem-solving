def solution(citations):
    """
    Args:
        citations(List): 어떤 과학자가 발표한 갹 논문별 인용 횟수

    Returns:
        h_index(Int): 연구자가 발표한 논문의 양과 질을 동시에 평가하는 수치 지표인 h_index
    """
    citations.sort(reverse=True)
    
    h_index = 0
    
    for index, citation in enumerate(citations):
        paper_count = index + 1
        
        if citation >= paper_count:
            h_index = paper_count
            
        else:
            break
            
    return h_index