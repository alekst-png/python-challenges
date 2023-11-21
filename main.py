# test function
def print_hi(name):
    print(f'Hi, {name}')


# merge two arrays and sort
def merge(num1, m, num2, n):
    for i in range(n):
        num1[m + i] = num2[i]
    num1.sort()
    return num1



class Main(object):
    # merge two arrays and sort
    array = merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    for i in range(6):
        print(array[i])
