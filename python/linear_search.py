# import sys  # for another input

def set_input():
    # massiv = [5, 5, 5, 7, 6, 4, 5, 5, 5]
    # pattern = 7

    massiv = input('>>> Please, enter array: ')
    pattern = input('>>> Please, enter pattern: ')
    # input = sys.stdin.read()  # more performance with this input
    # massiv, pattern = map(int, input.split(''))

    print('Type of the sequence: {}'.format(type(massiv)))
    print('Massiv: {}'.format(massiv))
    print('Pattern: {}\n'.format(pattern))
    return massiv, pattern

def linear_match(massiv, pattern):
    print('Linear_match with list comprehension...')
    return [element for element in massiv if element == pattern]

def has_element(massiv, pattern):
    print('>>> Has_element method')
    match = linear_match(massiv, pattern)
    if match:
        return True
    else:
        return False

def linear_search(massiv, pattern):
    print('>>> Linear_search with list comprehension')
    return [index for index, element in enumerate(massiv) if element == pattern]

def find_element(massiv, pattern):
    print('>>> Find_element method...')
    index = linear_search(massiv, pattern)
    if not index:
        index = -1
    return index

def main():
    massiv, pattern = set_input()
    
    result_has_element = has_element(massiv, pattern)
    print('Result: {}\n'.format(result_has_element))
    
    result_find_element = find_element(massiv, pattern)
    print('Result: {}\n'.format(result_find_element))


if __name__ == '__main__':
    main()
