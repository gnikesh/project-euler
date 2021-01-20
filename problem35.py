"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from itertools import permutations

def is_prime(num):
    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            return False

    return True

def get_rotations(num):
    rotations_list = []
    digits_array = list(str(num))
    n = len(digits_array)

    # [1, 2, 3, 4]
    for i in range(n):
        first = digits_array[0]
        k = 0
        for i in range(n - 1):
            digits_array[k % n] = digits_array[(k + 1) % n]
            k += 1 

        digits_array[n - 1] = first
        rotations_list.append(int("".join(digits_array)))

    return rotations_list




if __name__ == "__main__":
    range_to_search = 1000000
    all_prime_count = 0

    for i in range(2, range_to_search):
        all_primes = True
        for n in get_rotations(i):
            if not all_primes:
                break

            if not is_prime(n):
                all_primes = False

        if all_primes:
            all_prime_count += 1

    print(all_prime_count)



    
