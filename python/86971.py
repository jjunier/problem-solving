from collections import deque


def bfs(start, graph, visited, cut_a, cut_b):
    # 3. BFS로 한쪽 전력망의 송전탑 개수를 센다.
    queue = deque([start])
    visited[start] = True

    count = 0

    while queue:
        current = queue.popleft()
        count += 1

        for next_node in graph[current]:
            if ((current == cut_a and next_node == cut_b)
                or current == cut_b and next_node == cut_a):
                continue

            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

    return count

def solution(n, wires):
    """
    Args:
        n(Int): 송전탑의 개수
        wires(Matrix): 각 두 송전탑을 잇는 전선의 정보가 담긴 이차원 리스트
    
    Returns:
        (Int): 하나의 전선을 끊어 두 개의 송전탑 집단별 개수의 차이의 최소값
    """
    graph = [[] for _ in range(n + 1)]

    # 1. 인접 리스트를 구성한다.
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    answer = n

    # 2. 전선을 하나씩 끊어본다.
    for cut_a, cut_b in wires:
        visited = [False] * (n + 1)

        count = bfs(cut_a, graph, visited, cut_a, cut_b)

        # 4. 두 전력망의 송전탑 수 차이를 계산한다.
        other_count  = n - count
        difference = abs(count - other_count)

        answer = min(answer, difference)

    return answer