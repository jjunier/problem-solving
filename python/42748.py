def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        sliced = sorted(array[i-1:j])
        answer.append(sliced[k-1])
    
    return answer