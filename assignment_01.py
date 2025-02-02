import math

def get_all_primes(limit):
    # Returns a list of all primes up to the limit using sieve algorithm
    prime_list = [True for i in range(limit+1)]
    prime_list[0] = prime_list[1] = False
    for i in range(2, int(math.sqrt(limit))+1):
        if prime_list[i]:
            j = i*i
            while j <= limit:
                prime_list[j] = False
                j += i
    return [i for i in range(limit+1) if prime_list[i]]

print(get_all_primes(20))

def find_largest_gap(limit) :
    return 0