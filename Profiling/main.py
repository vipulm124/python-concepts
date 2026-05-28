import cProfile
import pstats
from io import StringIO


def finonacci(n):
    if n < 2:
        return n
    return finonacci(n-1) +  finonacci(n-2)


def process_data() -> list:
    results = []
    for i in range(30):
        results.append(finonacci(i))

    return results

profiler = cProfile.Profile()
profiler.enable()

process_data()

profiler.disable()

s = StringIO()
ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
ps.print_stats(10)
print(s.getvalue())

