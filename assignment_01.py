import math
import time
from mpi4py import MPI

# FUNCTIONS
def get_all_primes(start, end):
    """function Returns a list of all primes up to the limit using sieve 
    of Eratosthenes algorithm"""
    if start < 2:
        start = 2 # To ensure we dont count 0 or 1 since 2 is the first prime in this case
    # Initiate List
    prime_list = [True] * (end-start+1)

    # Now check all numbers up to the sqrt
    for i in range(2, int(math.sqrt(end+1))+1):
        # Sieve of Eratosthenes Algorithm Stuff 
        for j in range(max(i * i, (start + i - 1) // i * i), end+1, i):
            # Mark non primes as False
            prime_list[j-start] = False
    return [i for i in range(start, end+1) if prime_list[i-start]] # Returns a list of needed vals

def find_largest_gap(prime_list):
    """This function will return both the largest gap and the prime values
    in a 1d matrix that make up the gap"""
    max_gap = 0
    gap_vals = []
    # For loop below will go through each val in the list and return the max and gap the vals
    for i in range(1, len(prime_list)-1):
        gap = prime_list[i] - prime_list[i-1]
        if gap > max_gap:
            max_gap = gap
            gap_vals = [prime_list[i-1], prime_list[i]]
    return max_gap, gap_vals

# MAIN PROCESS CODE

# Setup MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Setup chunks and limitations
LIMIT = 1000000000
chunk_size = LIMIT // size
start = rank * chunk_size + 1
end = (rank + 1) * chunk_size

# Start Timer
start_time = time.time()

# Get Local Values
loc_prime_list = get_all_primes(start, end)
loc_max_gap, loc_gap_vals = find_largest_gap(loc_prime_list)

# Get Results from All Processors
results = comm.gather((loc_max_gap, loc_gap_vals), root=0)

# End Timer
total_time = time.time() - start_time

# Print the final results if it is the root
if rank == 0:
    global_max_gap = 0
    # Get Max Result from Results
    for result in results:
        max_gap, gap_vals = result
        if max_gap > global_max_gap:
            global_max_gap = max_gap
            global_gap_vals = gap_vals
    # Printing Results
    print("Number of Processors: ", size)
    print("Largest gap:", global_max_gap)
    print("Gap Values:", global_gap_vals)
    print(f"Run Time: {total_time:.8f} seconds")