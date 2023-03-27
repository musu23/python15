def get_sum_from_parameters(*args, **kwargs):
    total_sum = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total_sum += arg
        elif isinstance(arg, list):
            for elem in arg:
                if isinstance(elem, (int, float)):
                    total_sum += elem
    for value in kwargs.values():
        if isinstance(value, (int, float)):
            total_sum += value
    return total_sum


print(get_sum_from_parameters(1, 5, -3, 'abc', '12', [12, 56, 'cad']))
print(get_sum_from_parameters())
print(get_sum_from_parameters(2, 4, 'abc', param_1=2))
print(get_sum_from_parameters(2, 4, 'abc', param_1=2, param_2='abc'))

def get_rec_sum(n: int) -> tuple:
    if n == 0:
        return 0, 0, 0

    total_sum, even_sum, odd_sum = get_rec_sum(n - 1)

    total_sum += n
    if n % 2 ==0:
        even_sum += n
    else:
        odd_sum += n

    return total_sum, even_sum, odd_sum


total_sum, even_sum, odd_sum = get_rec_sum(5)
print('total_sum', total_sum)
print('even_sum', even_sum)
print('odd_sum', odd_sum)

def integer_from_kboard():
    try:
        value =int(input('Enter an integer: '))
        return value
    except ValueError:
        return 0

print(integer_from_kboard())








