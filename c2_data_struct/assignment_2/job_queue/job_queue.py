# python3
from heapq import *


class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))

        # For testing
        # with open('./tests/08') as f:
        #     self.num_workers, m = map(int, f.readline().split())
        #     self.jobs = list(map(int, f.read().split()))

        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs_naive(self):
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
            next_worker = 0
            for j in range(self.num_workers):
                if next_free_time[j] < next_free_time[next_worker]:
                    next_worker = j
            self.assigned_workers[i] = next_worker
            self.start_times[i] = next_free_time[next_worker]
            next_free_time[next_worker] += self.jobs[i]

    def assign_jobs(self):
        pq = [[0, i] for i in range(self.num_workers)]  # priority queue
        heapify(pq)
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        for i in range(len(self.jobs)):
            worker = heappop(pq)
            self.assigned_workers[i] = worker[1]  # worker id
            self.start_times[i] = worker[0]
            worker[0] += self.jobs[i]
            heappush(pq, worker)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

    # with open('./tests/08.a') as f:
    #     cr = f.read().split()
    # id_ = [int(s) for s in cr[::2]]
    # time_ = [int(s) for s in cr[1::2]]
    # print(len(id_))
    # if job_queue.assigned_workers != id_:
    #     print('Wrong worker')
    # if job_queue.start_times != time_:
    #     print('Wrong time')
    # else:
    #     print('Passed')
