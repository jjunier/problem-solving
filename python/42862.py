def solution(n, lost, reserve):
    """
    Args:
        n(Int): 전체 학생의 수
        lost(List): 체육복을 도난 당한 학생들의 번호가 담긴 리스트
        reserve(List): 여벌의 체육복을 가져온 학생들의 번호가 담긴 리스트

    Returns:
        (Int): 체육복을 가지고 있어 수업을 들을 수 있는 학생의 최댓값
    """
    real_lost = set(lost) - set(reserve)
    real_reserve = set(reserve) - set(lost)
    
    for student in sorted(real_reserve):
        if student - 1 in real_lost:
            real_lost.remove(student - 1)

        elif student + 1 in real_lost:
            real_lost.remove(student + 1)
            
    return n - len(real_lost)