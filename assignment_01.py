import math

def get_all_primes(limit):
    # Returns a list of all primes up to the limit
    prime_list = []
    prime_list.append(2)
    for i in range(3, limit+1, 2):
        is_prime = True
        for j in range(3, i+1, 2):
            if i % j == 0 and i != j:
                is_prime = False
        if is_prime:
            prime_list.append(i)
    return prime_list

print(get_all_primes(200))

def find_largest_gap(limit) :
    return 0