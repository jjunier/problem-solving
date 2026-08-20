from collections import deque

def can_change(word1, word2):
    diff = 0
    
    for a, b in zip(word1, word2):
        if a != b:
            diff += 1
            
    return diff == 1

def solution(begin, target, words):
    """
    Args:
        begin(String): 한 번에 하나의 알파벳만 바꿀 시작 영단어
        target(String): 목표 영단어
        words(List): 바꿀 수 있는 영단어들을 모아둔 리스트

    Returns:
        (Int): begin 단어를 words 리스트 내의 단어들 중 target 단어로 바꾸기 위한 최소한의 단계 횟수
    """
    if target not in words:
        return 0
    
    visited = [False] * len(words)
    
    queue = deque()
    queue.append((begin, 0))
    
    while queue:
        current_word, count = queue.popleft()
        
        if current_word == target:
            return count
        
        for i in range(len(words)):
            if(not visited[i] and can_change(current_word, words[i])):
                visited[i] = True
                queue.append((words[i], count + 1))
                
    return 0