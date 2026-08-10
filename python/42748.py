def solution(array, commands):
    """
    Args:
        array(List): 정렬할 숫자가 담긴 리스트
        commands(Matrix): i번째부터 j번째 숫자를 자르고 정렬한 후, k번째 숫자가 담긴 이차원 리스트

    Returns:
        (List): commands의 결과들이 담긴 정수형 리스트
    """
    answer = []
    
    for i, j, k in commands:
        sliced = sorted(array[i-1:j])
        answer.append(sliced[k-1])
    
    return answer