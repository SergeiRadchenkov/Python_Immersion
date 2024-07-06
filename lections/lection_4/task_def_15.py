def combine_example(pos_only, /, standart, *, kwd_only):
    '''Пример функции со всеми вариантами параметров'''
    print(pos_only, standart, kwd_only) # Принтим для примера, а не для привычки


# combine_example(1, 2, 3) # TypeError: combine_example() takes 2 positional arguments but 3 were given
combine_example(1, 2, kwd_only=3)
combine_example(1, standart=2, kwd_only=3)
combine_example(1, kwd_only=2, standart=3)
# combine_example(pos_only=1, standart=2, kwd_only=3) # TypeError: combine_example() got some positional-only arguments passed as keyword arguments: 'pos_only'