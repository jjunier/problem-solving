def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
        
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    
    if root_a != root_b:
        parent[root_b] = root_a
        return True
    
    return False
    

def solution(n, costs):
    """
    Args:
        n(Int): 섬의 갯수
        costs(Matrix): '섬 1, 섬 2, 다리 건설 비용'이 담긴 이차원 리스트
    
    Returns:
        (Int): 모든 섬이 서로 통행 가능한 최소 비용
    """
    parent = [i for i in range(n)]
    
    costs.sort(key=lambda x: x[2])
    
    total_cost = 0
    edge_count = 0
    
    for a, b, cost in costs:
        if union(parent, a, b):
            total_cost += cost
            edge_count += 1
            
        if edge_count == n - 1:
            break
            
    return total_cost