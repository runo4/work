import time


# 関数の実行時間を返す
def measure_time1(func):
    start = time.perf_counter_ns()
    func()
    end = time.perf_counter_ns()
    dt = end - start
    if dt >= 1000000000:
        # ns -> s
        dt = str(dt / 1000000000) + " s"
    elif dt >= 1000000:
        # ns -> ms
        dt = str(dt / 1000000) + " ms"
    elif dt >= 1000:
        # ns -> μs
        dt = str(dt / 1000) + " μs"
    else:
        dt = str(dt) + " ns"
    return dt


# 関数の実行時間を返す
def measure_time2(func, n):
    start = time.perf_counter_ns()
    func(n)
    end = time.perf_counter_ns()
    dt = end - start
    if dt >= 1000000000:
        # ns -> s
        dt = str(dt / 1000000000) + " s"
    elif dt >= 1000000:
        # ns -> ms
        dt = str(dt / 1000000) + " ms"
    elif dt >= 1000:
        # ns -> μs
        dt = str(dt / 1000) + " μs"
    else:
        dt = str(dt) + " ns"
    return dt
