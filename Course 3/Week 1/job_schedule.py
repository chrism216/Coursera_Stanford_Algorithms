import os
from copy import deepcopy

def get_jobs(file_name):
    this_folder = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(this_folder, file_name)
    job_list = []
    with open(my_file) as f:
        for i, line in enumerate(f):
            if i > 0:
                weight = int(line.strip().split()[0])
                length = int(line.strip().split()[1])
                diff = weight - length
                job_list.append((diff, weight, length))
    return job_list

def completion_time(jobs):
    c = 0
    total_weighted_completion_time = 0
    for job in jobs:
        c += job[2]
        total_weighted_completion_time += c * job[1]
    return total_weighted_completion_time


if __name__ == "__main__":
    jobs = get_jobs("jobs.txt")
    jobs_by_diff = sorted(deepcopy(jobs), key=lambda x: (-x[0], -x[1]))
    
    print(completion_time(jobs_by_diff))

    jobs_by_ratio = sorted(deepcopy(jobs), key=lambda x: (-x[0]/x[1]))
    print(completion_time(jobs_by_ratio))
