import random as rnd

data = [2, 4, 6, 8, 42, 73]

print(f'{data = }')
rnd.shuffle(data)
print(f'{data = }')

print(f'{rnd.sample(data, 3) = }')
print(f'{rnd.sample(data, 3, counts=[1, 1, 1, 1, 1, 100]) = }')
