def solution(people, limit):
    """
    Args:
        people(List): 무인도에 갇힌 사람들의 몸무게
        limit(Int): 2인승 구명 보트의 무게 제한

    Returns:
        (Int): 모든 사람을 구출하기 위한 구명 보트를 최대한 적게 운용한 횟수
    """
    people.sort()
    
    left = 0
    right = len(people) - 1
    answer = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
            answer += 1
        
        else:
            right -= 1
            answer += 1
    
    return answer