import time
import threading


def f(t0, array):
    dt = array[1, 0] - array[0, 0]
    while True:
        t = time.perf_counter_ns() - t0
        i = int(t/dt)
        if i >= len(array):
            break
        array[i, 1] += 1
    return None


t0 = time.perf_counter_ns()
for i in range(nthreads):
    arrays.append(np.copy(array))
    threads.append(threading.Thread(target=f, args=(t0, arrays[-1])))

for thread in threads:
    thread.start()
