import heapq

def solution(jobs):
    """
    Args:
        jobs(Matrix): [요청 시간, 소요 시간] 쌍을 갖는 2차원 리스트

    Returns:
        (Int): 모든 요청 작업의 반환 시간에 대한 평균
    """
    jobs_with_number = []
    
    for job_number, (request_time, duration) in enumerate(jobs):
        jobs_with_number.append((request_time, duration, job_number))
        
    jobs_with_number.sort()
    waiting_heap = []
    current_time = 0
    job_index = 0
    completed_count = 0
    total_turnaround = 0
    
    while completed_count < len(jobs):
        
        while (job_index < len(jobs_with_number) 
               and jobs_with_number[job_index][0] <= current_time
              ):
            request_time, duration, job_number = jobs_with_number[job_index]
            
            heapq.heappush(waiting_heap, (duration, request_time, job_number))
            
            job_index += 1
            
        if waiting_heap:
            duration, request_time, job_number = heapq.heappop(waiting_heap)
            
            current_time += duration
            total_turnaround += current_time - request_time
            completed_count += 1
            
        else:
            current_time = jobs_with_number[job_index][0]
            
    return total_turnaround // len(jobs)