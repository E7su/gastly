#!/usr/bin/python
# import sys  # for another input

def set_input():
    massiv = [5, 5, 5, 7, 6, 4, 5, 5, 5]
    pattern = 7
    massiv = input('>>> Please, enter array: ')
    pattern = input('>>> Please, enter pattern: ')
    # input = sys.stdin.read()  # more performance with this input
    # massiv, pattern = map(int, input.split(''))    
    print('Type of the sequence: {}'.format(type(massiv)))
    print('Massiv: {}'.format(massiv))
    print('Pattern: {}\n'.format(pattern))
    return massiv, pattern

def has_element(massiv, pattern):
    print('>>> Has_element')
    if [x for x in massiv if x == pattern]:
        return True
    else:
        return False

def linear_match(massiv, pattern):
    print('>>> Linear_match')
    return [x for x in massiv if x == pattern]

def linear_search(massiv, pattern):
    print('>>> Linear_search')
    for index, element in enumerate(massiv):
        if element == pattern:
	    return index
        else:
            return -1

def main():
    massiv, pattern = set_input()
    
    result_has_element = has_element(massiv, pattern)
    print('Result: {}'.format(result_has_element))
    
    result_match = linear_match(massiv, pattern)
    print('Result: {}'.format(result_match))

    result_search = linear_search(massiv, pattern)
    print('Result: {}'.format(result_search))


if __name__ == '__main__':
    main()
