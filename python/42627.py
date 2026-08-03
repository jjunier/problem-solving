import heapq

def solution(jobs):
    jobs = sorted([(req, duration, idx) for idx, (req, duration) in enumerate(jobs)])
    heap = []
    time = 0
    i = 0
    total = 0
    n = len(jobs)
    
    while i < n or heap:
        while i < n and jobs[i][0] <= time:
            req, duration, idx = jobs[i]
            heapq.heappush(heap, (duration, req, idx))
            i += 1
            
        if heap:
            duration, req, idx = heapq.heappop(heap)
            time += duration
            total += time - req
        else:
            time = jobs[i][0]
            
    return total // n
            