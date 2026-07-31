import math

def solution(progresses, speeds):
    """
    Args:
        progress(List): 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수형 리스트
        speeds(List): 각 작업의 개발 속도가 적힌 정수형 리스트

    Returns:
        (List): 각 배포마다 몇 개의 기능이 배포되는 지에 대한 리스트
    """
    days = []
    
    for progress, speed in zip(progresses, speeds):
        required_day = math.ceil((100 - progress) / speed)
        days.append(required_day)
        
    answer = []
    
    current_release_day = days[0]
    count = 1
    
    for day in days[1:]:
        if day <= current_release_day:
            count += 1
        else:
            answer.append(count)
            current_release_day = day
            count = 1
        
    answer.append(count)
        
    return answer