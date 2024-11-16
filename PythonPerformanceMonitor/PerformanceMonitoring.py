

def long_running_fibbonacci(n):
    fib = [0, 1]
    t1 = time.time()    

    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
        # print(f"Fibonacci({i}) = {fib[-1]}")
    

n = 20000

#region Time

import time

def implement_time_package():
    t1 = time.time()
    long_running_fibbonacci(n)
    t2 = time.time()
    print(f'TIME:Total time it took: {t2-t1} seconds')

implement_time_package()


#endregion


#region Timeit

import timeit

# Approach 1
start = timeit.default_timer()
print(f'TIMEIT: Started the function call at: {start}')
long_running_fibbonacci(n)
print(f'TIMEIT: Time taken reported by timeint approach 1: {timeit.default_timer() - start}')

# Approach 2
CODE_BLOCK = '''
# long_running_fibbonacci(20000)
# '''
times = timeit.timeit(stmt=CODE_BLOCK, globals=globals(), number=1)
print(f'TIMEIT: Time taken reported by timeint approach 2: {times}')

#endregion

#region LineProfiler

# USE COMMAND - kernprof -lv PerformanceMonitoring.py
import line_profiler

@line_profiler.profile
def long_running_fibbonacci(n):
    fib = [0, 1]

    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
        # print(f"Fibonacci({i}) = {fib[-1]}")


long_running_fibbonacci(20000)

#endregion


#region MemoryProfiler

# USE COMMAND - python -m memory_profiler PerformanceMonitoring.py

import memory_profiler

@memory_profiler.profile
def long_running_fibbonacci(n):
    fib = [0, 1]

    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
        # print(f"Fibonacci({i}) = {fib[-1]}")


long_running_fibbonacci(20000)
#endregion