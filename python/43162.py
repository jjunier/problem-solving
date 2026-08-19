def dfs(node, computers, visited):
    visited[node] = True
    
    for next_node in range(len(computers)):
        if computers[node][next_node] == 1 and not visited[next_node]:
            dfs(next_node, computers, visited)

def solution(n, computers):
    """
    Args:
        n(Int): 네트워크를 연결할 컴퓨터 총 갯수
        computers(Matrix): 각 컴퓨터 별 연결 여부가 담긴 이차원 리스트

    Returns:
        network(Int): 각 컴퓨터끼리 연결된 네트워크의 갯수
    """
    visited = [False] * n
    network = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(i, computers, visited)
            network += 1
        
    return network