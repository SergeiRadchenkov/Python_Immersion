import random as rnd

print(f'{rnd.random() = }')
rnd.seed(42)
state = rnd.getstate()
print(f'{state = }')
print(f'{rnd.random() = }')
print(f'{rnd.random() = }')
rnd.setstate(state)
print(f'{rnd.random() = }')
print(f'{rnd.random() = }')
