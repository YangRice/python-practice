import time
import concurrent.futures
import multiprocessing

# Measurement methods
def measure_time(func, input, n_loop=100):
    start = time.time()
    for _ in range(n_loop):
        func(input)
    return (time.time() - start) / float(n_loop)

# Dummy IO function
def dummy_io(x):
    time.sleep(0.001)
    return x * 2


def for_loop(input):
    for x in input:
        yield dummy_io(x)

def for_range(input):
    for i in range(len(input)):
        yield dummy_io(input[i])

def for_enumerate(input):
    for i, x in enumerate(input):
        yield dummy_io(x)

def map_list(input):
    return map(dummy_io, input)

def thread_pool_executer_map(input):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as tpe:
        return tpe.map(dummy_io, input)

def multiprocessing_pool_map(input):
    with multiprocessing.Pool(processes=10) as mp:
        return mp.map(dummy_io, input)

def list_comprehension(input):
    return [dummy_io(x) for x in input]
    
def range_list_comprehension(input):
    return [dummy_io(input[i]) for i in range(len(input))]
    
def list_enumerate_comprehension(input):
    return [dummy_io(x) for i, x in enumerate(input)]

print('Check results: [0, 2, 4, 6, 8]')

x = list(range(5))
print(f'for_loop: {for_loop(x)}')
print(f'for_range: {for_range(x)}')
print(f'for_enumerate: {for_enumerate(x)}')
print(f'map: {map_list(x)}')
print(f'ThreadPoolExecuter.map: {thread_pool_executer_map(x)}')
print(f'multiprocess.Pool.map: {multiprocessing_pool_map(x)}')
print(f'list(for_loop): {list(for_loop(x))}')
print(f'list(for_range): {list(for_range(x))}')
print(f'list(for_enumerate): {list(for_enumerate(x))}')
print(f'list(map): {list(map_list(x))}')
print(f'list(ThreadPoolExecuter.map): {list(thread_pool_executer_map(x))}')
print(f'list_comprehension: {list_comprehension(x)}')
print(f'range_list_comprehension: {range_list_comprehension(x)}')
print(f'enumerate_list_comprehension: {list_enumerate_comprehension(x)}')


print('Time measurement')

x = list(range(100))
print(f'for_loop: {measure_time(for_loop, x)}')
print(f'for_range: {measure_time(for_range, x)}')
print(f'for_enumerate: {measure_time(for_enumerate, x)}')
print(f'map: {measure_time(map_list, x)}')
print(f'ThreadPoolExecuter.map: {measure_time(thread_pool_executer_map, x, 100)}')
print(f'multiprocess.Pool.map: {measure_time(multiprocessing_pool_map, x, 10)}')
print(f'list(for_loop): {measure_time(lambda x: list(for_loop(x)), x)}')
print(f'list(for_range): {measure_time(lambda x: list(for_range(x)), x)}')
print(f'list(for_enumerate): {measure_time(lambda x: list(for_enumerate(x)), x)}')
print(f'list(map): {measure_time(lambda x: list(map_list(x)), x)}')
print(f'list(ThreadPoolExecuter.map): {measure_time(lambda x: list(thread_pool_executer_map(x)), x)}')
print(f'list_comprehension: {measure_time(list_comprehension, x)}')
print(f'range_list_comprehension: {measure_time(range_list_comprehension, x)}')
print(f'enumerate_list_comprehension: {measure_time(list_enumerate_comprehension, x)}')