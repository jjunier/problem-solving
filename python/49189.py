from collections import deque

def bfs(graph, start, n):
    distance = [-1] * (n + 1)
    distance[start] = 0
    
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        
        for next_node in graph[current]:
            if distance[next_node] == -1:
                distance[next_node] = distance[current] + 1
                queue.append(next_node)

    return distance

def solution(n, vertex):
    """
    Args:
        n(Int): 노드의 갯수
        vertex(Matrix): 각 노드별로 이어진 간선의 정보가 담긴 이차원 리스트

    Returns:
        (Int): 1번 노드로부터 가장 멀리 떨어진 노드의 갯수
    """
    graph = [[] for _ in range(n + 1)]
    
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)

    distance = bfs(graph, 1, n)
                
    max_distance = max(distance)
    
    return distance.count(max_distance)