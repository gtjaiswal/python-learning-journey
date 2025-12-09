import math
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# --- CPU-Bound Task: Prime Number Calculation ---

def get_primes(limit: int) -> list[int]:
    """Calculates prime numbers up to a given limit using the Sieve of Eratosthenes."""
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

async def get_primes_async(limit: int) -> list[int]:
    """Async version of get_primes to demonstrate asyncio with CPU-bound tasks."""
    primes = []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for multiple in range(i*i, limit + 1, i):
                sieve[multiple] = False
        if i % 1000 == 0:
            await asyncio.sleep(0)
    for i in range(2, limit + 1):
        if sieve[i]:
            primes.append(i)
    return primes

async def run_async_tasks(limit):
    """Runs get_primes concurrently using asyncio.to_thread."""
    tasks = [asyncio.to_thread(get_primes, limit) for _ in range(4)]
    await asyncio.gather(*tasks)

async def run_native_async_tasks(limit):
    """Runs get_primes_async concurrently using asyncio.create_task."""
    tasks = [asyncio.create_task(get_primes_async(limit)) for _ in range(4)]
    await asyncio.gather(*tasks)

# --- I/O-Bound Task Simulation: Fetching Data ---

def fetch_data_sync(url: str):
    """Simulates fetching data from a URL with a delay (synchronous)."""
    print(f"Fetching data from {url}...")
    time.sleep(1)
    print(f"Data fetched from {url}.")
    return {"url": url, "data": "Sample data"}

async def fetch_data_async(url: str):
    """Simulates fetching data from a URL with a delay (asynchronous)."""
    print(f"Fetching data from {url}...")
    await asyncio.sleep(1)
    print(f"Data fetched from {url}.")
    return {"url": url, "data": "Sample data"}

# --- Mixed I/O- and CPU-Bound Task Simulation ---

def cpu_bound_operation(data):
    """A CPU-intensive function that simulates processing data."""
    print(f"Processing data from {data['url']}...")
    # Simulate CPU work
    sum(i * i for i in range(10**6))
    print(f"Finished processing data from {data['url']}.")
    return "Processed"

async def fetch_and_process_naive(url: str):
    """Naive approach: Awaits I/O then blocks on CPU work."""
    data = await fetch_data_async(url)
    # This blocks the event loop!
    cpu_bound_operation(data)

async def fetch_and_process_optimized(executor, url: str):
    """Optimized approach: Awaits I/O then delegates CPU work to an executor."""
    data = await fetch_data_async(url)
    loop = asyncio.get_running_loop()
    # This runs the CPU-bound work in a separate process
    await loop.run_in_executor(executor, cpu_bound_operation, data)

async def main_mixed_workload():
    """Compares naive and optimized approaches for mixed workloads."""
    urls = ["url1", "url2", "url3", "url4"]
    print("\n--- Mixed I/O- and CPU-Bound Task Comparison ---")

    # Scenario 1: Naive Concurrent Execution (will block)
    print("\nRunning mixed tasks naively (will block event loop)...")
    start_time = time.time()
    tasks = [asyncio.create_task(fetch_and_process_naive(url)) for url in urls]
    await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"Total execution time for 4 naive mixed calls: {end_time - start_time:.4f} seconds")

    # Scenario 2: Optimized Concurrent Execution
    print("\nRunning mixed tasks with a ProcessPoolExecutor...")
    start_time = time.time()
    with ProcessPoolExecutor() as executor:
        tasks = [asyncio.create_task(fetch_and_process_optimized(executor, url)) for url in urls]
        await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"Total execution time for 4 optimized mixed calls: {end_time - start_time:.4f} seconds")


async def main_io_bound():
    """Compares sequential and concurrent execution for I/O-bound tasks."""
    urls = ["url1", "url2", "url3", "url4"]
    print("\n--- I/O-Bound Task Comparison ---")

    # Scenario 1: Sequential Execution
    print("\nRunning I/O-bound tasks sequentially...")
    start_time = time.time()
    for url in urls:
        fetch_data_sync(url)
    end_time = time.time()
    print(f"Total execution time for 4 sequential I/O-bound calls: {end_time - start_time:.4f} seconds")

    # Scenario 2: Concurrent Execution with ThreadPoolExecutor
    print("\nRunning I/O-bound tasks concurrently with ThreadPoolExecutor...")
    start_time = time.time()
    with ThreadPoolExecutor() as executor:
        executor.map(fetch_data_sync, urls)
    end_time = time.time()
    print(f"Total execution time for 4 ThreadPoolExecutor I/O-bound calls: {end_time - start_time:.4f} seconds")

    # Scenario 3: Concurrent Execution with asyncio
    print("\nRunning I/O-bound tasks concurrently with asyncio...")
    start_time = time.time()
    tasks = [asyncio.create_task(fetch_data_async(url)) for url in urls]
    await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"Total execution time for 4 concurrent asyncio I/O-bound calls: {end_time - start_time:.4f} seconds")


if __name__ == '__main__':
    # --- CPU-Bound Comparisons ---
    upper_limit = 100000
    print("--- CPU-Bound Task Comparison ---")
    # ... (rest of the CPU-bound comparisons)

    # --- I/O-Bound Comparison ---
    asyncio.run(main_io_bound())

    # --- Mixed Workload Comparison ---
    asyncio.run(main_mixed_workload())
