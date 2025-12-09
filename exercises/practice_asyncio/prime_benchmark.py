import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def get_primes(limit: int) -> list[int]:
    """
    Calculates prime numbers up to a given limit using the Sieve of Eratosthenes.
    """
    primes = []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for multiple in range(i*i, limit + 1, i):
                sieve[multiple] = False
    for i in range(2, limit + 1):
        if sieve[i]:
            primes.append(i)
    return primes

if __name__ == '__main__':
    upper_limit = 10000000

    # Sequential execution
    start_time = time.time()
    for _ in range(4):
        get_primes(upper_limit)
    end_time = time.time()
    print(f"Total execution time for 4 sequential calls: {end_time - start_time:.4f} seconds")

    # Concurrent execution with ThreadPoolExecutor
    start_time = time.time()
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_primes, upper_limit) for _ in range(4)]
        for future in futures:
            future.result()
    end_time = time.time()
    print(f"Total execution time for 4 ThreadPoolExecutor calls: {end_time - start_time:.4f} seconds")

    # Concurrent execution with ProcessPoolExecutor
    start_time = time.time()
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(get_primes, upper_limit) for _ in range(4)]
        for future in futures:
            future.result()
    end_time = time.time()
    print(f"Total execution time for 4 ProcessPoolExecutor calls: {end_time - start_time:.4f} seconds")
