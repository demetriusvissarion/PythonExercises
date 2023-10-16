import time


def f(t0, array):
    t_offset = time.time() - t0
    dt = array[1, 0] - array[0, 0]
    while True:
        t = time.perf_counter_ns() - t_offset*1E9
        i = int(t/dt)
        if i >= len(array):
            break
        array[i, 1] += 1
    return array


for i in range(nprocesses):
    inarrays.append(np.copy(array))

p = Pool(processes=nthreads)
t0 = time.time()
outarrays = p.starmap(f, [(t0, array) for array in inarrays], chunksize=1)
