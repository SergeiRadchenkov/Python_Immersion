def mean(args):
    return sum(args) / len(args)


print(mean([1, 2, 3]))
# print(mean(1, 2, 3))  # TypeError: mean() takes 1 positional argument but 3 were given

def mean(*args):
    return sum(args) / len(args)


print(mean(*[1, 2, 3]))
print(mean(1, 2, 3))