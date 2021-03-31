
def for_loop(input):
    for x in input:
        x = x * 2
    print('in function', input)

def for_range(input):
    for i in range(len(input)):
        input[i] = input[i] * 2
    print('in function', input)

def for_enumerate(input):
    for i, x in enumerate(input):
        input[i] = x * 2
    print('in function', input)

def list_comprehension(input):
    input = [x * 2 for x in input]
    print('in function', input)
    
def range_list_comprehension(input):
    input = [input[i] * 2 for i in range(len(input))]
    print('in function', input)
    
def list_enumerate_comprehension(input):
    input = [x * 2 for i, x in enumerate(input)]
    print('in function', input)

print('Check results: [0, 2, 4, 6, 8]')

x = list(range(5))
print(f'for_loop: ')
for_loop(x)
print('after function', x)

x = list(range(5))
print(f'for_range: ')
for_range(x)
print('after function', x)

x = list(range(5))
print(f'for_enumerate: ')
for_enumerate(x)
print('after function', x)

x = list(range(5))
print(f'list_comprehension: ')
list_comprehension(x)
print('after function', x)

x = list(range(5))
print(f'range_list_comprehension: ')
range_list_comprehension(x)
print('after function', x)

x = list(range(5))
print(f'list_enumerate_comprehension: ')
list_enumerate_comprehension(x)
print('after function', x)
