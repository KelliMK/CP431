import math
import time

def get_all_primes(limit):
    """function Returns a list of all primes up to the limit using sieve 
    of Eratosthenes algorithm"""
    prime_list = [True for i in range(limit+1)]
    prime_list[0] = prime_list[1] = False
    for i in range(2, int(math.sqrt(limit))+1):
        if prime_list[i]:
            for j in range(i*i, limit+1, i):
                prime_list[j] = False
    return [i for i in range(limit+1) if prime_list[i]]

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
    return gap, gap_vals

"""Main"""

# Setting up timer
start = time.time()

# Run functions
prime_list = get_all_primes(100000000) # 100,000,000 takes approx. 9 seconds rn
largest_gap, gap_vals = find_largest_gap(prime_list)

run_time = time.time() - start

print("Largest gap: ", largest_gap)
print("Gap Values: ", gap_vals)
print(f"Run Time: {run_time:.8f} seconds") 