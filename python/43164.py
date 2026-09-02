from collections import defaultdict

def dfs(airport, graph, route):
    while graph[airport]:
        next_airport = graph[airport].pop()
        dfs(next_airport, graph, route)
        
    route.append(airport)
    
def solution(tickets):
    """
    Args:
        tickets(List): '출발공항, 도착공항' 쌍으로 담긴 이차원 리스트

    Returns:
        (List): 모든 공항을 방문하는 공항 경로가 담긴 리스트
    """
    graph = defaultdict(list)
    
    for start, end in tickets:
        graph[start].append(end)
        
    for airport in graph:
        graph[airport].sort(reverse=True)
        
    route = []
    
    dfs("ICN", graph, route)
    
    return route[::-1]