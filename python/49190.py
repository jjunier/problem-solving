def solution(arrows):
    """
    Args:
        arrows(List): 8개의 방향으로 0부터 7까지 표기된 이동하는 방향이 담긴 리스트

    Returns:
        (Int): 전체 이동 후, 사방이 막힌 도형(방)의 갯수
    """
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    
    x, y = 0, 0
    
    visited_nodes = set()
    visited_edges = set()
    
    visited_nodes.add((0, 0))
    
    answer = 0
    
    for direction in arrows:
        for _ in range(2):
            nx = x + dx[direction]
            ny = y + dy[direction]
            
            current = (x, y)
            next_node = (nx, ny)
            
            edge = (current, next_node)
            reverse_edge = (next_node, current)
            
            if(next_node in visited_nodes
              and edge not in visited_edges):
                answer += 1
                
            visited_nodes.add(next_node)
            
            visited_edges.add(edge)
            visited_edges.add(reverse_edge)
            
            x, y = nx, ny
            
    return answer