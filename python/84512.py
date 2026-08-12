def solution(word):
    answer = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    weights = [781, 156, 31, 6, 1]
    
    for i, ch in enumerate(word):
        answer += vowels.index(ch) * weights[i] + 1
    
    return answer