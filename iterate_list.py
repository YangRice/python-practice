import time

# Measurement methods
def measure_time(func, input, n_loop=10000):
    start = time.time()
    for _ in range(n_loop):
        func(input)
    return time.time() - start




def for_loop(input):
    for x in input:
        yield x * 2

def for_range(input):
    for i in range(len(input)):
        yield input[i] * 2

def for_enumerate(input):
    for i, x in enumerate(input):
        yield x * 2

def list_comprehension(input):
    return [x * 2 for x in input]
    
def range_list_comprehension(input):
    return [input[i] * 2 for i in range(len(input))]
    
def list_enumerate_comprehension(input):
    return [x * 2 for i, x in enumerate(input)]

print('Check results: [0, 2, 4, 6, 8]')

x = list(range(5))
print(f'for_loop: {for_loop(x)}')
print(f'for_range: {for_range(x)}')
print(f'for_enumerate: {for_enumerate(x)}')
print(f'list(for_loop): {list(for_loop(x))}')
print(f'list(for_range): {list(for_range(x))}')
print(f'list(for_enumerate): {list(for_enumerate(x))}')
print(f'list_comprehension: {list_comprehension(x)}')
print(f'range_list_comprehension: {range_list_comprehension(x)}')
print(f'enumerate_list_comprehension: {list_enumerate_comprehension(x)}')


print('Time measurement')

x = list(range(100))
print(f'for_loop: {measure_time(for_loop, x)}')
print(f'for_range: {measure_time(for_range, x)}')
print(f'for_enumerate: {measure_time(for_enumerate, x)}')
print(f'list(for_loop): {measure_time(lambda x: list(for_loop(x)), x)}')
print(f'list(for_range): {measure_time(lambda x: list(for_range(x)), x)}')
print(f'list(for_enumerate): {measure_time(lambda x: list(for_enumerate(x)), x)}')
print(f'list_comprehension: {measure_time(list_comprehension, x)}')
print(f'range_list_comprehension: {measure_time(range_list_comprehension, x)}')
print(f'enumerate_list_comprehension: {measure_time(list_enumerate_comprehension, x)}')