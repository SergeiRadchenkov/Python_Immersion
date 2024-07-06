def func(positional_only_parameters, /, positional_or_keyword_parameters, *, keyword_only_parameters):
    pass


def standard_arg(arg):
    '''Пример обычной функции'''
    print(arg)  # Принтим для примера, а не для привычки


standard_arg(42)
standard_arg(arg=42)
