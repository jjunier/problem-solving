from collections import deque

def solution(n, wires):
    answer = n
    
    for i in range(len(wires)):
        graph = n
        
        for  i in range(len(wires)):
            graph = [[] for _ in range(n + 1)]
            
            for j, (a, b) in enumerate(wires):
                if i == j:
                    continue
                graph[a].append(b)
                graph[b].append(a)
            visited = [False] * (n + 1)
            queue = deque([1])
            visited[1] = True
            count = 1
            
            while queue:
                now = queue.popleft()
                
                for nxt in graph[now]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        queue.append(nxt)
                        count += 1
                        
            answer = min(answer, abs((n - count) - count))
            
    return answer