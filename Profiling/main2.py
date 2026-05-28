from functools import lru_cache
import cProfile
import pstats
from io import StringIO

@lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n < 2:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)

def process_data():
    results = []
    for i in range(30):
        results.append(fibonacci_cached(i))
    return results

# Profile the function
profiler = cProfile.Profile()
profiler.enable()

process_data()

profiler.disable()

# Print results
s = StringIO()
ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
ps.print_stats(10)
print(s.getvalue())

