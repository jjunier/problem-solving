def solution(answers):
    """
    Args:
        answers(List): 5지선다형 수학 문제의 정답이 담긴 리스트

    Returns:
        result(List): 수포자 3인 중 가장 많은 문항의 정답자가 담긴 정수형 리스트(오름차순)
    
    """
    person_1 = [1,2,3,4,5]
    person_2 = [2,1,2,3,2,4,2,5]
    person_3 = [3,3,1,1,2,2,4,4,5,5]
    
    scores = [0, 0, 0]
    
    for index, answer in enumerate(answers):
        if person_1[index % len(person_1)] == answer:
            scores[0] += 1
            
        if person_2[index % len(person_2)] == answer:
            scores[1] += 1
            
        if person_3[index % len(person_3)] == answer:
            scores[2] += 1
            
    max_score = max(scores[0], scores[1], scores[2])
    
    result = []
    
    for index, score in enumerate(scores):
        if score == max_score:
            result.append(index + 1)
            
    return result