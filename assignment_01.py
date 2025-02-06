import math
import time
from mpi4py import MPI

def get_all_primes(start, end):
    """function Returns a list of all primes up to the limit using sieve 
    of Eratosthenes algorithm"""
    if start < 2:
        start = 2
    prime_list = [True] * (end-start+1)
    for i in range(2, int(math.sqrt(end+1))+1):
        for j in range(max(i * i, (start + i - 1) // i * i), end+1, i):
            prime_list[j-start] = False
    return [i for i in range(start, end+1) if prime_list[i-start]]

def find_largest_gap(prime_list):
    """This function will return both the largest gap and the prime values
    in a 1d matrix that make up the gap"""
    max_gap = 0
    gap_vals = []
    for i in range(1, len(prime_list)-1):
        gap = prime_list[i] - prime_list[i-1]
        if gap > max_gap:
            max_gap = gap
            gap_vals = [prime_list[i-1], prime_list[i]]
    return max_gap, gap_vals

"""Main"""
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

LIMIT = 1000000000
chunk_size = LIMIT // size
start = rank * chunk_size + 1
end = (rank + 1) * chunk_size

start_time = time.time()

local_prime_list = get_all_primes(start, end)
local_max_gap, local_gap_vals = find_largest_gap(local_prime_list)

if local_prime_list:
    all_results = comm.gather((local_max_gap, local_gap_vals), root=0)
else:
    local_max_gap, local_gap_vals = 0, []   

total_time = time.time() - start_time

if rank == 0:
    global_max_gap = 0
    for result in all_results:
        max_gap, gap_vals = result
        if max_gap > global_max_gap:
            global_max_gap = max_gap
            global_gap_vals = gap_vals

    print("Largest gap:", global_max_gap)
    print("Gap Values:", global_gap_vals)
    print(f"Run Time: {total_time:.8f} seconds")