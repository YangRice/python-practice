import time
import itertools
import functools

# Measurement methods
def measure_time(func, input, n_loop=10000):
    start = time.time()
    for _ in range(n_loop):
        func(input)
    return time.time() - start




def for_loop(inputs):
    for input in inputs:
        for y in input:
            yield y

def list_comprehension(inputs):
    return [x for input in inputs for x in input]

def chain_from_iterable(inputs):
    return itertools.chain.from_iterable(inputs)

def reduce_list(inputs):
    return functools.reduce(lambda x, y: x + y, inputs)

def sum_list(inputs):
    return sum(inputs, [])



print('Check results: [1, 2, 3, 4, 5, 6, 7, 8, 9]')

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'for_loop: {for_loop(x)}')
print(f'list(for_loop): {list(for_loop(x))}')
print(f'list_comprehension: {list_comprehension(x)}')
print(f'chain_from_iterable: {chain_from_iterable(x)}')
print(f'list(chain_from_iterablechain_list): {list(chain_from_iterable(x))}')
print(f'reduce_list: {reduce_list(x)}')
print(f'sum_list: {sum_list(x)}')


print('Time measurement')

x = [list(range(10) for _ in range(10))]    # 10 x 10
print(f'for_loop: {measure_time(for_loop, x)}')
print(f'list(for_loop): {measure_time(lambda x: list(for_loop(x)), x)}')
print(f'list_comprehension: {measure_time(list_comprehension, x)}')
print(f'chain_from_iterable: {measure_time(chain_from_iterable, x)}')
print(f'list(chain_from_iterable): {measure_time(lambda x: list(chain_from_iterable(x)), x)}')
print(f'reduce_list: {measure_time(reduce_list, x)}')
print(f'sum_list: {measure_time(sum_list, x)}')
